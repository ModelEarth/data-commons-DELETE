import requests
import json
from datetime import datetime
import pandas as pd
import plotly.graph_objects as go
import os
import sys

# Get the current working directory
current_directory = os.getcwd()


def parse_country_data(country_codes):
    country_data = []

    # API endpoint for fetching statistical data
    url = 'https://api.datacommons.org/stat/series'

    # Fetching data for each country
    for code in country_codes:
        # Parameters for the API request
        params = {
            'place': f'country/{code}',
            'stat_var': 'sdg/EN_ATM_GHGT_AIP',
        }

        # Make the GET request
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            # Store each country's data as a record
            country_data.append({
                "country_code": code,
                "data": [{"year": year, "emission": value} for year, value in data.get('series', {}).items()]
            })
        else:
            print(f'Failed to fetch data for {code}. Status code: {response.status_code}')

    return country_data

# List of non-EU country codes. We can pull the list dynamically based on the technique above to check for all countries. Doing this for now.
country_codes = ['AUS', 'AUT', 'BEL', 'BGR', 'BLR', 'CAN', 'CHE', 'CYP', 'CZE', 'DEU',
                'DNK', 'ESP', 'EST', 'FIN', 'FRA', 'GBR', 'GRC', 'HRV', 'HUN', 'IRL',
                'ISL', 'ITA', 'JPN', 'LIE', 'LTU', 'LUX', 'LVA', 'MCO', 'MLT', 'NLD',
                'NOR', 'NZL', 'POL', 'PRT', 'ROU', 'RUS', 'SVK', 'SVN', 'SWE', 'TUR',
                'UKR', 'USA']

# Function to fetch data for the European Union
def fetch_eu_data():
    # API endpoint for fetching statistical data
    url = 'https://api.datacommons.org/stat/series'

    # Parameters for the API request
    params = {
        'place': 'undata-geo/G00500360',
        'stat_var': 'sdg/EN_ATM_GHGT_AIP',
    }

    # Make the GET request for the European Union
    response = requests.get(url, params=params)

    if response.status_code == 200:
        eu_data = response.json()
        if 'series' in eu_data:
            # Extract EU data
            EU_data = [{"country_code": "EU", "data": [{"year": year, "emission": value} for year, value in eu_data['series'].items()]}]
            print(f'Data fetched for European Union:', EU_data)
            return EU_data
        else:
            print("No EU data available.")
            return []
    else:
        print(f'Failed to fetch data for European Union. Status code:', response.status_code)
        return []

# Combine all data
def combine_data(country_data, EU_data):
    combined_data = country_data + EU_data if EU_data else country_data
    # Sorting the "data" list of each country dictionary by "year"
    for country in combined_data:
        country["data"] = sorted(country["data"], key=lambda x: x["year"])
    return combined_data

# Save data to a JSON file
def save_data_to_json(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f'Data saved to {file_path}')

# Function to load data from JSON file
def load_data_from_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

# Path to the JSON file containing the dataset
file_name = "data_sorted.json"
file_path = os.path.join(current_directory, file_name)


# Fetching data for non-EU countries
country_data = parse_country_data(country_codes)

# Fetching data for the European Union
EU_data = fetch_eu_data()

# Combine all data
combined_data = combine_data(country_data, EU_data)

# Save the data to a JSON file
save_data_to_json(combined_data, file_path)

# Load the data
sorted_concat_data = load_data_from_json(file_path)
