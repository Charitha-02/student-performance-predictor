# a_data_collection.py

import pandas as pd
import os

# Create folder path if not exists
DATA_PATH = "d_data/StudentsPerformance.csv"

# Check if the dataset exists
if os.path.exists(DATA_PATH):
    print("✅ Dataset found.")
    data = pd.read_csv(DATA_PATH)
    print("✅ First 5 rows of the dataset:")
    print(data.head())
else:
    print("❌ Dataset not found. Please check the path:", DATA_PATH)
