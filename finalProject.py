import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

from electionResults import *
from PIbyCDataCleaning import *



election_data = pd.read_csv('filtered_county_presidential_data.csv')
income_data = pd.read_csv('Per_capita_PI_by_County.csv')


income_data['GeoName'] = income_data['GeoName'].str.upper()

# Filter income data to include only relevant counties
income_data = income_data[income_data['GeoName'].isin(totalcounties)]

# Step 2: Assign flipped status
income_data['flipped'] = income_data['GeoName'].apply(
    lambda x: 1 if x in swung_counties else 0
)

# Step 3: Calculate year-to-year changes
income_data['income_change'] = income_data['2017'] - income_data['2016']

# Step 4: Correlation Analysis
corr, p_value = pearsonr(income_data['income_change'], income_data['flipped'])
print(f"Pearson Correlation (Income Change vs Flipped): {corr:.2f}, P-value: {p_value:.2e}")

# Step 5: Visualizations
# Boxplot for income change
sns.boxplot(x='flipped', y='income_change', data=income_data)
plt.xticks([0, 1], ['Not Flipped', 'Flipped'])
plt.title('Income Change (2017-2016) by Flipped Status')
plt.ylabel('Income Change')
plt.xlabel('Flipped Status')
plt.show()

# Scatter plot for income change vs flipped status
sns.scatterplot(x='income_change', y='flipped', data=income_data)
plt.title('Income Change vs. Flipped Status')
plt.ylabel('Flipped Status')
plt.xlabel('Income Change (2017-2016)')
plt.show()