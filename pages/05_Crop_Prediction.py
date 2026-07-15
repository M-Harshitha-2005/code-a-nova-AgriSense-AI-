import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.set_page_config(
    page_title="AI Crop Advisor",
    page_icon="🎯",
    layout="wide"
)

# ==================================
# Load Model Files
# ==================================

model = joblib.load("models/best_model.pkl")
scaler = joblib.load("models/scaler.pkl")
encoder = joblib.load("models/label_encoder.pkl")

st.title("🎯 AI Crop Advisor")
st.caption(
    "Get intelligent crop recommendations based on soil and environmental conditions."
)

st.markdown("---")

# ==================================
# Input Section
# ==================================

st.subheader("🌾 Farm Condition Analysis")

col1, col2 = st.columns(2)

with col1:

    N = st.slider(
        "Nitrogen (N)",
        0, 150, 50
    )

    P = st.slider(
        "Phosphorus (P)",
        0, 150, 50
    )

    K = st.slider(
        "Potassium (K)",
        0, 250, 50
    )

    temperature = st.slider(
        "Temperature (°C)",
        0.0, 50.0, 25.0
    )

with col2:

    humidity = st.slider(
        "Humidity (%)",
        0.0, 100.0, 60.0
    )

    ph = st.slider(
        "Soil pH",
        0.0, 14.0, 6.5
    )

    rainfall = st.slider(
        "Rainfall",
        0.0, 300.0, 100.0
    )

st.markdown("---")
# ==================================
# Prediction Engine
# ==================================

if st.button("🚀 Analyze Farm Conditions"):

    npk_total = N + P + K

    npk_average = npk_total / 3

    humidity_temp_index = (
        humidity * temperature
    )

    soil_fertility = (
        0.4 * N +
        0.3 * P +
        0.3 * K
    )

    if rainfall < 100:
        rainfall_low = 1
        rainfall_medium = 0

    elif rainfall < 200:
        rainfall_low = 0
        rainfall_medium = 1

    else:
        rainfall_low = 0
        rainfall_medium = 0

    input_data = pd.DataFrame([[
        N,
        P,
        K,
        temperature,
        humidity,
        ph,
        rainfall,
        npk_total,
        npk_average,
        humidity_temp_index,
        soil_fertility,
        rainfall_low,
        rainfall_medium
    ]])

    input_scaled = scaler.transform(
        input_data
    )

    prediction = model.predict(
        input_scaled
    )

    crop = encoder.inverse_transform(
        prediction
    )[0]

    st.markdown("## 🌱 Recommended Crop")

    st.success(
        crop.upper()
    )

    st.markdown("---")

    st.subheader("📋 AI Recommendation Report")

    recommendations = []

    if rainfall > 180:
        recommendations.append(
            "High rainfall conditions detected."
        )

    if temperature > 25:
        recommendations.append(
            "Warm climate suitable for crop growth."
        )

    if 6 <= ph <= 7.5:
        recommendations.append(
            "Soil pH is within ideal range."
        )

    if npk_total > 150:
        recommendations.append(
            "Good nutrient availability detected."
        )

    for item in recommendations:
        st.success(item)

    st.markdown("---")