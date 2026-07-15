import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Model Performance Lab",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 Model Performance Lab")
st.caption(
    "Analyze, compare and rank machine learning models used in AgriSense AI."
)

# ==========================================
# Model Results
# ==========================================

results_df = pd.DataFrame({

    "Model":[
        "XGBoost",
        "Random Forest",
        "Gradient Boosting",
        "Decision Tree",
        "Logistic Regression"
    ],

    "Accuracy":[
        99.55,
        99.09,
        98.86,
        98.18,
        97.95
    ]
})

best_model = "XGBoost"
best_accuracy = 99.55

st.markdown("---")

# ==========================================
# Champion Section
# ==========================================

st.subheader("🥇 Model Champion")

left,right = st.columns([2,1])

with left:

    st.success(
        f"""
        🏆 WINNER : {best_model}

        Accuracy Achieved : {best_accuracy}%

        Selected as the final production model
        for crop recommendation.
        """
    )

with right:

    st.metric(
        "Champion Accuracy",
        f"{best_accuracy}%"
    )

st.markdown("---")

# ==========================================
# Live Ranking Board
# ==========================================

st.subheader("🎯 Live Model Rankings")

ranked = results_df.sort_values(
    "Accuracy",
    ascending=False
).reset_index(drop=True)

ranked.index = ranked.index + 1

st.dataframe(
    ranked,
    use_container_width=True,
    height=250
)

st.markdown("---")
# ==========================================
# Model Battle Arena
# ==========================================

st.subheader("⚔️ Model Battle Arena")

col1, col2 = st.columns(2)

with col1:

    model_1 = st.selectbox(
        "Select First Model",
        results_df["Model"],
        key="model1"
    )

with col2:

    model_2 = st.selectbox(
        "Select Second Model",
        results_df["Model"],
        index=1,
        key="model2"
    )

acc_1 = results_df[
    results_df["Model"] == model_1
]["Accuracy"].values[0]

acc_2 = results_df[
    results_df["Model"] == model_2
]["Accuracy"].values[0]

left,right = st.columns(2)

with left:

    st.info(
        f"""
        🤖 {model_1}

        Accuracy : {acc_1}%
        """
    )

with right:

    st.info(
        f"""
        🤖 {model_2}

        Accuracy : {acc_2}%
        """
    )

difference = abs(acc_1 - acc_2)

st.metric(
    "Performance Difference",
    f"{difference:.2f}%"
)

st.markdown("---")

# ==========================================
# Winner Analysis
# ==========================================

st.subheader("🏆 Match Winner")

if acc_1 > acc_2:

    st.success(
        f"""
        {model_1} wins this comparison.

        Performance Advantage:
        {difference:.2f}%
        """
    )

elif acc_2 > acc_1:

    st.success(
        f"""
        {model_2} wins this comparison.

        Performance Advantage:
        {difference:.2f}%
        """
    )

else:

    st.warning(
        "Both models performed equally."
    )

st.markdown("---")

# ==========================================
# Why XGBoost Won
# ==========================================

st.subheader("🧠 Why XGBoost Became Champion")

st.info(
    """
    • Highest overall accuracy (99.55%)

    • Excellent handling of non-linear relationships

    • Better generalization ability

    • Strong performance on multiclass classification

    • Consistent cross-validation results

    • Lowest prediction error among all models
    """
)

st.markdown("---")

# ==========================================
# Production Deployment Decision
# ==========================================

st.subheader("🚀 Production Deployment Decision")

st.success(
    """
    Selected Production Model

    ✔ XGBoost

    Status : Ready for Deployment

    Reason :
    Highest accuracy and strongest
    predictive performance among all
    evaluated models.
    """
)