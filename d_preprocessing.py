import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load data
data = pd.read_csv("d_data/StudentsPerformance.csv")

# Display first few rows before encoding
print("Before Encoding:")
print(data.head())

# Encode categorical variables
label_cols = ["gender", "race/ethnicity", "parental level of education", "lunch", "test preparation course"]
label_encoders = {}

for col in label_cols:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

# Display first few rows after encoding
print("\nAfter Encoding:")
print(data.head())

# Save the preprocessed data for next steps
data.to_csv("d_data/StudentsPerformance_preprocessed.csv", index=False)
print("\nPreprocessed data saved as 'StudentsPerformance_preprocessed.csv'")
