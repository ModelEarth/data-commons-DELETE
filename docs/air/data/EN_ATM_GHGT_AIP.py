import aiohttp
import asyncio
import json
from datetime import datetime

async def fetch_data(session, url, params):
    async with session.get(url, params=params) as response:
        return await response.json()

async def parse_country_data(country_codes):
    country_data = []
    url = 'https://api.datacommons.org/stat/series'

    async with aiohttp.ClientSession() as session:
        tasks = []
        for code in country_codes:
            params = {'place': f'country/{code}', 'stat_var': 'sdg/EN_ATM_GHGT_AIP'}
            tasks.append(fetch_data(session, url, params))
        responses = await asyncio.gather(*tasks)

        for code, response in zip(country_codes, responses):
            if 'series' in response:
                country_data.append({
                    "country_code": code,
                    "data": [{"year": year, "emission": value} for year, value in response['series'].items()]
                })
            else:
                print(f'No data available for {code}.')
    return country_data

async def fetch_eu_data():
    url = 'https://api.datacommons.org/stat/series'
    params = {'place': 'undata-geo/G00500360', 'stat_var': 'sdg/EN_ATM_GHGT_AIP'}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            eu_data = await response.json()
            if 'series' in eu_data:
                EU_data = [{"country_code": "EU", "data": [{"year": year, "emission": value} for year, value in eu_data['series'].items()]}]
                print(f'Data fetched for European Union:', EU_data)
                return EU_data
            else:
                print("No EU data available.")
                return []

async def combine_data(country_data, EU_data):
    combined_data = country_data + EU_data if EU_data else country_data
    for country in combined_data:
        country["data"] = sorted(country["data"], key=lambda x: x["year"])
    return combined_data

async def save_data_to_json(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f'Data saved to {file_path}')

async def load_data_from_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

async def main():
    # Define country codes and file paths
    country_codes = ['AUS', 'AUT', 'BEL', 'BGR', 'BLR', 'CAN', 'CHE', 'CYP', 'CZE', 'DEU',
                     'DNK', 'ESP', 'EST', 'FIN', 'FRA', 'GBR', 'GRC', 'HRV', 'HUN', 'IRL',
                     'ISL', 'ITA', 'JPN', 'LIE', 'LTU', 'LUX', 'LVA', 'MCO', 'MLT', 'NLD',
                     'NOR', 'NZL', 'POL', 'PRT', 'ROU', 'RUS', 'SVK', 'SVN', 'SWE', 'TUR',
                     'UKR', 'USA']
    file_name = "EN_ATM_GHGT_AIP_series.json"
    file_path = f'./{file_name}'

    # Fetch and combine data
    country_data = await parse_country_data(country_codes)
    EU_data = await fetch_eu_data()
    combined_data = await combine_data(country_data, EU_data)

    # Save data to specified path
    await save_data_to_json(combined_data, file_path)

    # Load and print an example of the saved data (optional)
    data_example = await load_data_from_json(file_path)
    print(data_example)

# Run the main function
asyncio.run(main())
