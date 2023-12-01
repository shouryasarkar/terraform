import requests
import json
import os
import csv
import time
from datetime import datetime

def load_data_from_api(api_url):
    try:
        # Make GET request to the API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON data from the response
            data = response.json()
            return data['data']
        else:
            # Print an error message if the request was not successful
            print(f"Error: Unable to fetch data. Status code: {response.status_code}")
            return None
    except Exception as e:
        # Handle exceptions, e.g., network issues
        print(f"Error: {e}")
        return None

def save_data_to_csv(data, csv_file_path):
    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(csv_file_path), exist_ok=True)

        # Write the data to a CSV file with a timestamp in the file name
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        file_path_with_timestamp = f"{csv_file_path}_{timestamp}.csv"

        with open(file_path_with_timestamp, 'a', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())

            # If the file is empty, write the header
            if csv_file.tell() == 0:
                csv_writer.writeheader()

            # Write data
            csv_writer.writerows(data)
        
        print(f"Data appended to {file_path_with_timestamp}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage with the CoinCap API for cryptocurrency prices
api_url = "https://api.coincap.io/v2/assets"

# Define the base file path where you want to save the cryptocurrency prices in CSV format
base_csv_file_path = "/Users/supatra_mac/downloads/cryptocurrency_prices"

# Set the duration for which API calls will be made (2 minutes)
duration_seconds = 120

# Set the interval between API calls (10 seconds)
interval_seconds = 5

# Calculate the number of iterations
num_iterations = duration_seconds // interval_seconds

# Make API calls at regular intervals
for _ in range(num_iterations):
    data = load_data_from_api(api_url)

    # Save the cryptocurrency prices to a CSV file with a timestamp
    if data:
        save_data_to_csv(data, base_csv_file_path)

    # Wait for the specified interval before making the next API call
    time.sleep(interval_seconds)
