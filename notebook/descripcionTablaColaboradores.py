# Toda rutina de analisis debe describir el data set

# 1.Es importante conocer cuantos registros tengo
#2. Es importante conocer los atributos que tengo
#3. Es util tener acceso a una lista con los nombres de los atributos
#4.Es util hacer conteos de algunas columnas de interes
#5.Es util conocer las estadisticas descriptivas de los campos numericos
#media-maximo-minimo-la dispersion estandar y los percentiles
#6. Si hay fechas es util conocer la cual la fecha mmas antigua y la fecha mas reciente

import pandas as pd

def descripcion_datos(dataframe):
   
    print("----- DESCRIPCION DEL DATASET -----")

    print(f"Numero de filas del dataset: {dataframe.shape[0]}") #cuantas filas tiene el dataset
    print(f"Numero de columnas del dataset: {dataframe.shape[1]}") #cuantas columnas tiene el dataset
    print(f"Lista de columnas disponibles: {list(dataframe.columns)}")#list lista de columnas ayuda de py
    print(f"Tipos de datos de cada atributo:\n {dataframe.dtypes}") #tipos de datos de cada columna

    print("*** ESTADISTICAS ***")

    print(f"{dataframe[['id_colaboradora','id_oficina','cedula']].describe()}")

     # Informacion de conteos valiosos
    print("----- CONTEOS ***")
    print(f"{dataframe['id_colaboradora'].value_counts()}") #conteo de cada servicio
    print(f"{dataframe['id_oficina'].value_counts()}") #fecha mas antigua
    print(f"{dataframe['cedula'].value_counts()}") #conteo de cada cedula

    return dataframe
