import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

from electionResults import *
from PIbyCDataCleaning import *



election_data = pd.read_csv('filtered_county_presidential_data.csv')
per_cap_data = pd.read.csv('Per_capita_PI_by_County.csv')


flipped = data[data['flipped'] == 1]
not_flipped = data[data['flipped'] == 0]

# Calculate Pearson correlation
correlation, p_value = pearsonr(data['personal_income'], data['flipped'])

# Print correlation result
print(f"Pearson Correlation: {correlation}")
print(f"P-value: {p_value}")

# Visualization: Boxplot to compare personal income
plt.figure(figsize=(10, 6))
sns.boxplot(x='flipped', y='personal_income', data=data, palette='Set2')
plt.xticks([0, 1], ['Not Flipped', 'Flipped'])
plt.title('Personal Income Distribution by Flipping Status')
plt.xlabel('Flipping Status')
plt.ylabel('Personal Income')
plt.show()

# Visualization: Distribution plot for personal income
plt.figure(figsize=(10, 6))
sns.kdeplot(flipped['personal_income'], label='Flipped', shade=True)
sns.kdeplot(not_flipped['personal_income'], label='Not Flipped', shade=True)
plt.title('Personal Income Distribution for Flipped vs Not Flipped Counties')
plt.xlabel('Personal Income')
plt.ylabel('Density')
plt.legend()
plt.show()

# Scatter plot for personal income vs flipping status
plt.figure(figsize=(10, 6))
sns.scatterplot(x='personal_income', y='flipped', data=data, alpha=0.6)
plt.title('Scatter Plot of Personal Income vs Flipping Status')
plt.xlabel('Personal Income')
plt.ylabel('Flipping Status (0 = Not Flipped, 1 = Flipped)')
plt.show()
