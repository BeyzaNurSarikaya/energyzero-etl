import requests
import json
import os
from datetime import datetime, timedelta

def fetch_energy_data():
    # API Parameters
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7) # One-week data target
    
    # EnergyZero API URL 
    url = f"https://api.energyzero.nl/v1/energyprices"
    params = {
        "fromDate": start_date.strftime("%Y-%m-%dT00:00:00.000Z"),
        "tillDate": end_date.strftime("%Y-%m-%dT23:59:59.999Z"),
        "interval": 4, # Hourly
        "usageType": 1 # Electricity
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        file_path = f"data/raw/energy_data_{datetime.now().strftime('%Y%m%d')}.json"
        
        with open(file_path, 'w') as f:
            json.dump(data, f)
        print(f"The data has been successfully retrieved and saved here: {file_path}")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    fetch_energy_data()