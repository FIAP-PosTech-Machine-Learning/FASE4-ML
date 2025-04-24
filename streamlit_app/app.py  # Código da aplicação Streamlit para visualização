import streamlit as st
import pandas as pd
import numpy as np
from keras.models import load_model

# Carregar o modelo LSTM treinado
model = load_model('../models/lstm_model.h5')

# Função para fazer previsões
def predict_stock_price(data):
    # Pré-processar os dados conforme necessário
    # Aqui você deve incluir a lógica de pré-processamento que foi utilizada durante o treinamento
    # Exemplo: normalização, reshaping, etc.
    data = np.array(data).reshape((1, data.shape[0], data.shape[1]))
    prediction = model.predict(data)
    return prediction

# Título da aplicação
st.title('Previsão de Preços de Ações com LSTM')

# Carregar dados históricos
data = pd.read_csv('../data/dataset.csv')

# Exibir os dados
st.subheader('Dados Históricos de Ações')
st.write(data)

# Input do usuário para dados de entrada
user_input = st.text_input("Insira os dados históricos para previsão (ex: [valor1, valor2, ...]):")

if user_input:
    # Converter a entrada do usuário em um array
    input_data = np.array(eval(user_input))
    
    # Fazer a previsão
    predicted_price = predict_stock_price(input_data)
    
    # Exibir o resultado
    st.subheader('Preço Previsto:')
    st.write(predicted_price)