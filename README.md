# AgriSense AI
## Smart Crop Recommendation & Agricultural Intelligence Platform

AgriSense AI is a machine learning-powered agricultural intelligence platform that recommends suitable crops based on soil nutrients, weather conditions, and environmental factors.

The project applies Data Science, Feature Engineering, Machine Learning, Model Evaluation, Hyperparameter Tuning, and Streamlit Dashboard Development to support intelligent agricultural decision-making.

---

# Project Objectives

- Analyze agricultural datasets using Exploratory Data Analysis (EDA)
- Engineer domain-specific agricultural features
- Train and compare multiple machine learning models
- Optimize model performance through hyperparameter tuning
- Build an interactive Streamlit dashboard
- Recommend suitable crops based on farm conditions

---

# Project Structure

```text
AgriSense_AI/

│
├── data/
│   ├── Crop_recommendation.csv
│   └── cleaned_crop_data.csv
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   └── 03_model_training.ipynb
│
├── models/
│   ├── best_model.pkl
│   ├── scaler.pkl
│   └── label_encoder.pkl
│
├── pages/
│   ├── 01_Dataset_Overview.py
│   ├── 02_Agricultural_Insights.py
│   ├── 03_Feature_Engineering.py
│   ├── 04_Model_Comparison.py
│   └── 05_Crop_Prediction.py
│
├── Home.py
├── requirements.txt
└── README.md
```

---

# Dataset Information

Dataset Name:

Crop Recommendation Dataset

Target Variable:

```python
label
```

Features:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH
- Rainfall

Records:

```text
2200
```

Crop Categories:

```text
22
```

---

# Data Cleaning

Performed:

- Missing Value Analysis
- Duplicate Record Detection
- Data Validation
- Data Type Verification
- Outlier Detection
- Clean Dataset Export

Output:

```text
cleaned_crop_data.csv
```

---

# Feature Engineering

Engineered Features:

| Feature | Description |
|----------|-------------|
| NPK_Total | Combined nutrient strength |
| NPK_Average | Average nutrient score |
| Humidity_Temp_Index | Temperature and humidity interaction |
| Soil_Fertility | Weighted soil productivity score |
| Rainfall_Category | Rainfall categorization |

Benefits:

- Improved predictive capability
- Better environmental representation
- Enhanced agricultural insights

---

# Exploratory Data Analysis

Visualizations Created:

- Crop Distribution
- Temperature Distribution
- Humidity Distribution
- Rainfall Distribution
- pH Distribution
- Nitrogen Distribution
- Phosphorus Distribution
- Potassium Distribution
- Correlation Heatmap
- Temperature vs Rainfall
- Humidity vs Rainfall
- Average Nitrogen by Crop
- Average Phosphorus by Crop
- Average Potassium by Crop
- Rainfall Category Distribution
- Soil Fertility Distribution
- NPK Total Distribution

Total Visualizations:

```text
17+
```
---
# Machine Learning Models

Models Trained:
1. Logistic Regression
2. Decision Tree
3. Random Forest
4. Gradient Boosting
5. XGBoost

---

# Model Performance

| Model | Accuracy (%) |
|---------|---------|
| XGBoost | 99.55 |
| Random Forest | 99.09 |
| Gradient Boosting | 98.86 |
| Decision Tree | 98.18 |
| Logistic Regression | 97.95 |

Best Model:

```
XGBoost
```

Final Accuracy:

```
99.55%
```

---

# Hyperparameter Tuning

Technique Used:

```
RandomizedSearchCV
```

Parameters Tuned:

- n_estimators
- max_depth
- min_samples_split

Outcome:

- Improved model generalization
- Better cross-validation performance
- Optimized prediction accuracy

---

# Model Persistence

Saved Files:

```text
best_model.pkl
scaler.pkl
label_encoder.pkl
```

Benefits:

- Reproducible predictions
- No retraining required
- Faster deployment
---
# Streamlit Dashboard
Modules:
### Home Dashboard
- KPI Cards
- Crop Statistics
- Rainfall Analysis
### Dataset Explorer
- Dynamic Filtering
- Dataset Health Center
- Crop Profile Explorer
### Agricultural Intelligence Center
- Crop Intelligence Reports
- Nutrient Analysis
- Farmer Recommendations
### Feature Engineering Lab
- Feature Analytics
- Agricultural Impact Analysis
- Transformation Showcase
### Model Performance Lab
- Model Ranking
- Model Battle Arena
- Champion Model Selection
### AI Crop Advisor
- Farm Condition Analysis
- Crop Recommendation
- Farm Health Score
- AI Insights
---

# Technology Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Scikit-Learn
- XGBoost
- Joblib
- Streamlit

---

# Dashboard Screenshots

## Home Dashboard

<img width="1911" height="965" alt="image" src="https://github.com/user-attachments/assets/92e2a21b-53fb-430b-90f2-d083115a10e1" />
<img width="1901" height="947" alt="image" src="https://github.com/user-attachments/assets/baa0a053-a16e-4e6c-8f0f-ac9ebade1088" />


## Dataset Explorer

<img width="1907" height="926" alt="image" src="https://github.com/user-attachments/assets/97e3d4e3-356b-4cce-9a69-ead520807972" />
<img width="1897" height="926" alt="image" src="https://github.com/user-attachments/assets/40f72519-6e29-436c-8ee6-2790902b727e" />

## Agricultural Intelligence Center

<img width="1890" height="837" alt="image" src="https://github.com/user-attachments/assets/00b59b36-a80f-419c-b15f-87f32f0399e0" />
<img width="1857" height="782" alt="image" src="https://github.com/user-attachments/assets/d7ac1cd3-10a3-429c-afb1-b9741e16af97" />
<img width="1882" height="887" alt="image" src="https://github.com/user-attachments/assets/5181f0e0-677d-4eee-b5b3-addc346e9fc4" />

## Feature Engineering Lab

<img width="1855" height="897" alt="image" src="https://github.com/user-attachments/assets/96a9ff61-82c9-4796-9c07-7e87d5e5e4b3" />
<img width="1872" height="877" alt="image" src="https://github.com/user-attachments/assets/80436153-72b6-4e15-bd08-1a56738a8e55" />

## Model Performance Lab

<img width="1832" height="900" alt="image" src="https://github.com/user-attachments/assets/e9004499-ef36-4e50-8383-205edd96647e" />
<img width="1872" height="892" alt="image" src="https://github.com/user-attachments/assets/0cc47266-86fe-4acb-b6c3-2515fe1429b4" />
<img width="1822" height="902" alt="image" src="https://github.com/user-attachments/assets/c167e8e7-7d14-4d14-8b3d-3a29cb23d4a6" />

## AI Crop Advisor

<img width="1907" height="917" alt="image" src="https://github.com/user-attachments/assets/1be4f910-93e4-4362-b369-ae8b4a94d3f1" />
<img width="1872" height="837" alt="image" src="https://github.com/user-attachments/assets/19f5ccbb-6dbe-4b5f-b42a-4d93823a594b" />

---
# Key Outcomes

- Agricultural Data Analysis
- Feature Engineering
- Machine Learning Pipeline
- Hyperparameter Optimization
- Interactive Dashboard
- Crop Recommendation System
- 99.55% Accuracy
---

# Author
M Harshitha


