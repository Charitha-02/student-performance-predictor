import streamlit as st
import pandas as pd
import pickle
import os

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), "d_data", "best_model.pkl")
model = pickle.load(open(model_path, "rb"))

# Streamlit page setup
st.set_page_config(page_title="Student Performance Predictor", layout="centered")
st.title("📚 Student Performance Predictor")
st.write("Enter the student details below to predict the exam score:")

# Input form
gender = st.selectbox("Gender", ["female", "male"])
race_ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
parental_education = st.selectbox("Parental Level of Education", [
    "some high school", "high school", "some college", "associate's degree", "bachelor's degree", "master's degree"
])
lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
test_prep = st.selectbox("Test Preparation Course", ["none", "completed"])
reading_score = st.slider("Reading Score", 0, 100, 70)
writing_score = st.slider("Writing Score", 0, 100, 70)

# Map inputs to DataFrame
input_data = pd.DataFrame({
    "gender": [gender],
    "race/ethnicity": [race_ethnicity],
    "parental level of education": [parental_education],
    "lunch": [lunch],
    "test preparation course": [test_prep],
    "reading score": [reading_score],
    "writing score": [writing_score]
})

# Predict button
if st.button("Predict Math Score"):
    prediction = model.predict(input_data)
    st.success(f"🎯 Predicted Math Score: {prediction[0]:.2f}")
