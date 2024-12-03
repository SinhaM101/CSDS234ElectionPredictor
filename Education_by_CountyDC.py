import pandas as pd
#Monish Sinha
#Clean the Education personal income by county

# File Paths
file_paths = {
    "Arizona": "Education by County Predictive\ARIZONADATA.csv",
    "Georgia": "Education by County Predictive/GEORGIA DATA.csv",
    "Michigan": "Education by County Predictive/MICHIGANDATA.csv",
    "Pennsylvania": "Education by County Predictive/PENNSYLVANIADATA.csv",
    "Wisconsin": "Education by County Predictive/WISCONSINDATA.csv",
    "Ohio": "Education by County Predictive/OHIODATA.csv",
    "Nevada": "Education by County Predictive/NEVADADATA.csv",
    "Florida": "Education by County Predictive/FLORIDADATA.csv"
}
print("HEY")
# Function to load and clean a single file
def load_clean_csv(file_path, state):
    # Load the file, skipping the first 5 rows
    data = pd.read_csv(file_path, skiprows=82)
    # Remove the last 6 rows
    if len(data) > 6:  # Ensure there are enough rows to drop
        data = data.iloc[:-6]

    # List of state names to exclude
    states_to_exclude = [
        "Arizona", "Georgia", "Michigan", "Pennsylvania", "Wisconsin",
         "Ohio", "Nevada", "Florida"
    ]
    # Remove rows where GeoName matches any state name in the exclusion list
    data = data[~data['county'].isin(states_to_exclude)]

    # Add a new column for State
    data['State'] = state  # Add the state name to a new column

    # Remove the last word in the County column
    data['county'] = data['county'].str.rsplit(' ', n=1).str[0]

    # Adjust column order: Move the State column to the right of County
    column_order = ['county', 'State'] + [col for col in data.columns if col not in ['county', 'State']]
    data = data[column_order]

    # Remove rows where "GeoName" column equals "United States"
    if 'county' in data.columns:  # Ensure the column exists
        data = data[data['county'] != "United"]
    return data

# Process each file
cleaned_data = {}
for state, path in file_paths.items():
    cleaned_data[state] = load_clean_csv(path, state)

# Combine all states into one DataFrame
combined_data = pd.concat(cleaned_data.values(), ignore_index=True)


# Save the cleaned data to a CSV file
combined_data.to_csv("NewEducationCraftedData", index=False)

print("Cleaned data saved to 'Cleaned_Education_Data.csv'.")