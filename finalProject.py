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

income_data['Swing_Direction'] = income_data['County'].apply(
    lambda x: 'Left' if x in list_swung_left else ('Right' if x in list_swung_right else 'No Swing')
)

swing_data = income_data[income_data['Swing_Direction'].isin(['Left', 'Right'])]

# Create the box plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=swing_data, x='Swing_Direction', y='Income_Difference_2020_2016', palette='Set2')
plt.title('Income Change (2016-2020) by Swing Direction')
plt.xlabel('Swing Direction')
plt.ylabel('Income Change (2020 - 2016)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Show the plot
#plt.show()


data_path = 'Updated_Education_Data.csv'
education_data = pd.read_csv(data_path)

education_data['Swing_Direction'] = education_data['County'].apply(
    lambda x: 'Left' if x in list_swung_left else ('Right' if x in list_swung_right else 'No Swing')
)
swing_dader = education_data[education_data['Swing_Direction'].isin(['Left', 'Right'])]


plt.figure(figsize=(10, 6))
sns.boxplot(
    x='Swing_Direction',
    y='Value (Percent)',
    data=swing_dader,
    palette='coolwarm'
)
plt.title("Education Levels by Swing Direction (2020 Election)", fontsize=16)
plt.xlabel("Swing Direction", fontsize=12)
plt.ylabel("% with At Least a Bachelor's Degree", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()



file_path = 'Per_capita_PI_by_County_Uppercase.csv'
infdata = pd.read_csv(file_path)


inflation_factors = {
    2016: 240.0,
    2017: 245.0,
    2018: 250.0,
    2019: 255.0,
    2020: 260.0
}

# Normalize inflation factors to 2020
adjustment_factors = {year: inflation_factors[2020] / value for year, value in inflation_factors.items()}

# Adjust income values for inflation
adjusted_data = infdata.copy()
for year in range(2016, 2021):
    adjusted_data[str(year)] *= adjustment_factors[year]

# Reshape data for plotting
melted_data = adjusted_data.melt(id_vars=["County", "State"], 
                                 value_vars=[str(year) for year in range(2016, 2021)],
                                 var_name="Year", 
                                 value_name="Adjusted Income")
melted_data["Year"] = melted_data["Year"].astype(int)

# Specify the counties to plot
selected_counties = list_swung_left  # Replace with your list of counties

# Filter data for the selected counties
selected_data = melted_data[melted_data["County"].isin(selected_counties)]

# Plotting
plt.figure(figsize=(12, 8))
for county in selected_counties:
    county_data = selected_data[selected_data["County"] == county]
    plt.plot(county_data["Year"], county_data["Adjusted Income"], marker='o', label=county)

plt.title("Per Capita Personal Income by Counties that Swung Left (Inflation-Adjusted)", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Adjusted Income (2020 Dollars)", fontsize=12)
plt.legend(title="County", fontsize=10)
plt.grid(True)
plt.show()



