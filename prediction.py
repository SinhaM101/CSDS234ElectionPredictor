import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

from electionResults import *
# Load your dataset
# Ensure it has columns: ['County', 'State', 'Year', '% Bachelor's Degree', 'Winner']
data = pd.read_csv('')

# Filter data for swing states
swing_states = ['GEORGIA', 'PENNSYLVANIA', 'WISCONSIN', 'ARIZONA','OHIO','FLORIDA''NORTH CAROLINA', 'NEW HAMPSHIRE', 'NEVADA']
data = data[data['State'].isin(swing_states)]

# Select features and target
features = ['% Bachelor\'s Degree']  # Add more features if available
target = 'Winner'  # Binary: 0 (Right) or 1 (Left)

X = data[features]
y = data[target]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Predict for a specific year
new_year_data = pd.DataFrame({
    '% Bachelor\'s Degree': [30, 35, 40, 25, 50]  # Example percentages for swing counties
})
predictions = model.predict(new_year_data)
print("Predicted Winners:", predictions)