import numpy as np
from tensorflow.keras.models import load_model
import joblib  # para carregar o scaler salvo

# Carrega o modelo treinado
model = load_model("models/lstm_model.keras")

# Carrega o scaler usado no pré-processamento do treino
scaler = joblib.load("models/scaler.save")  # use o caminho correto aqui


def predict_price(prices: list[float]) -> float:
    # Garante que o tamanho da entrada bate com o time_step (ex: 60)
    if len(prices) != model.input_shape[1]:
        raise ValueError(
            f"Esperado {model.input_shape[1]} valores, mas recebeu {len(prices)}.")

    # 1. Normalizar os preços
    input_scaled = scaler.transform(np.array(prices).reshape(-1, 1))

    # 2. Ajustar shape para LSTM: (1, time_step, 1)
    input_array = input_scaled.reshape(1, len(prices), 1)

    # 3. Fazer a previsão
    prediction_scaled = model.predict(input_array)

    # 4. Reverter a normalização da saída
    prediction = scaler.inverse_transform(prediction_scaled)

    return float(prediction[0][0])
