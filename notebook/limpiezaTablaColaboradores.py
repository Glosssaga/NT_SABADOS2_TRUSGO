import pandas as pd


def limpieza_datos(dataframe_sucio):

    df = dataframe_sucio.copy()

    # 1. Limpiar columnas de texto
    columnas_texto = ["id_colaborador", "nombre_colaborador", "cargo", "telefono", "activo"]

    for columna in columnas_texto:
        df[columna] = df[columna].astype("string").str.strip().str.lower()

    # 2. Validar cargos permitidos
    cargos_validos = {"gerente", "despachador", "desarrollador", "diseñador", "soporte técnico"}
    df["cargo"] = df["cargo"].where(df["cargo"].isin(cargos_validos), pd.NA)

    # 3. Validar que activo solo tenga valores permitidos
    df["activo"] = df["activo"].where(df["activo"].isin({"true", "false"}), pd.NA)

    # 4. Eliminar nulos en campos obligatorios
    columnas_obligatorias = ["id_colaborador", "nombre_colaborador", "cargo", "activo"]
    df = df.dropna(subset=columnas_obligatorias)

    # 5. Eliminar duplicados
    df = df.drop_duplicates()

    return df