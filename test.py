import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# Load Election Data
data = pd.read_csv('dataverse_files/countypres_2000-2020.csv')

# Filter relevant data
data = data[
    (data['year'].isin([2016, 2020])) &
    (data['state'].isin(['GEORGIA', 'PENNSYLVANIA', 'WISCONSIN', 'ARIZONA',
                         'OHIO', 'FLORIDA', 'NORTH CAROLINA', 'NEW HAMPSHIRE', 'NEVADA']))
]

# Aggregate candidate votes
data_grouped = (
    data.groupby(['year', 'state', 'county_name', 'party'])['candidatevotes']
    .sum()
    .reset_index()
)

# Identify winning parties
winning_parties = (
    data_grouped.loc[data_grouped.groupby(['year', 'state', 'county_name'])['candidatevotes'].idxmax()]
    .reset_index(drop=True)
)

# Pivot to compare 2016 and 2020
pivoted_data = winning_parties.pivot(index=['state', 'county_name'], columns='year', values='party').reset_index()
pivoted_data.columns = ['state', 'county_name', 'party_2016', 'party_2020']

# Identify swung counties
swung_counties = pivoted_data[pivoted_data['party_2016'] != pivoted_data['party_2020']]
list_swung = list(swung_counties['county_name'])
total_counties = list(data['county_name'].unique())

# List of non-swung counties
list_not_swung = [county for county in total_counties if county not in list_swung]

# Load Income Data
income_data = pd.read_csv('Per_capita_PI_by_County.csv')

# Ensure consistency in county names
income_data = income_data[income_data['GeoName'].isin(total_counties)]

# Assign flipped status
income_data['flipped'] = income_data['GeoName'].apply(lambda x: 1 if x in list_swung else 0)

# Validate necessary columns for income change
if '2016' in income_data.columns and '2017' in income_data.columns:
    income_data['income_change'] = income_data['2017'] - income_data['2016']
else:
    raise ValueError("Columns '2016' and '2017' are missing from income data.")

# Correlation Analysis
if income_data['income_change'].notnull().sum() >= 2 and income_data['flipped'].notnull().sum() >= 2:
    corr, p_value = pearsonr(income_data['income_change'], income_data['flipped'])
    print(f"Pearson Correlation (Income Change vs Flipped): {corr:.2f}, P-value: {p_value:.2e}")
else:
    print("Insufficient data to calculate Pearson correlation.")

# Visualizations
if len(income_data['flipped'].unique()) > 1 and len(income_data['income_change'].unique()) > 1:
    # Boxplot
    sns.boxplot(x='flipped', y='income_change', data=income_data)
    plt.xticks([0, 1], ['Not Flipped', 'Flipped'])
    plt.title('Income Change (2017-2016) by Flipped Status')
    plt.ylabel('Income Change')
    plt.xlabel('Flipped Status')
    plt.show()

    # Scatter plot
    sns.scatterplot(x='income_change', y='flipped', data=income_data)
    plt.title('Income Change vs. Flipped Status')
    plt.ylabel('Flipped Status')
    plt.xlabel('Income Change (2017-2016)')
    plt.show()
else:
    print("Not enough variability in the data for visualizations.")
