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
    (data['state'].isin(['GEORGIA', 'PENNSYLVANIA', 'WISCONSIN', 'ARIZONA']))
]


winning_parties = (
    filteredData.groupby(['year', 'state', 'county_name'])
    .apply(lambda group: group.loc[group['candidatevotes'].idxmax()][['party']])
    .reset_index()
)
pivoted_data = winning_parties.pivot(index=['state', 'county_name'], columns='year', values='party').reset_index()
pivoted_data.columns.name = None
pivoted_data.columns = ['state', 'county_name', 'party_2016', 'party_2020']
swung_counties = pivoted_data[pivoted_data['party_2016'] != pivoted_data['party_2020']]



print("Filtered Data Preview:\n", filteredData.head())


