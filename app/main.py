from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Load the new professional pipeline model
# (joblib is much better for pipelines than standard pickle)
model = joblib.load('models/MIPML.pkl')

# Create app
app = FastAPI(title="Medical Insurance Premium API")

# Input schema
class InsuranceInput(BaseModel):
    age: int
    sex: str
    bmi: float
    children: int
    smoker: str
    region: str

# Home route
@app.get("/")
def home():
    return {"message": "Medical Insurance Premium Predictor API is running"}

# Prediction route
@app.post("/predict")
def predict(data: InsuranceInput):
    
    # 1. Convert the incoming data directly into a Pandas DataFrame.
    # The new ML Pipeline expects raw strings and handles all encoding automatically!
    input_df = pd.DataFrame([dict(data)])

    # 2. Prediction
    prediction = model.predict(input_df)

    return {
        "predicted_premium": float(prediction[0])
    }