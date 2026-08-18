import streamlit as st 
import pandas as pd
import joblib 
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

model_path = BASE_DIR / "pickles" / "pipeline.pickle" 
model = joblib.load(model_path)

st.markdown('''
# Venom Sorce Prediction  
''')

st.sidebar()

st.sidebar.header("User Input Parameters")

Age = st.sidebar.slider("Age", 0, 120, 18)
Time_Since_Bite_Min = st.sidebar.slider("Time Since Bite Min", 10, 300, 60)
Heart_Rate_BPM = st.sidebar.slider("Hear Rate BPM", 40, 200, 50)
Blood_Pressure_Systolic = st.sidebar.slider("Blood Pressure Systolic", 40, 200, 120)
Gender = st.sidebar.radio("Gender", ["Male", "Female", "Other"])
Local_Swelling = st.sidebar.radio("Local Swelling", ["Mild", "Severe", "Medium", "Unknown"])
Blood_Coagulation_Failure = st.sidebar.radio(
    "Blood Coagulation Failure", 
    [0, 1], 
    format_func=lambda x: "False" if x == 0 else "True"
)

def make_df():
    df = pd.DataFrame({
        "Age": [Age],
        "Time_Since_Bite_Min": [Time_Since_Bite_Min],
        "Heart_Rate_BPM": [Heart_Rate_BPM],
        "Blood_Pressure_Systolic": [Blood_Pressure_Systolic],
        "Gender": [Gender],
        "Local_Swelling": [Local_Swelling],
        "Blood_Coagulation_Failure": [Blood_Coagulation_Failure]
    })

    return df

df = make_df()

prediction_button = st.sidebar.button("Predict", type="primary")

st.subheader('Class labels')
st.dataframe(
    pd.DataFrame(
        ["Black_Widow_Spider", "Harmless_Insect", "Scorpion", "Viper_Snake"],
        columns=["Sorces"]
    )
)

st.markdown("---")

if prediction_button:
    import time
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.001)
        my_bar.progress(percent_complete + 1)

    st.subheader("Prediction", text_alignment="center")

    pre = model.predict(df)
    result = pre[0].replace("_", " ")

    st.markdown(
        f'''
        <h3 style="padding: 10px;
                    border-radius: 15px;
                    text-align: center;
                    background-color: #e8f5e9;">
            {result}
        </h3>
        ''',unsafe_allow_html=True)
    
