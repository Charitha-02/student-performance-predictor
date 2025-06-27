# z_app.py
import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open('d_data/best_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title="Student Performance Predictor & Study Plan", layout="centered")

st.title("📊 Student Performance Predictor & Study Plan Generator")
st.markdown("Predict math score and get a customized study plan.")

# Input form
with st.form("prediction_form"):
    gender = st.selectbox("Gender", ["female", "male"])
    race = st.selectbox("Race/Ethnicity", [
        "group A", "group B", "group C", "group D", "group E"
    ])
    parental_edu = st.selectbox("Parental Level of Education", [
        "some high school", "high school", "some college", 
        "associate's degree", "bachelor's degree", "master's degree"
    ])
    lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
    test_prep = st.selectbox("Test Preparation Course", ["none", "completed"])
    reading_score = st.slider("Reading Score", 0, 100, 70)
    writing_score = st.slider("Writing Score", 0, 100, 70)

    submitted = st.form_submit_button("Predict Performance")

# Prediction logic
if submitted:
    input_df = pd.DataFrame([{
        "gender": gender,
        "race/ethnicity": race,
        "parental level of education": parental_edu,
        "lunch": lunch,
        "test preparation course": test_prep,
        "reading score": reading_score,
        "writing score": writing_score
    }])

    # Predict using the pipeline model
    prediction = model.predict(input_df)[0]
    st.success(f"📈 Predicted Math Score: **{prediction:.2f}**")

    # Study plan suggestion
    st.subheader("📝 Suggested Study Plan")

    if prediction < 50:
        st.error("You need focused help! 📚 Spend at least 3–4 hours daily on math, practice basics, and revise concepts. Enroll in remedial classes if possible.")
    elif prediction < 70:
        st.warning("You're doing okay. Aim for consistent practice. 🕒 Spend 1–2 hours daily on past papers and concept revisions.")
    elif prediction < 85:
        st.info("Good performance! 🎯 Maintain it by practicing problem-solving and mock tests weekly.")
    else:
        st.success("Excellent! 🚀 Keep challenging yourself with higher-order problems to stay ahead.")

    st.markdown("---")
    st.caption("Prototype by [Your Name] - Student Performance Predictor using ML & Streamlit")
