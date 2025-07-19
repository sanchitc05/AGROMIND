# crop_recommender.py
import joblib
import numpy as np
import os

# Load the model only once when the module is imported
model_path = os.path.join("models", "crop_recommender.pkl")
try:
    model = joblib.load(model_path)
except FileNotFoundError:
    raise FileNotFoundError(f"Model not found at {model_path}. Please run train_model.py first.")

def recommend_crop(N, P, K, temp, humidity, ph, rainfall):
    data = np.array([[N, P, K, temp, humidity, ph, rainfall]])
    prediction = model.predict(data)
    return prediction[0]
