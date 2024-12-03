import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load elements
income_path = "Per_capita_PI_by_County_Uppercase.csv"
election_path = "dataverse_files/countypres_2000-2020.csv"

income_data = pd.read_csv(income_path)
election_data = pd.read_csv(election_path)

# Filter 2020 data and calculate Democratic vote share
election_2020 = election_data[(election_data['year'] == 2020) & (election_data['mode'] == 'TOTAL')]
election_2020 = election_2020[election_2020['party'] == 'DEMOCRAT'].copy()  # Ensure party name matches dataset
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
merged_data.rename(columns={'2020': 'income', 'vote_share': 'democratic_vote_share'}, inplace=True)

# Step 2: Get U.S. county shapefile data
shapefile_url = "https://www2.census.gov/geo/tiger/TIGER2020/COUNTY/tl_2020_us_county.zip"
counties = gpd.read_file(shapefile_url)

# Prepare FIPS codes for merging (ensure integer type)
counties['county_fips'] = pd.to_numeric(counties['GEOID'], errors='coerce')

# Step 3: Merge shapefile with election and income data
geo_merged = counties.merge(merged_data, on='county_fips', how='left')

# Step 4: Plot choropleth maps

# Democratic Vote Share Map
fig1, ax1 = plt.subplots(figsize=(20, 20))
geo_merged.plot(
    column='democratic_vote_share',
    cmap='Blues',  # Blue for Democrats
    legend=True,
    legend_kwds={
        'orientation': "vertical"  # Vertical color bar
    },
    missing_kwds={"color": "grey", "label": "No Data"},
    ax=ax1
)
ax1.set_title('Democratic Vote Share by County (2020)', fontsize=24)
ax1.axis('off')
plt.tight_layout()
plt.savefig("democratic_vote_share_map.png", dpi=300)  # Save as a high-resolution image
plt.show()

# Per Capita Income Map
fig2, ax2 = plt.subplots(figsize=(20, 20))
geo_merged.plot(
    column='income',
    cmap='Greens',  # Changed to 'Greens' for variety
    legend=True,  # Add legend for income map
    legend_kwds={
        'orientation': "vertical",  # Vertical legend for income
        'shrink': 0.5,
        'aspect': 20
    },
    missing_kwds={"color": "grey", "label": "No Data"},
    ax=ax2
)
ax2.set_title('Per Capita Income by County Democratic(2020)', fontsize=24)
ax2.axis('off')
plt.tight_layout()
plt.savefig("democratic_income_map_fixed.png", dpi=300)  # Save as a high-resolution image
plt.show()