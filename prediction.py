import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data_path = "Education by County Predictive/PENNSYLVANIADATA.csv"  # Replace with your CSV file name
try:
    data = pd.read_csv(data_path)
except FileNotFoundError:
    print("File not found. Make sure 'key_counties_data.csv' is in the same directory.")
    exit()

# Check if required columns exist
required_columns = ['Bachelors_Degree_Percent', 'Winner']
if not all(col in data.columns for col in required_columns):
    print(f"Dataset must contain the following columns: {', '.join(required_columns)}")
    exit()

# Encode the Winner column into numerical values (e.g., 0 for Candidate A, 1 for Candidate B)
data['Winner'] = data['Winner'].astype('category').cat.codes

# Features and target
X = data[['Bachelors_Degree_Percent']]
y = data['Winner']

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest Classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Calculate and display accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Predict the winner for the entire dataset
data['Predicted_Winner'] = model.predict(X)
data['Predicted_Winner'] = data['Predicted_Winner'].map({idx: cat for cat, idx in data['Winner'].astype('category').cat.categories.items()})

# Save the predictions to a new CSV file
output_file = "predicted_election_winners.csv"
data.to_csv(output_file, index=False)
print(f"Predictions saved to {output_file}")