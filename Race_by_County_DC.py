import pandas as pd
#Monish Sinha
#Clean the Race by county

df = pd.read_csv("dataverse_files/Race by County/Graham_Race_Data.csv")

# Remove the word "County" from the 'County' column
df['County'] = df['County'].str.replace(r'\bCounty\b', '', regex=True).str.strip()

# Split the column into two new columns
df[['County', 'State']] = df['County'].str.split(',', expand=True)

# Adjust column order: Move the State column to the right of County
column_order = ['County', 'State'] + [col for col in df.columns if col not in ['County', 'State']]
df = df[column_order]

# Remove leading/trailing whitespace from the new columns
df['County'] = df['County'].str.strip()
df['State'] = df['State'].str.strip()

df.to_csv("Cleaned_Race_Data.csv", index=False)

print("Cleaned data saved to 'Cleaned_Race_Data.csv'")