#Exploración y Análisis de Precios de Automóviles con Streamlit
#Descripción: Este código utiliza Streamlit para crear una interfaz interactiva que permite a los usuarios explorar los precios de los automóviles en función de diferentes variables. El archivo de datos se carga y se limpia mediante la eliminación de valores nulos y la categorización de variables en quintiles. Se generan gráficos de barras para visualizar cómo el precio promedio varía según el modelo, tipo de vehículo, tipo de transmisión y si es un vehículo 4WD. También se realiza un análisis de datos para modificar y reemplazar ciertos valores, lo que mejora la precisión del análisis.

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.cache_data 
def load_data():
    # Carga el archivo de datos en un DataFrame
    df = pd.read_csv('C:/Users/bokol/OneDrive/Desktop/Tripleten/Sprints/Sprint 3/vehicles_us.csv')
    #Convertir NaN a 0 en is_4wd
    df['is_4wd'] = df['is_4wd'].fillna(0)
    #Definir los quintiles y sus correspondientes categorías
    quintiles = pd.qcut(df['price'], q=5, labels=False)
    categories = {0: 'Low', 1: 'Medium Low', 2: 'Medium', 3: 'Medium high', 4: 'High'}

    # Función para categorizar el ingreso
    def categorize_price(value):
        if pd.isnull(value):
            return 'NaN'
        else:
            return categories[value]

    # Crear la columna 'price_grouped' basada en los quintiles
    df['price_grouped'] = quintiles.apply(categorize_price)
    #Definir los quintiles y sus correspondientes categorías
    quintiles = pd.qcut(df['odometer'], q=5, labels=False)
    categories = {0: 'Low', 1: 'Medium Low', 2: 'Medium', 3: 'Medium high', 4: 'High'}

    # Función para categorizar el ingreso
    def categorize_odometer(value):
        if pd.isnull(value):
            return 'NaN'
        else:
            return categories[value]

    # Crear la columna 'income_range' basada en los quintiles
    df['odometer_grouped'] = quintiles.apply(categorize_odometer)
    
    #  reemplazaré los valores de NaN

    pivot_model_year = df.pivot_table(index=['odometer', 'price','model'], values='model_year', aggfunc='median')

    def fill_model_year(row):
        year = row['model_year']
        price_grouped = row['price_grouped']
        odometer_grouped = row['odometer_grouped']
        model = row['model']
        try:
            if pd.isna(year):
                return pivot_model_year.loc[odometer_grouped, model, price_grouped]['model_year']
            return year
        except:
            return df['model_year'].median()

    df['model_year'] = df.apply(fill_model_year, axis=1)

    #Definir los quintiles y sus correspondientes categorías
    quintiles = pd.qcut(df['model_year'], q=5, labels=False)
    categories = {0: 'Old', 1: 'Semi old', 2: 'Medium', 3: 'Semi new', 4: 'New'}

    # Función para categorizar el ingreso
    def categorize_model_year(value):
        if pd.isnull(value):
            return 'NaN'
        else:
            return categories[value]

    # Crear la columna 'price_grouped' basada en los quintiles
    df['model_year_grouped'] = quintiles.apply(categorize_model_year)

    #  reemplazaré los valores de NaN

    pivot_odometer = df.pivot_table(index=['model_year', 'price', 'model'], values='odometer', aggfunc='median')

    def fill_odometer(row):
        odometer = row['odometer']
        price = row['price']
        model_year = row['model_year']
        model = row['model']
        try:
            if pd.isna(odometer):
                return pivot_odometer.loc[model_year, price, model]['odometer']
            return odometer
        except:
            return df['odometer'].median()

    df['odometer'] = df.apply(fill_odometer, axis=1)

    #  reemplazaré los valores de NaN

    pivot_cylinders = df.pivot_table(index=['is_4wd', 'model', 'type'], values='cylinders', aggfunc='median')

    def fill_cylinders(row):
        cylinders = row['cylinders']
        is_4wd = row['is_4wd']
        model = row['model']
        type = row['type']
        try:
            if pd.isna(cylinders):
                return pivot_cylinders.loc[is_4wd, model, type]['cylinders']
            return cylinders
        except:
            return df['cylinders'].median()

    df['cylinders'] = df.apply(fill_cylinders, axis=1)

    # Aborda los valores problemáticos
    df['paint_color'].fillna('unknown', inplace=False)

    # Cambiando valores de float a int
    df['model_year'] = df['model_year'].astype(int)

    def replace_if_contains_multiple(df, column, replacements):
        """
        Replace the entire string in a specific DataFrame column 
        if it contains any of multiple keywords.

        :param df: Pandas DataFrame to modify.
        :param column: Column name to check.
        :param replacements: Dictionary {keyword: replacement_value}.
        :return: Modified DataFrame.
        """
        if column in df.columns:
            df["model"] = df["model"].astype(str).apply(
                lambda x: next((replacement for keyword, replacement in replacements.items() if keyword in x), x)
            )
        return df

    df = pd.DataFrame(df)

    # Dictionary with keywords and their respective replacements
    replacements = {
        "ford": "Ford",
        "chevrolet": "Chevrolet",
        "acura": "Acura",
        "bmw": "BMW",
        "buick": "Buick",
        "cadillac": "Cadillac",
        "chrysler": "Chrysler",
        "dodge": "Dodge",
        "gmc": "GMC",
        "honda": "Honda",
        "hyundai": "Hyundai",
        "jeep": "Jeep",
        "kia": "Kia",
        "mercedes": "Mercedes",
        "nissan": "Nissan",
        "ram": "Dodge Ram",
        "subaru": "Subaru",
        "toyota": "Toyota",
        "volkswagen": "Volkswagen"
    }

    # Apply the function
    df = replace_if_contains_multiple(df, "model", replacements)

    # reemplazar los valores de cadena

    df['condition_range'] = df['condition'].replace(
        to_replace = ['new', 'like new', 'excellent', 'good', 'fair', 'salvage'],
        value = [5,4,3,2,1,0]
    )

    # Eliminar columnas
    df.drop(columns=['paint_color'], inplace=True)
    df.drop(columns=['cylinders'], inplace=True)
    df.drop(columns=['condition_range'], inplace=True)
    df.drop(columns=['days_listed'], inplace=True)
    df.drop(columns=['date_posted'], inplace=True)
    df.drop(columns=['price_grouped'], inplace=True)
    df.drop(columns=['model_year_grouped'], inplace=True)
    #df.drop(columns=['is_4wd'], inplace=True)
    return df

df = load_data()

def show_explore_page():
    st.title("Explore car prices")

    st.write("""### Explore car prices""")

    data = df.groupby(["model"])["price"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    data = df.groupby(["type"])["price"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    data = df.groupby(["transmission"])["price"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    data = df.groupby(["is_4wd"])["price"].mean().sort_values(ascending=True)
    st.bar_chart(data)



    



    


    #fig1, ax1 = plt.subplots()
    #ax1.bar(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    #ax1.axis("equal")

    #st.write("""#### Distrubution of models""")

    #st.pyplot(fig1)

