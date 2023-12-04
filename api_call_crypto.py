import requests
import json
import os
import csv
import time
from datetime import datetime

def load_data_from_api(api_url):
    try:
        
        response = requests.get(api_url)
        if response.status_code == 200:
            
            data = response.json()
            return data['data']
        else:
            
            print(f"Error found: Unable to fetch data. Status code: {response.status_code}")
            return None
    except Exception as e:
        
        print(f"Error: {e}")
        return None

def save_data_to_csv(data, csv_file_path):
    try:
        
        os.makedirs(os.path.dirname(csv_file_path), exist_ok=True)

        
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        file_path_with_timestamp = f"{csv_file_path}_{timestamp}.csv"

        with open(file_path_with_timestamp, 'a', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())

            
            if csv_file.tell() == 0:
                csv_writer.writeheader()

            
            csv_writer.writerows(data)
        
        print(f"Data appended to {file_path_with_timestamp}")
    except Exception as e:
        print(f"Error: {e}")


api_url = "https://api.coincap.io/v2/assets"


base_csv_file_path = "/Users/supatra_mac/downloads/crypto_lates_price"


duration_seconds = 120


interval_seconds = 5


num_iterations = duration_seconds // interval_seconds


for _ in range(num_iterations):
    data = load_data_from_api(api_url)

    
    if data:
        save_data_to_csv(data, base_csv_file_path)

    
    time.sleep(interval_seconds)
