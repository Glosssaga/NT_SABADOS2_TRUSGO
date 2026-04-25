import pandas as pd

def limpieza_datos(dataframe_sucio):
    
    dataframe_limpio = dataframe_sucio.copy()

    # 1. Limpiar las columnas string del DF
    columnas_texto = ["id_colaboradora", "cargo", "cedula", "id_oficina"]

    for columna in columnas_texto:
        dataframe_limpio[columna] = dataframe_limpio[columna].astype("string").str.strip().str.lower()

    # 1.1 Definir valores de string esperados (fuera del for)
    valores_validos = {"gerente", "despachador", "desarrollador", "diseñador", "soporte técnico"}
    dataframe_limpio["cargo"] = dataframe_limpio["cargo"].where(
        dataframe_limpio["cargo"].isin(valores_validos), pd.NA
    )

    # 2. Convertir a numérico
    dataframe_limpio["id_colaboradora"] = pd.to_numeric(dataframe_limpio["id_colaboradora"], errors="coerce")
    dataframe_limpio["id_oficina"] = pd.to_numeric(dataframe_limpio["id_oficina"], errors="coerce")
    dataframe_limpio["cedula"] = dataframe_limpio["cedula"].where(
        dataframe_limpio["cedula"].str.match(r"^\d{10}$"), pd.NA
    )

    # 2.1 Filtrar valores numéricos inválidos
    dataframe_limpio = dataframe_limpio[dataframe_limpio["id_colaboradora"] >= 1000]
    dataframe_limpio = dataframe_limpio[dataframe_limpio["id_oficina"] >= 1000]

    # 4. Eliminar filas con campos obligatorios vacíos
    columnas_obligatorias = ["id_colaboradora", "id_oficina", "cedula"]
    dataframe_limpio = dataframe_limpio.dropna(subset=columnas_obligatorias)

    # 5. Eliminar duplicados
    dataframe_limpio = dataframe_limpio.drop_duplicates()

    return dataframe_limpio