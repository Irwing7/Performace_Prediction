import streamlit as st
import joblib as jb
import numpy as np

# Load scaler and model
scaler = jb.load("scaler.pkl")
model = jb.load("model.pkl")

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #f5f5f5;
        font-family: Arial, sans-serif;
    }
    .main-title {
        color: #3d3d3d;
        font-size: 2.5rem;
        text-align: center;
        margin-bottom: 20px;
    }
    .divider {
        border-top: 2px solid #6c63ff;
        margin: 20px 0;
    }
    .info-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    }
    .predict-btn {
        background-color: #6c63ff;
        color: white;
        font-size: 1rem;
        padding: 10px 20px;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Page title
st.markdown('<div class="main-title">📊 Employee Performance Prediction</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)
st.write("### Get an estimation of employee performance based on key parameters")
st.markdown('<hr class="divider">', unsafe_allow_html=True)

# Input section
with st.container():
    st.write("### Enter the following details:")
    col1, col2 = st.columns(2)

    with col1:
        years = st.number_input("Years at the company", min_value=0, max_value=15, value=2, key="years")
        salary = st.number_input("Monthly Salary", min_value=1000, max_value=10000, value=5000, key="salary")
        overtime_hours = st.number_input("Overtime Hours", min_value=0, max_value=100, value=4, key="overtime")

    with col2:
        no_of_promotions = st.number_input("Number of Promotions", min_value=0, max_value=10, value=2, key="promotions")
        satisfaction_score = st.number_input("Satisfaction Score (0.0 to 5.0)", min_value=0.0, max_value=5.0, value=1.0, key="satisfaction")

# Collecting input data
x = [years, salary, overtime_hours, no_of_promotions, satisfaction_score]

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# Prediction Button
prediction_button = st.button("✨ Predict the Performance Score", key="predict")

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# Prediction Logic
if prediction_button:
    # Animation
    with st.spinner("Predicting performance score... Please wait."):
        x1 = np.array(x)
        x1_scaled = scaler.transform([x1])
        prediction = model.predict(x1_scaled)[0]

    st.success("Prediction Complete!")

    # Display prediction
    st.markdown(f"""
        <div class="info-box">
            <h3>🎯 Predicted Performance Score:</h3>
            <p style="font-size: 1.5rem; color: #6c63ff; font-weight: bold;">{prediction}</p>
        </div>
    """, unsafe_allow_html=True)
else:
    st.info("Press the prediction button to calculate the performance score.")

