import numpy as np
from typing import Dict
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def train_linear_regression(X_train, y_train) -> LinearRegression:
    model = LinearRegression().fit(X_train, y_train)
    return model

def evaluate(model, X, y) -> Dict[str, float]:
    y_pred = model.predict(X)
    return {
        "r2": r2_score(y, y_pred)
    }

def predict_single(model, experience_value: float) -> float:
    return float(model.predict(np.array([[experience_value]]))[0])
