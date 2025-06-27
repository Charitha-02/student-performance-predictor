import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load the data
data = pd.read_csv("d_data/StudentsPerformance.csv")

# Preprocessing
data['gender'] = data['gender'].map({'female': 0, 'male': 1})
data['race/ethnicity'] = data['race/ethnicity'].astype('category').cat.codes
data['parental level of education'] = data['parental level of education'].astype('category').cat.codes
data['lunch'] = data['lunch'].map({'standard': 1, 'free/reduced': 0})
data['test preparation course'] = data['test preparation course'].map({'none': 0, 'completed': 1})

# Features and target
X = data.drop(columns=['math score'])
y = data['math score']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
best_model = RandomForestRegressor(n_estimators=100, random_state=42)
best_model.fit(X_train, y_train)

# Save the trained model to file
with open("d_data/best_model.pkl", "wb") as f:
    pickle.dump(best_model, f)

print("✅ Model saved successfully at d_data/best_model.pkl")
