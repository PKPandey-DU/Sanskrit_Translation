import pickle
from typing import Tuple
import numpy as np
from sklearn.linear_model import LinearRegression
from .paths import ML_BASELINE_MODEL

def train_dummy_regression(X, y) -> LinearRegression:
    model = LinearRegression()
    model.fit(X, y)
    ML_BASELINE_MODEL.parent.mkdir(parents=True, exist_ok=True)
    with open(ML_BASELINE_MODEL, "wb") as f:
        pickle.dump(model, f)
    return model

def load_ml_baseline(path=ML_BASELINE_MODEL):
    with open(path, "rb") as f:
        return pickle.load(f)
