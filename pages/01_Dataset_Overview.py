import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("data/cleaned_crop_data.csv")

df = load_data()

st.title("📊 Dataset Explorer")
st.caption("Interactively explore agricultural data and crop characteristics")

# ==========================
# Sidebar Filters
# ==========================

st.sidebar.header("🔍 Dataset Filters")

selected_crop = st.sidebar.multiselect(
    "Select Crop",
    options=sorted(df["label"].unique()),
    default=[]
)

rainfall_range = st.sidebar.slider(
    "Rainfall Range",
    float(df["rainfall"].min()),
    float(df["rainfall"].max()),
    (
        float(df["rainfall"].min()),
        float(df["rainfall"].max())
    )
)

# Apply Filters
filtered_df = df.copy()

if selected_crop:
    filtered_df = filtered_df[
        filtered_df["label"].isin(selected_crop)
    ]

filtered_df = filtered_df[
    (filtered_df["rainfall"] >= rainfall_range[0]) &
    (filtered_df["rainfall"] <= rainfall_range[1])
]

# ==========================
# Dynamic KPI Cards
# ==========================

st.subheader("📈 Live Dataset Statistics")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Records",
        len(filtered_df)
    )

with c2:
    st.metric(
        "Crop Types",
        filtered_df["label"].nunique()
    )

with c3:
    st.metric(
        "Avg Temp",
        f"{filtered_df['temperature'].mean():.1f}°C"
    )

with c4:
    st.metric(
        "Avg Rainfall",
        f"{filtered_df['rainfall'].mean():.1f}"
    )

st.markdown("---")
# ==========================
# Dataset Health Center
# ==========================

st.subheader("🩺 Dataset Health Center")

c1, c2, c3 = st.columns(3)

with c1:
    st.success(
        f"✅ Missing Values: {filtered_df.isnull().sum().sum()}"
    )

with c2:
    st.info(
        f"📄 Features: {filtered_df.shape[1]}"
    )

with c3:
    st.warning(
        f"🔁 Duplicate Records: {filtered_df.duplicated().sum()}"
    )

st.markdown("---")

# ==========================
# Dataset Preview
# ==========================

st.subheader("🔎 Interactive Dataset Viewer")

search_crop = st.text_input(
    "Search Crop Name"
)

display_df = filtered_df.copy()

if search_crop:
    display_df = display_df[
        display_df["label"]
        .str.contains(
            search_crop,
            case=False,
            na=False
        )
    ]

st.dataframe(
    display_df,
    use_container_width=True,
    height=350
)

# ==========================
# Download Button
# ==========================

csv = display_df.to_csv(index=False)

st.download_button(
    label="⬇ Download Filtered Dataset",
    data=csv,
    file_name="filtered_crop_data.csv",
    mime="text/csv"
)

st.markdown("---")

# ==========================
# Crop Profile Explorer
# ==========================

st.subheader("🌾 Crop Profile Explorer")

selected_profile_crop = st.selectbox(
    "Select Crop for Detailed Analysis",
    sorted(df["label"].unique())
)

crop_df = df[
    df["label"] == selected_profile_crop
]

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Avg Temperature",
        f"{crop_df['temperature'].mean():.2f} °C"
    )

    st.metric(
        "Avg Humidity",
        f"{crop_df['humidity'].mean():.2f}"
    )

with col2:

    st.metric(
        "Avg Rainfall",
        f"{crop_df['rainfall'].mean():.2f}"
    )

    st.metric(
        "Avg Soil pH",
        f"{crop_df['ph'].mean():.2f}"
    )

st.markdown("---")