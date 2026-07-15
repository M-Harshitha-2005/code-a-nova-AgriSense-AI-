import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Crop Intelligence Studio",
    page_icon="🌾",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv("data/cleaned_crop_data.csv")

df = load_data()

st.title("🌾 Crop Intelligence Studio")
st.caption(
    "Explore the environmental and nutrient requirements of every crop."
)

# ==================================
# Crop Selection Area
# ==================================

crop_list = sorted(df["label"].unique())

selected_crop = st.selectbox(
    "Select a Crop",
    crop_list
)

crop_df = df[df["label"] == selected_crop]

st.markdown("---")

# ==================================
# Crop Hero Section
# ==================================

avg_temp = crop_df["temperature"].mean()
avg_humidity = crop_df["humidity"].mean()
avg_rainfall = crop_df["rainfall"].mean()
avg_ph = crop_df["ph"].mean()

st.subheader(f"🌱 {selected_crop.title()} Profile")

left, right = st.columns([2,1])

with left:

    st.success(
        f"""
        Recommended Crop: {selected_crop.title()}
        
        This crop performs best under the environmental
        conditions shown on the right.
        """
    )

with right:

    st.metric(
        "Optimal Temperature",
        f"{avg_temp:.1f} °C"
    )

    st.metric(
        "Optimal Humidity",
        f"{avg_humidity:.1f}%"
    )

st.markdown("---")

# ==================================
# Agricultural Scorecards
# ==================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "🌡 Temperature",
        f"{avg_temp:.1f} °C"
    )

with c2:
    st.metric(
        "💧 Humidity",
        f"{avg_humidity:.1f}%"
    )

with c3:
    st.metric(
        "🌧 Rainfall",
        f"{avg_rainfall:.1f}"
    )

with c4:
    st.metric(
        "🧪 Soil pH",
        f"{avg_ph:.1f}"
    )

st.markdown("---")
# ==================================
# Smart Crop Advisory Panel
# ==================================

st.subheader("🧠 Smart Crop Advisory")

avg_n = crop_df["N"].mean()
avg_p = crop_df["P"].mean()
avg_k = crop_df["K"].mean()

def nutrient_level(value):
    if value < 50:
        return "🟢 Low"
    elif value < 100:
        return "🟡 Medium"
    else:
        return "🔴 High"

col1, col2 = st.columns([1, 1])

with col1:

    st.markdown("### 🌿 Nutrient Requirements")

    st.info(
        f"""
        Nitrogen Requirement : {nutrient_level(avg_n)}

        Phosphorus Requirement : {nutrient_level(avg_p)}

        Potassium Requirement : {nutrient_level(avg_k)}
        """
    )

with col2:

    st.markdown("### 📋 Environmental Suitability")

    suitability_score = (
        avg_temp * 0.25 +
        avg_humidity * 0.25 +
        avg_rainfall * 0.25 +
        avg_ph * 10 * 0.25
    )

    score = min(round(suitability_score), 100)

    st.progress(score / 100)

    st.metric(
        "Suitability Index",
        f"{score}/100"
    )

st.markdown("---")

# ==================================
# Farmer Recommendation Center
# ==================================

st.subheader("🚜 Farmer Recommendation Center")

recommendations = []

if avg_rainfall > 180:
    recommendations.append(
        "High rainfall conditions are suitable for water-intensive cultivation."
    )

if avg_temp > 25:
    recommendations.append(
        "Warm climate supports healthy crop growth."
    )

if avg_ph < 6:
    recommendations.append(
        "Acidic soil conditions detected."
    )

if avg_ph >= 6 and avg_ph <= 7.5:
    recommendations.append(
        "Soil pH is within the ideal agricultural range."
    )

if avg_n > 100:
    recommendations.append(
        "High nitrogen requirement indicates fertile soil demand."
    )

for rec in recommendations:
    st.success(rec)

st.markdown("---")

# ==================================
# Crop Snapshot
# ==================================

st.subheader("📌 Crop Snapshot")

snapshot_col1, snapshot_col2 = st.columns(2)

with snapshot_col1:

    st.metric(
        "Average NPK Total",
        round(crop_df["NPK_Total"].mean(), 2)
    )

    st.metric(
        "Soil Fertility Score",
        round(crop_df["Soil_Fertility"].mean(), 2)
    )

with snapshot_col2:

    st.metric(
        "Humidity Index",
        round(crop_df["Humidity_Temp_Index"].mean(), 2)
    )

    st.metric(
        "Records Available",
        len(crop_df)
    )

st.markdown("---")