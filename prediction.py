import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np

# Load the dataset
file_path = 'predicted_election_winners.csv'  # Update with your actual file path
data = pd.read_csv(file_path)

# Clean the dataset: Select relevant columns and clean percentage values
valid_data = data[data['Bachelors_Degree_Percent'].str.contains('%', na=False)]  # Keep only rows with valid percentages
valid_data['Bachelors_Degree_Percent'] = valid_data['Bachelors_Degree_Percent'].str.replace('%', '').astype(float)


# Generate synthetic labels for demonstration (e.g., 0 = Candidate A, 1 = Candidate B)
# In a real scenario, labels would come from actual data.
np.random.seed(42)


# Prepare data for modeling
X = data[['Bachelors_Degree_Percent']]
y = data['Winner']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Add predictions back to the cleaned dataset
data['Predicted_Winner'] = model.predict(X)

# Save the predictions to a new CSV file
output_file = 'pbrrrr.csv'
data.to_csv(output_file, index=False)

print(f"Predictions saved to {output_file}")
