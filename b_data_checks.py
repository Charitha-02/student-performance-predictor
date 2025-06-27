# b_data_checks.py

import pandas as pd

# Load the dataset
data = pd.read_csv("d_data/StudentsPerformance.csv")

print("✅ Dataset Loaded Successfully")

# Check for missing values
print("\n🔍 Checking for Missing Values:")
print(data.isnull().sum())

# Check data types
print("\n🔍 Data Types:")
print(data.dtypes)

# Check basic statistics
print("\n📊 Basic Statistical Info:")
print(data.describe(include='all'))

# Check for duplicates
print("\n🔁 Duplicate Records Count:", data.duplicated().sum())
