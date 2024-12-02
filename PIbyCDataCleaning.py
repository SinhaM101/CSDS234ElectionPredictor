import pandas as pd
#Monish Sinha

azfile_path = "dataverse_files/Annual Personal Income by County/CAINC1_AZ_1969_2023.csv"
azdata = pd.read_csv(azfile_path)

print(azdata)

