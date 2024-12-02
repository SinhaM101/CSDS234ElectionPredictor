import pandas as pd

file_path = "dataverse_files/countypres_2000-2020.csv"
data = pd.read_csv(file_path)

# Assign columns to variables
year = data['year']
state = data['state']
state_po = data['state_po']
county_name = data['county_name']
county_fips = data['county_fips']
office = data['office']
candidate = data['candidate']
party = data['party']
candidatevotes = data['candidatevotes']
totalvotes = data['totalvotes']
mode = data['mode']
version = data['version']

# Display a summary of the variables
print("Year:")
print(year.head())
print("\nState:")
print(state.head())
print("\nState Postal Code:")
print(state_po.head())
print("\nCounty Name:")
print(county_name.head())
print("\nCounty FIPS:")
print(county_fips.head())
print("\nOffice:")
print(office.head())
print("\nCandidate:")
print(candidate.head())
print("\nParty:")
print(party.head())
print("\nCandidate Votes:")
print(candidatevotes.head())
print("\nTotal Votes:")
print(totalvotes.head())
print("\nMode:")
print(mode.head())
print("\nVersion:")
print(version.head())

# Optional: Process the data into a dictionary for further use
data_dict = {
    "year": year,
    "state": state,
    "state_po": state_po,
    "county_name": county_name,
    "county_fips": county_fips,
    "office": office,
    "candidate": candidate,
    "party": party,
    "candidatevotes": candidatevotes,
    "totalvotes": totalvotes,
    "mode": mode,
    "version": version
}

# Example: Print the first few rows of the processed data
data_processed = pd.DataFrame(data_dict)
print("\nProcessed Data (First 5 Rows):")
print(data_processed.head())
