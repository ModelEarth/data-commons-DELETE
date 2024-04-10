import datacommons as dc

# Retrieve all counties in Georgia (state code: 13)
georgia_counties_info = dc.get_places_in(['geoId/13'], 'County')

# Extract the DCIDs of the counties
georgia_counties_dcids = georgia_counties_info['geoId/13']

# Fetch LandCoverFraction_Forest data for each county in Georgia
forest_cover_data = {}
for county_dcid in georgia_counties_dcids:
    forest_cover_data[county_dcid] = dc.get_stat_all([county_dcid], ["LandCoverFraction_Forest"])

print(forest_cover_data)

# pulls all available years but its out of order and will need to sort it with a JSON parser in descending/ascending order:
# 'LandCoverFraction_Forest': {'sourceSeries': [{'val': {'2015': 57.712213157748906, '2019': 56.10225251926496, '2017': 57.329201724571796, '2016': 57.08418588188137, '2018': 58.540199494228055}