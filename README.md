# Venom Sourve Prediction | SVM 

## Portfolio Project

A Machine Learning multi-class classification project focused on identifying the source of a bite based on clinical, demographic, and physiological features.

The goal of this project is to build a model capable of classifying bite incidents into four categories: **BLACK WIDOW SPIDER**, **HARMLESS INSECT**, **SCORPION**, and **VIPER SNAKE**.

The model uses patient features such as age, time since bite, heart rate, systolic blood pressure, gender, local swelling, and blood coagulation failure to identify the most likely source of the bite.

---

# Problem Definition

Snakebite and other venomous bites can cause a wide range of clinical symptoms and physiological changes. Identifying the source of a bite based on these clinical features can help support faster and more informed medical assessment.

This project focuses on:

**Can Machine Learning identify the source of a bite based on the patient's demographic, physiological, and clinical features?**

The model uses features such as age, time since the bite, heart rate, systolic blood pressure, gender, local swelling, and blood coagulation failure to classify the source of the bite into one of four categories:

- Black Widow Spider
- Harmless Insect
- Scorpion
- Viper Snake

This is formulated as a **multi-class classification problem**.

---

# Dataset

- Dataset Source : Kaggle 
- Dataset License : CC0: Public Domain
- Dataset Link: https://www.kaggle.com/datasets/jacopoferretti/emergency-triage-venomous-bites-dataset

Target Variable:

`Bite Source Target`

Classes:

- Black_Widow_Spider
- Harmless_Insect
- Scorpion
- Viper_Snake

Selected Features:

- Age
- Time_Since_Bite_Min
- Heart_Rate_BPM
- Blood_Pressure_Systolic
- Gender
- Local_Swelling
- Blood_Coagulation_Failure

---

## Data Analysis

- EDA
- Visulization
- Dataset inspection
- Missing value analysis
- dupilucated analysis
- Outlires analysis
- Target distribution analysis
- Correlation analysis
- Feature relationship analysis


## Data Preprocessing

- Data cleaning
- Feature selection
- Remove missing value
- Label encoding
- Train/Test split

## Model Development

- Streamlit
- Webapp link : venom-source-prediction.streamlit.app 

Models:

- SVM Classifier (SVC)

Evaluation:

- Accuracy
- Precision
- Recall
- F1-score
- Cross Validation
- Confusion Matrix
- Classification Report 

# Model Performance

Final Model:

SVM Classifier (SVC)

accuracy Results:

| Metric | Score |
|---|---|
| test | 99.6316% |
| train | 99.6392% |


5-Fold Cross Validation:

99.63%

Standard Deviation:

0.021


---

# Model Interpretation

To understand feature contribution:

- Mutal Information
- correlation 


Important Features:

- Blood_Coagulation_Failure
- Local_Swelling
- Blood_Pressure_Systolic
- Heart_Rate_BPM


---

# Repository Structure

```text
Venom-Source-Prediction/
│
├── App/
│    └── venomSource.py
│
├── Pickles/
│     ├── classifier.pickle
│     ├── column_transformer.pickle
│     └── pipeline.py
│
├── Data/
│      └── silent_sting_triage_data_sample.ipynb
│
├── webapp/
│      └── VenomSource.ipynb
│
├── notebook.ipynb
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

---

# Webapp Link

- link: venom-source-prediction.streamlit.app 

# How To Run with you python

Install requirements: pip install -r requirements.txt

Run prediction:python App/venomSource.py

---

# Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Seaborn
- Jupyter Notebook
- Joblib 
- Streamlit 

## Author

**Amir Mohammad (Arash) Khanzadeh**