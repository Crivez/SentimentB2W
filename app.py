import pandas as pd
import streamlit as st
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import ktrain

#Detector de Sentimento

#Cabeçalho
st.subheader('Abaixo, uma visualização do seu grau de satisfação de acordo com o texto:')

#Nome do Usuário
user_input = st.sidebar.text_input("Digite o seu nome:")

#Texto
user_input2 = st.sidebar.text_input("Digite sua avaliação:")

#aplicando o modelo
predictor = ktrain.load_predictor('bertimbau9010procleve2')
y = int(predictor.predict(user_input2))

#Resposta
if (y == 1 and st.sidebar.button('Go')):
    st.write(user_input,", você está assim: 😡!!! ")
if (y == 2 and st.sidebar.button('Go')):
    st.write(user_input,", você está assim: 🙁!!! ")
if (y == 3 and st.sidebar.button('Go')):
    st.write(user_input,", você está assim: 😐!!! ")
if (y == 4 and st.sidebar.button('Go')):
    st.write(user_input,", você está assim: 🙂!!! ")
if (y == 5 and st.sidebar.button('Go')):
    st.write(user_input,", você está assim: 😀!!! ")
