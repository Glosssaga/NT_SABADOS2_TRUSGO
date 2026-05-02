import pandas as pd

def describir_datos(data_frame_limpio):
    """
    Rutina de análisis que describe el dataset.
    
    Proporciona información sobre:
    1. Cantidad de registros
    2. Cantidad de atributos
    3. Nombres de los atributos
    4. Conteos de algunas columnas de interés
    5. Estadísticas descriptivas de campos numéricos (media, max, min, std, percentiles)
    6. Fechas más antigua y reciente (si aplica)
    
    Args:
        data_frame_limpio (pd.DataFrame): DataFrame limpio a analizar
    """
    
    print("*** DESCRIPCION DEL DATASET ***")
    print(f"Numero de filas del dataset: {data_frame_limpio.shape[0]}")
    print(f"Numero de columnas del dataset: {data_frame_limpio.shape[1]}")
    print(f"Listas de las columnas disponibles: {data_frame_limpio.columns.tolist()}")
    print(f"Tipos de dato de cada atributo: \n{data_frame_limpio.dtypes}")

    # Estadísticas (SOLO APLICA PARA DATOS NUMERICOS)
    print("\n*** ESTADISTICAS ***")
    columnas_numericas = data_frame_limpio.select_dtypes(include=['number']).columns.tolist()
    if columnas_numericas:
        print(data_frame_limpio[columnas_numericas].describe())
    else:
        print("No hay columnas numéricas en el dataset")

    # Información de conteos valiosos
    print("\n*** CONTEOS POR COLUMNAS ***")
    columnas_categoricas = data_frame_limpio.select_dtypes(include=['object']).columns.tolist()
    for columna in columnas_categoricas[:5]:  # Limitar a primeras 5 columnas categóricas
        if data_frame_limpio[columna].nunique() < 50:  # Solo si tiene pocos valores únicos
            print(f"\nConteos de '{columna}':")
            print(data_frame_limpio[columna].value_counts())

    # Describiendo las fechas
    fechas_encontradas = data_frame_limpio.select_dtypes(include=['datetime64']).columns.tolist()
    if fechas_encontradas:
        print("\n*** DESCRIPCION DE FECHAS ***")
        for columna_fecha in fechas_encontradas:
            print(f"Columna: {columna_fecha}")
            print(f"  Fecha más antigua: {data_frame_limpio[columna_fecha].min()}")
            print(f"  Fecha más reciente: {data_frame_limpio[columna_fecha].max()}")
