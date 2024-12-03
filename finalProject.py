import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

from electionResults import *
from PIbyCDataCleaning import *



election_data = pd.read_csv('filtered_county_presidential_data.csv')
income_data = pd.read_csv('Per_capita_PI_by_County_Uppercase.csv')
income_data['2016'] = pd.to_numeric(income_data['2016'], errors='coerce')
income_data['2020'] = pd.to_numeric(income_data['2020'], errors='coerce')
income_data = income_data[income_data['County'].isin(totalcounties)]
income_data['Flipped'] = income_data['County'].apply(lambda x: 1 if x in list_swung else 0)
income_data['Income_Difference_2020_2016'] = income_data['2020'] - income_data['2016']


income_column = 'Income_Difference_2020_2016'
flipped_column = 'Flipped'

grouped_data = income_data.groupby('Flipped')['Income_Difference_2020_2016'].mean().reset_index()

# Map flipped status to descriptive labels
grouped_data['Flipped'] = grouped_data['Flipped'].map({0: 'Not Flipped', 1: 'Flipped'})

# Plot the bar chart
plt.figure(figsize=(8, 6))
plt.bar(grouped_data['Flipped'], grouped_data['Income_Difference_2020_2016'], color=['blue', 'orange'])
plt.title('Average Income Change (2016 to 2020) by Flipping Status')
plt.xlabel('Flipping Status')
plt.ylabel('Average Income Change')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Show the plot
plt.show()

X = income_data[['Income_Difference_2020_2016']].values
y = income_data['Flipped'].values

# Standardize the independent variable for better logistic regression performance
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Fit the logistic regression model
log_reg = LogisticRegression()
log_reg.fit(X_scaled, y)

# Generate predictions for a range of income changes
income_change_range = np.linspace(X.min(), X.max(), 300).reshape(-1, 1)
income_change_range_scaled = scaler.transform(income_change_range)
probabilities = log_reg.predict_proba(income_change_range_scaled)[:, 1]

# Plot the logistic regression curve
plt.figure(figsize=(8, 6))
plt.plot(income_change_range, probabilities, label='Logistic Regression', color='red')
sns.scatterplot(data=income_data, x='Income_Difference_2020_2016', y='Flipped', alpha=0.6, color='blue', label='Data Points')
plt.title('Logistic Regression: Income Change vs Flipping Probability')
plt.xlabel('Income Change (2020 - 2016)')
plt.ylabel('Flipping Probability')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()