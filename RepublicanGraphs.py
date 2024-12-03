import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

from electionResults import *
from PIbyCDataCleaning import *

# Load elements
income_path = "Per_capita_PI_by_County_Uppercase.csv"
election_path = "dataverse_files/countypres_2000-2020.csv"

income_data = pd.read_csv(income_path)
election_data = pd.read_csv(election_path)

# Filter 2020 data and calculate Republican vote share
election_2020 = election_data[(election_data['year'] == 2020) & (election_data['mode'] == 'TOTAL')]
election_2020 = election_2020[election_2020['party'] == 'REPUBLICAN'].copy()
election_2020['vote_share'] = election_2020['candidatevotes'] / election_2020['totalvotes']

# Prepare FIPS or standardized keys for merging
election_2020['County_State'] = election_2020['county_name'].str.upper() + ', ' + election_2020['state_po']
income_data['County_State'] = income_data['County'].str.upper() + ', ' + income_data['State']

# Merge election and income data
merged_data = pd.merge(
    election_2020[['County_State', 'vote_share', 'county_fips']],
    income_data[['County_State', '2020']],
    on='County_State',
    how='inner'
)
merged_data.rename(columns={'2020': 'income', 'vote_share': 'republican_vote_share'}, inplace=True)

# Step 2: Get U.S. county shapefile data
shapefile_url = "https://www2.census.gov/geo/tiger/TIGER2020/COUNTY/tl_2020_us_county.zip"
shapefile_path = "dataverse_files/shapefile.zip"  # Update to your path
counties = gpd.read_file(shapefile_url)

# Prepare FIPS codes for merging (ensure integer type)
counties['county_fips'] = pd.to_numeric(counties['GEOID'], errors='coerce')

# Step 3: Merge shapefile with election and income data
geo_merged = counties.merge(merged_data, on='county_fips', how='left')

# Step 4: Plot choropleth maps
# Increase the figure size
fig, ax = plt.subplots(1, 2, figsize=(30, 15))  # Larger figure size

# Map of Republican vote share
fig1, ax1 = plt.subplots(figsize=(20, 20))  # Increase size for clarity
geo_merged.plot(
    column='republican_vote_share',
    cmap='Reds',
    legend=True,
    legend_kwds={
        'label': "Republican Vote Share",
        'orientation': "vertical"  # Adjust legend orientation
    },
    missing_kwds={"color": "grey", "label": "No Data"},
    ax=ax1
)
ax1.set_title('Republican Vote Share by County (2020)', fontsize=24)
ax1.axis('off')
plt.tight_layout()
plt.savefig("republican_vote_share_map.png", dpi=300)  # Save as a high-resolution image (optional)
#plt.show()

# Map of Income
fig2, ax2 = plt.subplots(figsize=(20, 20))  # Increase size for clarity
geo_merged.plot(
    column='income',
    cmap='Blues',
    legend=False,
    missing_kwds={"color": "grey", "label": "No Data"},  # Define how missing data appears
    ax=ax2
)


ax2.set_title('Per Capita Income by County (2020)', fontsize=24)
ax2.axis('off')
plt.tight_layout()
plt.savefig("income_map_fixed.png", dpi=300)  # Save as a high-resolution image
plt.show()