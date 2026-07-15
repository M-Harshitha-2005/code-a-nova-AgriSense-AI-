import streamlit as st
import pandas as pd
import plotly.express as px

# Page Config
st.set_page_config(
    page_title="AgriSense AI",
    page_icon="🌾",
    layout="wide"
)

# Load Dataset
@st.cache_data
def load_data():
    return pd.read_csv("data/cleaned_crop_data.csv")

df = load_data()

# Title
st.title("🌾 AgriSense AI")
st.subheader("Smart Crop Recommendation & Agricultural Intelligence Platform")

st.markdown("""
This platform helps analyze agricultural conditions
and recommends suitable crops based on soil nutrients,
weather conditions, and rainfall patterns.
""")
st.markdown("---")

# KPI Section
total_records = len(df)
total_crops = df["label"].nunique()
avg_temp = round(df["temperature"].mean(), 2)
avg_rainfall = round(df["rainfall"].mean(), 2)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📊 Total Records",
        total_records
    )

with col2:
    st.metric(
        "🌾 Crop Types",
        total_crops
    )

with col3:
    st.metric(
        "🌡 Avg Temperature",
        f"{avg_temp} °C"
    )

with col4:
    st.metric(
        "🌧 Avg Rainfall",
        avg_rainfall
    )
st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    crop_count = (
        df["label"]
        .value_counts()
        .reset_index()
    )

    crop_count.columns = [
        "Crop",
        "Count"
    ]

    fig = px.bar(
        crop_count,
        x="Crop",
        y="Count",
        title="Crop Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    fig2 = px.histogram(
        df,
        x="rainfall",
        title="Rainfall Distribution"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )
st.markdown("---")

st.subheader("📌 Project Summary")

st.info(
    """
    AgriSense AI uses Machine Learning to recommend
    suitable crops based on soil nutrients,
    temperature, humidity, pH, and rainfall.

    Best Model: XGBoost
    Accuracy Achieved: 99.55%

    Dataset Size: 2200 Records
    Crop Categories: 22
    """
)