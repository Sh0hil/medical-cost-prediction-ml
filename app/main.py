from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import os

app = FastAPI(title="Medical Insurance Premium API")


# MODEL LOADING WITH DEBUG
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "pipeline.pkl")

model = None
model_status = "not_loaded"

try:
    model = joblib.load(MODEL_PATH)
    model_status = "loaded_successfully"
    print("✅ Model loaded successfully from:", MODEL_PATH)
except Exception as e:
    model_status = f"load_failed: {str(e)}"
    print("❌ Model loading failed:", e)



# INPUT SCHEMA
class InsuranceInput(BaseModel):
    age: int
    sex: str
    bmi: float
    children: int
    smoker: str
    region: str



# ROUTES
@app.get("/")
def home():
    return {"message": "Medical Insurance Premium Predictor API is running"}


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model_status": model_status
    }


@app.post("/predict")
def predict(data: InsuranceInput):
    if model is None:
        return {"error": f"Model not loaded. Reason: {model_status}"}

    try:
        input_df = pd.DataFrame([data.dict()])
        prediction = model.predict(input_df)

        return {
            "predicted_premium": round(float(prediction[0]), 2)
        }

    except Exception as e:
        return {"error": str(e)}