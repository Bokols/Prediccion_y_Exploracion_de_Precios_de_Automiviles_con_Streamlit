#Interfaz de Usuario de Streamlit para Predicción y Exploración de Precios de Automóviles
#Descripción: Este código crea una aplicación interactiva en Streamlit que permite a los usuarios elegir entre dos páginas: una para predecir el precio de un automóvil y otra para explorar datos sobre los precios de automóviles. Usando una barra lateral con un selectbox, el usuario puede seleccionar "Predict" (para predecir el precio de un automóvil basado en varias características) o "Explore" (para ver gráficos de tendencias de precios de automóviles según diferentes categorías como modelo, tipo, transmisión y si el vehículo es 4WD).

import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

page = st.sidebar.selectbox("Explore or Predict",("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()
