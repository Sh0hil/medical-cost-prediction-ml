# src/preprocess.py
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def get_preprocessor():
    """Returns the configured ColumnTransformer for the pipeline."""
    categorical = ["sex", "smoker", "region"]
    numerical = ["age", "bmi", "children"]

    preprocessor = ColumnTransformer([
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical),
        ("num", StandardScaler(), numerical) 
    ])
    
    return preprocessor