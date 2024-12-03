import pandas as pd
#Monish Sinha
#Clean the Per capita personal income by county
def load_filter_data(file_path, state_name, keyword = "Per capita personal income"):
    data = pd.read_csv(file_path)
    #filter data to include only rows that include keyword
    filtered_data = data[data['Description'].str.contains(keyword, case = False, na = False)]
    #remove rows where GeoName is a state name
    # List of state names to exclude
    states_to_exclude = [
        "Arizona", "Georgia", "Michigan", "Pennsylvania", "Wisconsin",
        "New Hampshire", "Ohio", "Nevada", "Florida"
    ]
    # Remove rows where GeoName matches any state name in the exclusion list
    filtered_data = filtered_data[~filtered_data['GeoName'].isin(states_to_exclude)]

    # Rename GeoName to County
    filtered_data.rename(columns={'GeoName': 'County'}, inplace=True)

    # Extract only the county name (remove state abbreviation)
    filtered_data['County'] = filtered_data['County'].str.split(',').str[0]

    # Add a new column for State
    filtered_data['State'] = state_name  # Add the state name to a new column

    # Adjust column order: Move the State column to the right of County
    column_order = ['County', 'State'] + [col for col in filtered_data.columns if col not in ['County', 'State']]
    filtered_data = filtered_data[column_order]

    columns_to_keep = ["County","State", "Region", "Description"] + [str(year) for year in range(2016, 2021)]
    filtered_data = filtered_data[columns_to_keep]

    # Remove specific row with GeoName "Shawano (includes Menominee), WI*"
    filtered_data = filtered_data[filtered_data['County'] != "Shawano (includes Menominee), WI*"]

    return filtered_data

# File Paths
az_path = "dataverse_files/Annual Personal Income by County/CAINC1_AZ_1969_2023.csv"
ga_path = "dataverse_files/Annual Personal Income by County/CAINC1_GA_1969_2023.csv"
mi_path = "dataverse_files/Annual Personal Income by County/CAINC1_MI_1969_2023.csv"
pa_path = "dataverse_files/Annual Personal Income by County/CAINC1_PA_1969_2023.csv"
wi_path = "dataverse_files/Annual Personal Income by County/CAINC1_WI_1969_2023.csv"
nh_path = "dataverse_files/Annual Personal Income by County/CAINC1_NH_1969_2023.csv"
oh_path = "dataverse_files/Annual Personal Income by County/CAINC1_OH_1969_2023.csv"
nv_path = "dataverse_files/Annual Personal Income by County/CAINC1_NV_1969_2023.csv"
fl_path = "dataverse_files/Annual Personal Income by County/CAINC1_FL_1969_2023.csv"

#Load and Flter Paths
az_data = load_filter_data(az_path, "AZ")
ga_data = load_filter_data(ga_path, "GA")
mi_data = load_filter_data(mi_path, "MI")
pa_data = load_filter_data(pa_path, "PA")
wi_data = load_filter_data(wi_path, "WI")
nh_data = load_filter_data(nh_path, "NH")
oh_data = load_filter_data(oh_path, "OH")
nv_data = load_filter_data(nv_path, "NV")
fl_data = load_filter_data(fl_path, "FL")

#Combine all filtered data into single Data Frame
combined_data = pd.concat([az_data, ga_data, mi_data, pa_data, wi_data, nh_data, oh_data, nv_data, fl_data], ignore_index=True)
print(combined_data)

combined_data.to_csv("Per_capita_PI_by_County.csv", index = False)
print("CSV file created successfully.")
