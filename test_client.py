import requests
import pandas as pd
import json
import argparse
from requests.exceptions import RequestException, HTTPError, ConnectionError, Timeout, TooManyRedirects

# Step 4
# Define the URL of the service
url = 'http://localhost:49200/process'

# Set up argument parsing
parser = argparse.ArgumentParser(description='Classify financial articles.')
parser.add_argument('input_path', type=str, help='Path to the input CSV file')
parser.add_argument('output_path', type=str, help='Path to the output CSV file')

args = parser.parse_args()

# Define input and output file paths
input_path = args.input_path
output_path = args.output_path

# Read the input CSV file
df = pd.read_csv(input_path)

# Convert dataframe to CSV
df.to_csv('temp_input.csv', index=False)

# Create a request payload
payload = {
    'inPath': 'temp_input.csv',
    'outPath': output_path
}

try:
    # Send a POST request to the service
    response = requests.post(url, json=payload)
    response.raise_for_status()  # Raise error for bad response status
    
    # Print the response
    print(response.json())

    # Load the output CSV and print it
    output_df = pd.read_csv(output_path)
    print(output_df)

except (RequestException, HTTPError, ConnectionError, Timeout, TooManyRedirects) as e:
    print(f"Error occurred: {e}")

except json.JSONDecodeError as json_err:
    print(f"JSON decoding error: {json_err}")

except Exception as ex:
    print(f"Unexpected error occurred: {ex}")

# example
# python classify_financial_articles.py
# python test_client.py input_file.csv output_file.csv
# python test_client.py new_articles.csv classified_articles.csv