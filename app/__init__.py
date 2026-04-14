# run_pipeline.py
import joblib
import os
from src.data_loader import load_and_split_data
from src.preprocess import get_preprocessor
from src.train import train_and_select_best_model

def main():
    # 1. Load Data
    print("Loading data...")
    X_train, X_test, y_train, y_test = load_and_split_data(
        data_path="data/insurance.csv", 
        target_col="charges"
    )
    
    # 2. Get Preprocessing Steps
    print("Initializing preprocessor...")
    preprocessor = get_preprocessor()
    
    # 3. Train, Evaluate, and Get Best Model
    best_pipeline = train_and_select_best_model(X_train, y_train, X_test, y_test, preprocessor)
    
    # 4. Save the winning model
    os.makedirs('models', exist_ok=True)
    joblib.dump(best_pipeline, "models/MIPML.pkl")
    print("\nBest pipeline successfully saved to models/MIPML.pkl")

if __name__ == "__main__":
    main()