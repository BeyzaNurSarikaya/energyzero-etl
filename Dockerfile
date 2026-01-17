FROM apache/airflow:2.7.1

# Copy the requirements.txt file into the container
COPY requirements.txt /requirements.txt

# Load the dependencies
RUN pip install --no-cache-dir -r /requirements.txt