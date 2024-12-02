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




print("Filtered Data Preview:\n", filteredData.head())


