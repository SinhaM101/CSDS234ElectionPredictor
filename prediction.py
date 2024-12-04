import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np
from electionResults import *

# Load the dataset
file_path = 'Updated_Education_Data.csv'  # Update with your actual file path
data = pd.read_csv(file_path)
data = data[data['State']=="Pennsylvania"]

data['Winner'] = data['County'].apply(
    lambda x: 'REPUBLICAN' if x in republican_counties_2020 
    else ('DEMOCRAT' if x in democrat_counties_2020 else 'UNKNOWN')
)




# Convert target to binary (A=0, B=1)
data['Winner'] = data['Winner'].map({'DEMOCRAT': 0, 'REPUBLICAN': 1})

# Features and target
X = data[['Value (Percent)']]
y = data['Winner']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print("Accuracy:", accuracy)
print("Confusion Matrix:\n", conf_matrix)



new_data_path = 'mejorenlace.csv'  # Update with your actual file path
new_data = pd.read_csv(new_data_path)

# Ensure the dataset contains the feature used for training
if 'Value (Percent)' not in new_data.columns:
    raise ValueError("New data must contain the 'Value (Percent)' column.")

# Use the trained model to predict for the new dataset
new_data['Winner'] = model.predict(new_data[['Value (Percent)']])

# Map binary predictions back to party names
new_data['Winner'] = new_data['Winner'].map({0: 'DEMOCRAT', 1: 'REPUBLICAN'})

# Count the total predictions for each party
party_counts = new_data['Winner'].value_counts()

# Determine the overall winner
presidential_winner = party_counts.idxmax()

print("Predicted County Results:\n", new_data[['County', 'Winner']])
print("\nOverall Predicted Presidential Winner:", presidential_winner)

