import pandas as pd
#Monish Sinha
#Clean the Per capita personal income by county
def load_filter_data(file_path, keyword = "Per capita personal income"):
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

    columns_to_keep = ["GeoFIPS", "GeoName", "Region", "Description"] + [str(year) for year in range(2016, 2021)]
    filtered_data = filtered_data[columns_to_keep]
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
az_data = load_filter_data(az_path)
ga_data = load_filter_data(ga_path)
mi_data = load_filter_data(mi_path)
pa_data = load_filter_data(pa_path)
wi_data = load_filter_data(wi_path)
nh_data = load_filter_data(nh_path)
oh_data = load_filter_data(oh_path)
nv_data = load_filter_data(nv_path)
fl_data = load_filter_data(fl_path)

#Combine all filtered data into single Data Frame
combined_data = pd.concat([az_data, ga_data, mi_data, pa_data, wi_data, nh_data, oh_data, nv_data, fl_data], ignore_index=True)
print(combined_data)

combined_data.to_csv("Per_capita_PI_by_County.csv", index = False)
print("CSV file created successfully.")
