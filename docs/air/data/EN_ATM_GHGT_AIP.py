import aiohttp
import asyncio
import json
import pandas as pd
import plotly.graph_objects as go
import sys
from datetime import datetime
import dash
from dash import dcc, html

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
    file_path = f'data-commons/dist/air/data/dcid/{file_name}'

    # Fetch and combine data
    country_data = await parse_country_data(country_codes)
    EU_data = await fetch_eu_data()
    combined_data = await combine_data(country_data, EU_data)

    # Save data with specified name
    await save_data_to_json(combined_data, file_path)

    # Load and display data
    data_example = await load_data_from_json(file_path)
    json.dump({"EN_ATM_GHGT_AIP_Data": combined_data}, sys.stdout)

    # Initialize the Dash app
    app = dash.Dash(__name__)

    # Define the layout of the app
    app.layout = html.Div([
        dcc.Dropdown(
            id='country-select',
            options=[{'label': country['country_code'], 'value': country['country_code']} for country in combined_data],
            value=['USA'],  # Default value
            multi=True
        ),
        dcc.Dropdown(
            id='graph-type-select',
            options=[
                {'label': 'Line Graph', 'value': 'line'},
                {'label': 'Heatmap', 'value': 'heatmap'},
                {'label': 'Stacked Area Plot', 'value': 'area'},
                {'label': 'Pie Chart', 'value': 'pie'}
            ],
            value='line'  # Default value
        ),
        dcc.Graph(id='EN_ATM_GHGT_AIP_Data-graph')
    ])

    @app.callback(
        dash.dependencies.Output('EN_ATM_GHGT_AIP_Data-graph', 'figure'),
        [dash.dependencies.Input('country-select', 'value'),
         dash.dependencies.Input('graph-type-select', 'value')]
    )
    def update_graph(selected_countries, graph_type):
        traces = []
        layout = {
            'title': 'Emissions Data Visualization',
            'xaxis': {'title': 'Year'},
            'yaxis': {'title': 'Emissions (Metric Tons)'}
        }

        if graph_type == 'heatmap':
            z_data = []
            for country in selected_countries:
                country_data = next(item for item in combined_data if item["country_code"] == country)
                years = [data['year'] for data in country_data['data']]
                values = [data['emission'] for data in country_data['data']]
                z_data.append(values)
            traces = [go.Heatmap(z=z_data, x=years, y=selected_countries)]
            layout['title'] = 'Emissions Heatmap'

        elif graph_type == 'pie':
            total_emissions = []
            for country in selected_countries:
                country_data = next(item for item in combined_data if item["country_code"] == country)
                total_emissions.append(sum(data['emission'] for data in country_data['data']))
            traces = [go.Pie(labels=selected_countries, values=total_emissions)]
            layout['title'] = 'Total Emissions Distribution'

        else:  # Default to line or stacked area plot
            mode = 'lines+markers' if graph_type == 'line' else 'lines'
            stackgroup = 'one' if graph_type == 'area' else None

            for country in selected_countries:
                country_data = next(item for item in combined_data if item["country_code"] == country)
                years = [data['year'] for data in country_data['data']]
                values = [data['emission'] for data in country_data['data']]
                traces.append(go.Scatter(x=years, y=values, mode=mode, stackgroup=stackgroup, name=country_data["country_code"]))

            layout['title'] = 'Emissions Trend'

        return {
            'data': traces,
            'layout': layout
        }

    # Run the app
    app.run_server(debug=True)

# Run the main function
asyncio.run(main())
