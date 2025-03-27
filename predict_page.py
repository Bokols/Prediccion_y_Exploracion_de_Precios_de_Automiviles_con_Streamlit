#Predicción del Precio de un Automóvil con Streamlit
#Descripción: Este código crea una interfaz de usuario interactiva utilizando la biblioteca Streamlit para predecir el precio de un automóvil. El modelo y los codificadores de etiquetas previamente guardados se cargan desde un archivo .pkl utilizando pickle. Los usuarios pueden ingresar características de su automóvil, como el modelo, el año, el kilometraje y otros detalles. Al hacer clic en un botón, se predice el precio estimado del automóvil y se muestra en la interfaz.

import streamlit as st
import pickle 
import numpy as np


def load_model():
    with open("saved_steps.pkl", "rb") as file:
        data = pickle.load(file)
    return data


data = load_model()

regressor = data["model"]
le_model = data["le_model"]
le_condition = data["le_condition"]
le_fuel = data["le_fuel"]
le_transmission = data["le_transmission"]
le_type = data["le_type"]

def show_predict_page():
    st.title("Car price prediction")

    st.write("""### We need some information to predict the price""")

    model_select = ('Acura', 'BMW', 'Buick', 'Cadillac', 'Chevrolet', 'Chrysler',
                     'Dodge','Dodge Ram', 'Ford', 'GMC', 'Honda', 'Hyundai', 'Jeep',
                       'Kia', 'Mercedes','Nissan', 'Subaru', 'Toyota', 'Volkswagen')
    condition_select = ("new", "like new", "excellent", "good", "fair", "salvage")
    fuel_select = ("gas", "diesel", "hybrid", "other", "electric")
    transmission_select = ("automatic", "manual", "other")
    type_select = ("SUV", "truck", "sedan", "pickup", 
           "coupe", "wagon", "mini-van", "hatchback",
           "van", "convertible", "offroad", "bus", "other")


    model_year_select = st.slider("How old is in your car?", 1997, 2019, 1997)
    model_select = st.selectbox("What model is your car?", model_select)
    condition_select = st.selectbox("How is the condition of your car?", condition_select)
    fuel_select = st.selectbox("What fuel system is in your car?", fuel_select)
    odometer_select = st.slider("How used is in your car?", 0, 250000, 10000)
    transmission_select = st.selectbox("What type of transmission is in your car?", transmission_select)
    type_select = st.selectbox("What type of vehicle is in your car?", type_select)
    

    ok = st.button("Calculate the price of your car")
    if ok:
        X = np.array([[model_year_select, model_select, condition_select, fuel_select, 
                       odometer_select, transmission_select, type_select]])
        X[:,1] = le_model.transform(X[:,1])
        X[:,2] = le_condition.transform(X[:,2])
        X[:,3] = le_fuel.transform(X[:,3])
        X[:,5] = le_transmission.transform(X[:,5])
        X[:,6] = le_type.transform(X[:,6])
        X = X.astype(float)

        price = regressor.predict(X)
        st.subheader(f"The estimated price is: ${price[0]:.2f}")

#model_year_select, 
#odometer_select, 