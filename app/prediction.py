import joblib
import pandas as pd

pipeline = joblib.load("models/pipeline.pkl")

def predict(data):
    df = pd.DataFrame([data])
    prediction = pipeline.predict(df)
    return float(prediction[0])
