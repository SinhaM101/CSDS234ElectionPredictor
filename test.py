import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load election data
election_data_path = "dataverse_files/countypres_2000-2020.csv"
election_data = pd.read_csv(election_data_path)

# Load income data
income_data_path = "Per_capita_PI_by_County.csv"
income_data = pd.read_csv(income_data_path)

# Print columns in income_data to confirm column names
print("Income Data Columns:", income_data.columns)

# Filter election data for 2016 and 2020 swing states
filtered_election_data = election_data[
    (election_data['year'].isin([2016, 2020])) & 
    (election_data['state'].isin(['GEORGIA', 'PENNSYLVANIA', 'WISCONSIN', 'ARIZONA', 
                                  'OHIO', 'FLORIDA', 'NORTH CAROLINA', 'NEW HAMPSHIRE', 'NEVADA']))
]

# Aggregate votes by year, state, county, and party
aggregated_data = (
    filtered_election_data.groupby(['year', 'state', 'county_name', 'party'])['candidatevotes']
    .sum()
    .reset_index()
)

# Determine winning party for each county
winning_parties = (
    aggregated_data.loc[aggregated_data.groupby(['year', 'state', 'county_name'])['candidatevotes'].idxmax()]
    .reset_index(drop=True)
)

# Pivot data to compare parties between 2016 and 2020
pivoted_data = winning_parties.pivot(index=['state', 'county_name'], columns='year', values='party').reset_index()
pivoted_data.columns.name = None
pivoted_data.columns = ['state', 'county_name', 'party_2016', 'party_2020']

# Identify swung counties
pivoted_data['swung'] = pivoted_data['party_2016'] != pivoted_data['party_2020']

# Merge with income data
pivoted_data = pivoted_data.merge(income_data, how='left', left_on='county_name', right_on='County')

# Check merged dataframe columns
print("Merged Data Columns:", pivoted_data.columns)

# Ensure 'Per_Capita_Income' is present
if 'Per_Capita_Income' not in pivoted_data.columns:
    raise ValueError("Column 'Per_Capita_Income' is missing from the merged dataset. Check the income data file.")

# Visualize distribution of per capita income for swung and non-swung counties
plt.figure(figsize=(10, 6))
sns.boxplot(
    x='swung',
    y='Per_Capita_Income',
    data=pivoted_data,
    palette='Set2'
)
plt.title("Per Capita Income in Swung vs Non-Swung Counties (2016-2020)")
plt.xlabel("Swung (True = County Swung)")
plt.ylabel("Per Capita Income")
plt.xticks([0, 1], ['Non-Swung', 'Swung'])
plt.tight_layout()
plt.show()

# Scatter plot of income vs swing status
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x='Per_Capita_Income',
    y='swung',
    data=pivoted_data,
    hue='state',
    palette='tab10'
)
plt.title("Relationship Between Per Capita Income and Swing Status")
plt.xlabel("Per Capita Income")
plt.ylabel("Swung (1 = True, 0 = False)")
plt.legend(title="State")
plt.tight_layout()
plt.show()
