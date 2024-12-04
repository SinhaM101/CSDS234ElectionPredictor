import pandas as pd

file_path = "dataverse_files/countypres_2000-2020.csv"
data = pd.read_csv(file_path)



year = data['year']
state = data['state']
state_po = data['state_po']
county_name = data['county_name']
county_fips = data['county_fips']
office = data['office']
candidate = data['candidate']
party = data['party']
candidatevotes = data['candidatevotes']
totalvotes = data['totalvotes']
mode = data['mode']
version = data['version']


filteredData = data[
    (data['year'].isin([2016, 2020])) &
    (data['state'].isin(['GEORGIA', 'PENNSYLVANIA', 'WISCONSIN', 'ARIZONA','OHIO','FLORIDA''NORTH CAROLINA', 'NEW HAMPSHIRE', 'NEVADA']))
]




aggregated_data = (
    filteredData.groupby(['year', 'state', 'county_name', 'party'])['candidatevotes']
    .sum()
    .reset_index()
)

winning_parties = (
    aggregated_data.loc[aggregated_data.groupby(['year', 'state', 'county_name'])['candidatevotes'].idxmax()]
    .reset_index(drop=True)
)



pivoted_data = winning_parties.pivot(index=['state', 'county_name'], columns='year', values='party').reset_index()
pivoted_data.columns.name = None
pivoted_data.columns = ['state', 'county_name', 'party_2016', 'party_2020']
swung_counties = pivoted_data[pivoted_data['party_2016'] != pivoted_data['party_2020']]


democrat_counties_2020 = winning_parties[
    (winning_parties['year'] == 2020) & (winning_parties['party'] == 'DEMOCRAT')
]['county_name'].tolist()


republican_counties_2020 = winning_parties[
    (winning_parties['year'] == 2020) & (winning_parties['party'] == 'REPUBLICAN')
]['county_name'].tolist()

list_swung = list(swung_counties['county_name'])

totalcounties = list(filteredData['county_name'].unique())

list_not_swung = [county for county in totalcounties if county not in list_swung]

swung_counties_right = swung_counties[swung_counties['party_2020'] == 'REPUBLICAN']
list_swung_right = list(swung_counties_right['county_name'])
swung_counties_left = swung_counties[swung_counties['party_2020'] == 'DEMOCRAT']
list_swung_left = list(swung_counties_left['county_name'])
list_swung_left.pop(0)
list_swung_left.pop(0)
list_swung_left.pop(0)
list_swung_left.remove("MONTGOMERY")


print(list_swung_left)
