import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Feature Engineering Lab",
    page_icon="⚙️",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv("data/cleaned_crop_data.csv")

df = load_data()

st.title("⚙️ Feature Engineering Lab")
st.caption(
    "Transforming raw agricultural data into intelligent features for machine learning."
)

st.markdown("---")

# ==================================
# Feature Summary Cards
# ==================================

st.subheader("🧪 Engineered Features Overview")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Original Features",
        8
    )

with c2:
    st.metric(
        "Engineered Features",
        5
    )

with c3:
    st.metric(
        "Total Features",
        df.shape[1]
    )

with c4:
    st.metric(
        "Target Classes",
        df["label"].nunique()
    )

st.markdown("---")

# ==================================
# Feature Explorer
# ==================================

feature_descriptions = {
    "NPK_Total":
        "Combined nutrient strength of Nitrogen, Phosphorus and Potassium.",

    "NPK_Average":
        "Average nutrient availability score.",

    "Humidity_Temp_Index":
        "Interaction between temperature and humidity.",

    "Soil_Fertility":
        "Weighted score representing soil productivity.",

    "Rainfall_Category":
        "Categorization of rainfall into agricultural zones."
}

selected_feature = st.selectbox(
    "Select Engineered Feature",
    list(feature_descriptions.keys())
)

st.info(
    feature_descriptions[selected_feature]
)

st.markdown("---")
# ==================================
# Live Feature Statistics
# ==================================

st.subheader("📊 Feature Analytics")

if selected_feature != "Rainfall_Category":

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Minimum",
            round(df[selected_feature].min(), 2)
        )

    with c2:
        st.metric(
            "Maximum",
            round(df[selected_feature].max(), 2)
        )

    with c3:
        st.metric(
            "Average",
            round(df[selected_feature].mean(), 2)
        )

    with c4:
        st.metric(
            "Standard Deviation",
            round(df[selected_feature].std(), 2)
        )

st.markdown("---")

# ==================================
# Before vs After Transformation
# ==================================

st.subheader("🔄 Feature Transformation Showcase")

transformation_data = {

    "NPK_Total":
        ("N + P + K",
         "Combined Nutrient Strength"),

    "NPK_Average":
        ("(N + P + K) / 3",
         "Average Nutrient Score"),

    "Humidity_Temp_Index":
        ("Humidity × Temperature",
         "Environmental Interaction"),

    "Soil_Fertility":
        ("0.4N + 0.3P + 0.3K",
         "Soil Productivity Index"),

    "Rainfall_Category":
        ("Continuous Rainfall",
         "Low / Medium / High")
}

before, after = transformation_data[selected_feature]

left, right = st.columns(2)

with left:

    st.info(
        f"""
        ### Raw Data
        
        {before}
        """
    )

with right:

    st.success(
        f"""
        ### Engineered Output
        
        {after}
        """
    )

st.markdown("---")

# ==================================
# Agricultural Impact Analysis
# ==================================

st.subheader("🌾 Agricultural Impact")

impact_text = {

    "NPK_Total":
        """
        Helps identify overall nutrient richness
        of agricultural soil.
        """,

    "NPK_Average":
        """
        Provides balanced nutrient availability
        measurement.
        """,

    "Humidity_Temp_Index":
        """
        Captures interaction between climate
        variables affecting crop growth.
        """,

    "Soil_Fertility":
        """
        Represents agricultural productivity
        potential.
        """,

    "Rainfall_Category":
        """
        Groups farms into different rainfall
        suitability zones.
        """
}

st.warning(
    impact_text[selected_feature]
)

st.markdown("---")

# ==================================
# Feature Quality Assessment
# ==================================

st.subheader("✅ Feature Quality Assessment")

q1, q2, q3 = st.columns(3)

with q1:
    st.success("✔ Domain Relevance")

with q2:
    st.success("✔ Model Compatibility")

with q3:
    st.success("✔ Predictive Value")

st.markdown("---")