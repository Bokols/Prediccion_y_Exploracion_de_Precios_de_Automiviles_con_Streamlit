# Descripción del Proyecto: Predicción y Exploración de Precios de Automóviles con Streamlit

## Introducción

Este proyecto tiene como objetivo desarrollar una **aplicación interactiva web** utilizando **Streamlit** que permite a los usuarios predecir el precio de un automóvil basado en ciertas características o explorar las tendencias de los precios de los automóviles a través de varias categorías. El proyecto utiliza modelos de machine learning para predecir los precios de los automóviles y visualizaciones para ayudar a los usuarios a comprender cómo las diferentes características afectan los precios de los automóviles. Implica la carga de datos, limpieza, entrenamiento de un modelo y la implementación de una interfaz interactiva tanto para la predicción como para la exploración.

La aplicación consta de dos secciones principales:
1. **Predicción de precios de automóviles**: Los usuarios ingresan diversas características de su automóvil para predecir su precio.
2. **Exploración de precios de automóviles**: Los usuarios exploran las relaciones entre los precios de los automóviles y características como el modelo, tipo, sistema de combustible, tipo de transmisión y si el automóvil es 4WD.

## Procedimientos

### 1. **Recopilación y Limpieza de Datos**
   - El conjunto de datos utilizado en este proyecto proviene de un archivo CSV (`vehicles_us.csv`) que contiene información detallada sobre varios automóviles, incluyendo características como precio, modelo, año, condición, kilometraje, tipo de combustible y tipo de transmisión.
   - Los datos se preprocesan para manejar los valores faltantes. Específicamente:
     - Los valores faltantes en ciertas columnas (como `is_4wd`, `model_year` y `odometer`) se completan utilizando diversos métodos, incluidos las tablas dinámicas y la mediana de características relacionadas.
     - Los valores no numéricos se codifican en valores numéricos mediante **Codificación de Etiquetas** para las variables categóricas (como modelo, condición, tipo de combustible, etc.).
     - Algunos valores se modifican para garantizar la consistencia (por ejemplo, los nombres de los modelos de automóviles se estandarizan).
     - Las transformaciones de datos incluyen la categorización de las columnas `price`, `odometer` y `model_year` en diferentes niveles para facilitar la agrupación.

### 2. **Entrenamiento del Modelo y Predicción**
   - Se entrena un modelo de regresión para predecir el precio de un automóvil en función de sus características (como modelo, año, kilometraje, tipo de combustible, condición, etc.).
   - Se utiliza **Codificación de Etiquetas** para convertir los datos categóricos (como los nombres de los modelos, la condición, el tipo de combustible) en valores numéricos que puedan ser alimentados en el modelo de machine learning.
   - El modelo entrenado se guarda mediante **pickle**, lo que permite cargarlo más tarde para realizar predicciones sin necesidad de volver a entrenarlo.

### 3. **Creación de la Interfaz Streamlit**
   - Se utiliza el marco de trabajo **Streamlit** para crear una interfaz web donde los usuarios pueden interactuar con el modelo.
     - La interfaz tiene dos opciones principales:
       - **Página de Predicción**: Los usuarios ingresan las características de su automóvil, y el modelo predice su precio.
       - **Página de Exploración**: Los usuarios pueden explorar la relación entre los precios de los automóviles y características como modelo, tipo de combustible, tipo de transmisión y si el automóvil es 4WD.
   - Los usuarios pueden seleccionar características del automóvil mediante menús desplegables y deslizadores. Una vez que se ingresan los datos, la predicción del precio se realiza utilizando el modelo previamente entrenado.
   - Los resultados se muestran dinámicamente, permitiendo a los usuarios ajustar los valores de entrada y ver inmediatamente el precio estimado actualizado.

### 4. **Exploración de Datos**
   - Para la sección **Explorar**, el proyecto utiliza `pandas` para agrupar los datos por diferentes categorías y calcular el precio promedio para cada categoría.
   - Se crean visualizaciones utilizando **matplotlib** y las funciones de gráficos integradas de **Streamlit**. Estas visualizaciones ayudan a los usuarios a comprender cómo diferentes características, como el modelo de automóvil, el tipo de vehículo y si el vehículo es 4WD, influyen en los precios de los automóviles.

### 5. **Interacción con el Usuario y Flujo de Trabajo**
   - Los usuarios comienzan eligiendo entre las secciones **Predecir** o **Explorar** desde una barra lateral de selección.
   - En la **Página de Predicción**, seleccionan características del automóvil como modelo, condición, tipo de combustible, tipo de transmisión, kilometraje y año. Al hacer clic en el botón **"Calcular el precio de tu automóvil"**, la aplicación utiliza el modelo previamente entrenado para predecir el precio del automóvil.
   - En la **Página de Exploración**, los usuarios pueden ver gráficos de barras que muestran cómo los precios promedio de los automóviles varían según diferentes características como el modelo del automóvil, el tipo de vehículo y si el vehículo es 4WD.

## Hallazgos

### 1. **Preprocesamiento y Limpieza de Datos**
   - La limpieza de datos fue esencial para manejar los valores faltantes y garantizar la precisión del modelo. Las columnas con valores faltantes se manejaron completándolos con los valores medianos o utilizando tablas dinámicas.
   - La codificación de etiquetas se aplicó con éxito para convertir los datos no numéricos en formato numérico, lo que permitió que el modelo de machine learning pudiera procesarlos.

### 2. **Desempeño del Modelo**
   - El modelo de regresión proporcionó una estimación razonable de los precios de los automóviles basándose en las características de entrada, aunque podría mejorarse con más ajustes y técnicas avanzadas.
   - La precisión del modelo depende de la calidad de las características de entrada. Características como el año del modelo, el kilometraje y la condición tuvieron un impacto significativo en el precio predicho, mientras que características menos relevantes (como el color de la pintura) tuvieron un impacto mínimo en el resultado del modelo.

### 3. **Información de la Exploración**
   - La **Página de Exploración** permitió a los usuarios obtener información sobre cómo diferentes características afectan los precios de los automóviles. Por ejemplo:
     - **Modelos de automóviles** como Toyota y Honda generalmente tuvieron precios promedio más altos que los modelos menos populares.
     - **El tipo de vehículo** también jugó un papel importante en la determinación del precio, con SUVs y camiones tendiendo a tener precios más altos que sedanes o hatchbacks.
     - El **tipo de transmisión** influyó en el precio, siendo las transmisiones automáticas generalmente más caras que las manuales.
     - Los **vehículos 4WD** típicamente tuvieron precios más altos en comparación con los vehículos 2WD.

### 4. **Interactividad**
   - Las características interactivas de Streamlit permitieron a los usuarios probar rápidamente diferentes combinaciones de entradas y ver cómo cambiaba el precio. Este nivel de interactividad mejora el compromiso del usuario y proporciona una experiencia fácil de usar.

## Conclusión

Este proyecto desarrolló con éxito un **sistema de predicción de precios de automóviles** utilizando **Streamlit**. El sistema permite a los usuarios predecir el precio de un automóvil basado en diversas características como el modelo, la condición, el tipo de combustible y el kilometraje. También proporciona una herramienta valiosa para explorar cómo los precios de los automóviles varían según diferentes características. Al preprocesar los datos de manera efectiva y aplicar técnicas de machine learning, el sistema proporciona predicciones precisas y conocimientos valiosos.

### Recomendaciones para Trabajos Futuros:
1. **Mejora del Modelo**: El modelo de regresión actual puede mejorarse experimentando con diferentes algoritmos (por ejemplo, árboles de decisión, bosques aleatorios o gradient boosting) para aumentar la precisión de la predicción.
2. **Características Adicionales**: Incluir más características, como la ubicación y detalles del vendedor, podría mejorar la capacidad predictiva del modelo.
3. **Mejoras en la Experiencia del Usuario**: Añadir más visualizaciones en la **Página de Exploración** podría proporcionar a los usuarios información más profunda sobre las tendencias de los precios de los automóviles.
4. **Integración de Datos en Tiempo Real**: Incorporar datos en tiempo real de los mercados de automóviles ayudaría a proporcionar predicciones y tendencias actualizadas.

En general, este proyecto ofrece una herramienta integral tanto para predecir los precios de los automóviles como para explorar los factores que los influyen, proporcionando un valor significativo a los posibles compradores y vendedores de automóviles.
