import numpy as np
from tensorflow.keras.models import load_model

model = load_model("models/lstm_model.keras")

def predict_price(prices: list[float]) -> float:
    input_array = np.array(prices).reshape(1, -1)
    prediction = model.predict(input_array)
    return float(prediction[0][0])