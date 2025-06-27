# e_model_training.py
import pandas as pd
import pickle
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor

# Load dataset
df = pd.read_csv('d_data/StudentsPerformance.csv')
X = df.drop('math score', axis=1)
y = df['math score']

# Identify categorical columns
categorical = X.select_dtypes(include='object').columns.tolist()

# ColumnTransformer for preprocessing
preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical)
], remainder='passthrough')

# Full pipeline: preprocessing + model
pipeline = Pipeline([
    ('preprocessing', preprocessor),
    ('model', RandomForestRegressor())
])

# Fit the pipeline
pipeline.fit(X, y)

# Save the pipeline as best_model.pkl
with open('d_data/best_model.pkl', 'wb') as f:
    pickle.dump(pipeline, f)

print("✅ Model trained and saved as 'best_model.pkl'")
