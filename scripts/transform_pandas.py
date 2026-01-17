import pandas as pd
import json
import os
from datetime import datetime

def transform_energy_data():
    raw_dir = "data/raw"
    processed_dir = "data/processed"
    
    if not os.path.exists(processed_dir):
        os.makedirs(processed_dir)

    # 1. Find the latest raw data
    files = [f for f in os.listdir(raw_dir) if f.endswith('.json')]
    if not files:
        print("The file to be processed could not be found!")
        return
    
    latest_file = os.path.join(raw_dir, sorted(files)[-1])
    
    # 2. Read the JSON file and convert it to a DataFrame
    with open(latest_file, 'r') as f:
        data = json.load(f)
    
    df = pd.DataFrame(data['Prices'])

    # 3. Split the 'readingDate' column into Date and Time
    # First, we convert the column to a datetime object.
    df['readingDate'] = pd.to_datetime(df['readingDate'])
    
    df['Date'] = df['readingDate'].dt.date
    df['Time'] = df['readingDate'].dt.time

    # 4. Add the 'Price_with_VAT' column, including 21% VAT
    # Formul: Price * 1.21
    df['Price_with_VAT'] = (df['price'] * 1.21).round(4)

    # 5. Edit column names and data types
    df = df.rename(columns={
        'price': 'Base_Price',
        'readingDate': 'Timestamp'
    })

    # Let's make the column order more readable.
    cols = ['Timestamp', 'Date', 'Time', 'Base_Price', 'Price_with_VAT']
    df = df[cols]

    # 6. Save as Parquet
    output_filename = f"energy_processed_{datetime.now().strftime('%Y%m%d')}.parquet"
    output_path = os.path.join(processed_dir, output_filename)
    
    df.to_parquet(output_path, engine='pyarrow')

    # Check the results
    print("--- Transformation Process Successful ---")
    print(df.head())
    print("\nData Types:")
    print(df.dtypes)

if __name__ == "__main__":
    transform_energy_data()