# src/train.py
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

def train_and_select_best_model(X_train, y_train, X_test, y_test, preprocessor):
    """Iterates through models, evaluates them, and returns the best performing pipeline."""
    models = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(max_depth=5, random_state=42),
        "Random Forest": RandomForestRegressor(n_estimators=100, max_depth=7, random_state=42),
        "Gradient Boosting": GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
    }

    best_model_name = ""
    best_model_score = -float("inf")
    best_pipeline = None

    print("Starting Model Training and Evaluation...\n")

    for name, model in models.items():
        # Create pipeline
        pipeline = Pipeline([
            ("preprocessor", preprocessor),
            ("model", model)
        ])
        
        # Train
        pipeline.fit(X_train, y_train)
        
        # Predict & Evaluate
        y_pred = pipeline.predict(X_test)
        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        
        print(f"--- {name} ---")
        print(f"R2 Score: {r2:.4f} (Higher is better)")
        print(f"MAE:      ${mae:,.2f} (Lower is better)\n")
        
        # Track the best
        if r2 > best_model_score:
            best_model_score = r2
            best_model_name = name
            best_pipeline = pipeline

    print(f"Best Model: {best_model_name} with R2 Score: {best_model_score:.4f}")
    
    return best_pipeline