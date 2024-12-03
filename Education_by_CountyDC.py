import pandas as pd
#Monish Sinha
#Clean the Education personal income by county

# File Paths
file_paths = {
    "Arizona": "dataverse_files/Education by County/Arizona Counties Education Data.csv",
    "Georgia": "GEORGIA DATA.csv",
    "Michigan": "dataverse_files/Education by County/Michigan Counties Education Data.csv",
    "Pennsylvania": "PENNSYLVANIADATA.csv",
    "Wisconsin": "WISCONSINDATA.csv",
    "Ohio": "dataverse_files/Education by County/Ohio Counties Education Data.csv",
    "Nevada": "dataverse_files/Education by County/Nevada Counties Education Data.csv",
    "Florida": "dataverse_files/Education by County/Florida Counties Education Data.csv",
}

# Function to load and clean a single file
def load_clean_csv(file_path, state):
    # Load the file, skipping the first 5 rows
    data = pd.read_csv(file_path, skiprows=5)
    # Remove the last 6 rows
    if len(data) > 6:  # Ensure there are enough rows to drop
        data = data.iloc[:-6]

    # List of state names to exclude
    states_to_exclude = [
        "Arizona", "Georgia", "Michigan", "Pennsylvania", "Wisconsin",
         "Ohio", "Nevada", "Florida"
    ]
    # Remove rows where GeoName matches any state name in the exclusion list
    data = data[~data['County'].isin(states_to_exclude)]

    # Add a new column for State
    data['State'] = state  # Add the state name to a new column

    # Remove the last word in the County column
    data['County'] = data['County'].str.rsplit(' ', n=1).str[0]

    # Adjust column order: Move the State column to the right of County
    column_order = ['County', 'State'] + [col for col in data.columns if col not in ['County', 'State']]
    data = data[column_order]

    # Remove rows where "GeoName" column equals "United States"
    if 'County' in data.columns:  # Ensure the column exists
        data = data[data['County'] != "United"]
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