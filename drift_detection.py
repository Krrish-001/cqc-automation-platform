import numpy as np

def detect_drift(train_data, production_data):
    train_mean = np.mean(train_data)
    prod_mean = np.mean(production_data)

    if abs(train_mean - prod_mean) > 0.1:
        return "Drift Detected"
    return "No Drift"
