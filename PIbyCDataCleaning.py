import pandas as pd
#Monish Sinha

def load_filter_data(file_path, keyword = "Per capita personal income"):
    data = pd.read_csv(file_path)
    #filter data to include only rows that include keyword
    filtered_data = data[data['Description'].str.contains(keyword, case = False, na = False)]
    return filtered_data

# File Paths
az_path = "dataverse_files/Annual Personal Income by County/CAINC1_AZ_1969_2023.csv"
ga_path = "dataverse_files/Annual Personal Income by County/CAINC1_GA_1969_2023.csv"
mi_path = "dataverse_files/Annual Personal Income by County/CAINC1_MI_1969_2023.csv"
pa_path = "dataverse_files/Annual Personal Income by County/CAINC1_PA_1969_2023.csv"
wi_path = "dataverse_files/Annual Personal Income by County/CAINC1_WI_1969_2023.csv"

#Load and Flter Paths
az_data = load_filter_data(az_path)
ga_data = load_filter_data(ga_path)
mi_data = load_filter_data(mi_path)
pa_data = load_filter_data(pa_path)
wi_data = load_filter_data(wi_path)

print(az_data)

