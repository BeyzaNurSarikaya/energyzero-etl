from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys

# The /opt/airflow directory is the root directory within the Airflow container.
# We are adding this path so that it can find the scripts.
sys.path.append('/opt/airflow')

from scripts.extract_energyzero import fetch_energy_data
from scripts.transform_pandas import transform_energy_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'energyzero_etl_pipeline',
    default_args=default_args,
    description='EnergyZero API ETL Pipeline',
    schedule_interval='@daily',
    catchup=False
) as dag:

    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=fetch_energy_data
    )

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_energy_data
    )

    extract_task >> transform_task