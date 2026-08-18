import joblib
import pandas as pd 
import numpy as np
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
model_path = BASE_DIR / "pickles" / "pipeline.pickle"

model = joblib.load(model_path)

# Viper_Snake
sample = pd.DataFrame({
    "Age": [61],
    "Gender": ["Female"],
    "Time_Since_Bite_Min": [25],
    "Heart_Rate_BPM": [86],
    "Blood_Pressure_Systolic": [72],
    "Local_Swelling": ["Medium"],
    "Blood_Coagulation_Failure": [0]
})

pre = model.predict(sample)
print(pre)