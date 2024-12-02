import pandas as pd
#Monish Sinha
#Clean the Education personal income by county

# File Paths
"""
az_path = "dataverse_files/Education by County/Arizona Counties Education Data.csv"
ga_path = "dataverse_files/Education by County/Georgia Counties Education Data.csv"
mi_path = "dataverse_files/Education by County/Michigan Counties Education Data.csv"
pa_path = "dataverse_files/Education by County/Pennsylvania Counties Education Data.csv"
wi_path = "dataverse_files/Education by County/Wisconsin Counties Education Data.csv"
nh_path = "dataverse_files/Education by County/New Hampshire Counties Education Data.csv"
oh_path = "dataverse_files/Education by County/Ohio Counties Education Data.csv"
nv_path = "dataverse_files/Education by County/Nevada Counties Education Data.csv"
fl_path = "dataverse_files/Education by County/Florida Counties Education Data.csv"




az_data = pd.read_csv(az_path)
ga_data = pd.read_csv(ga_path)
mi_data = pd.read_csv(mi_path)
pa_data = pd.read_csv(pa_path)
wi_data = pd.read_csv(wi_path)
nh_data = pd.read_csv(nh_path)
oh_data = pd.read_csv(oh_path)
nv_data = pd.read_csv(nv_path)
fl_data = pd.read_csv(fl_path)
"""
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
    return data

