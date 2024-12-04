import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load U.S. county shapefile data
shapefile_url = "https://www2.census.gov/geo/tiger/TIGER2020/COUNTY/tl_2020_us_county.zip"
counties = gpd.read_file(shapefile_url)

# Load education data
education_path = "Updated_Education_Data.csv"  # Replace with the correct file path
education_data = pd.read_csv(education_path)

# Ensure `county_fips` (FIPS) is numeric for merging
education_data['FIPS'] = pd.to_numeric(education_data['FIPS'], errors='coerce')
counties['FIPS'] = pd.to_numeric(counties['GEOID'], errors='coerce')

# Drop rows with missing FIPS in either dataset
education_data.dropna(subset=['FIPS'], inplace=True)
counties.dropna(subset=['FIPS'], inplace=True)

# Merge the shapefile with education data
geo_merged_education = counties.merge(
    education_data[['FIPS', 'Value (Percent)']],  # Using 'Value (Percent)' as education level
    on='FIPS',
    how='left'
)

# Rename column for easier interpretation
geo_merged_education.rename(columns={'Value (Percent)': 'education_percent'}, inplace=True)

# Plot the education map
fig, ax = plt.subplots(figsize=(20, 20))  # Adjust size for clarity
geo_merged_education.plot(
    column='education_percent',  # Column for education levels
    cmap='Purples',  # Use a purple color map where darker means more educated
    legend=True,  # Add a legend
    legend_kwds={
        'label': "Percent with at Least Bachelor's Degree",
        'orientation': "vertical"
    },
    missing_kwds={"color": "grey", "label": "No Data"},  # Highlight missing data in grey
    ax=ax
)

# Set title and formatting
ax.set_title('Education Levels by County (2020)', fontsize=24)
ax.axis('off')  # Remove axes for better visualization

# Save and show the map
plt.tight_layout()
plt.savefig("education_map.png", dpi=300)  # Save as a high-resolution image
plt.show()