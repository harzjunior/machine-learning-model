# Here’s an example of how you might write a Python script to send a request to your service:

import requests
import pandas as pd
import json

# Step 4
# Define the URL of the service
url = 'http://localhost:49200'

# Create a sample dataframe with the same structure as your input CSV
data = {
    'id': [1199],
    'body': ["European Union antitrust regulators have given the go-ahead for Royal Dutch Shell to buy competitor BG Group, which will lead to the creation of one of the richest and biggest oil companies. The EU commissioner for competition, Margrethe Vestager, found that the £47bn (€64bn, $72bn) acquisition would not prevent fair competition in the oil market."]
}
df = pd.DataFrame(data)

# Convert dataframe to CSV
df.to_csv('temp_input.csv', index=False)

# Define input and output file paths
input_path = 'temp_input.csv'
output_path = 'temp_output.csv'

# Create a request payload
payload = {
    'inPath': input_path,
    'outPath': output_path
}

# Send a POST request to the service
response = requests.post(url, json=payload)

# Print the response
print(response.json())

# Load the output CSV and print it
output_df = pd.read_csv(output_path)
print(output_df)
