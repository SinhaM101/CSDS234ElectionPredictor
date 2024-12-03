import pandas as pd
#Monish Sinha
#Clean the Education personal income by county

# File Paths
file_paths = {
    "Arizona": "dataverse_files/Education by County/Arizona Counties Education Data.csv",
    "Georgia": "dataverse_files/Education by County/Georgia Counties Education Data.csv",
    "Michigan": "dataverse_files/Education by County/Michigan Counties Education Data.csv",
    "Pennsylvania": "dataverse_files/Education by County/Pennsylvania Counties Education Data.csv",
    "Wisconsin": "dataverse_files/Education by County/Wisconsin Counties Education Data.csv",
    "New Hampshire": "dataverse_files/Education by County/New Hampshire Counties Education Data.csv",
    "Ohio": "dataverse_files/Education by County/Ohio Counties Education Data.csv",
    "Nevada": "dataverse_files/Education by County/Nevada Counties Education Data.csv",
    "Florida": "dataverse_files/Education by County/Florida Counties Education Data.csv",
}

# Function to load and clean a single file
def load_clean_csv(file_path):
    # Load the file, skipping the first 5 rows
    data = pd.read_csv(file_path, skiprows=5)
    # Remove the last 6 rows
    if len(data) > 6:  # Ensure there are enough rows to drop
        data = data.iloc[:-6]

    # Remove rows where "GeoName" column equals "United States"
    if 'County' in data.columns:  # Ensure the column exists
        data = data[data['County'] != "United States"]
    return data

# Process each file
cleaned_data = {}
for state, path in file_paths.items():
    cleaned_data[state] = load_clean_csv(path)

# Combine all states into one DataFrame
combined_data = pd.concat(cleaned_data.values(), ignore_index=True)


# Save the cleaned data to a CSV file
combined_data.to_csv("Cleaned_Education_Data.csv", index=False)

print("Cleaned data saved to 'Cleaned_Education_Data.csv'.")