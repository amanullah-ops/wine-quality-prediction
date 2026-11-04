import joblib
import pandas as pd
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "wine_quality_model.pkl"

model = joblib.load(MODEL_PATH)

def predict_quality(wine_features):

    input_df = pd.DataFrame([wine_features])

    # Ensure correct feature order
    input_df = input_df[model.feature_names_in_]

    prediction = model.predict(input_df)

    return float(prediction[0])

