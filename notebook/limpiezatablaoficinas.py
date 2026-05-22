import pandas as pd


def limpiar_datos_oficinas(data_frame_sucio):

    df = data_frame_sucio.copy()

    # 1. Limpiar columnas de texto solo si existen
    columnas_texto = ["id_oficina", "nombre_oficina", "direccion", "telefono", "activo"]

    for columna in columnas_texto:
        if columna in df.columns:
            df[columna] = df[columna].astype("string").str.strip().str.lower()

    # 2. Validar activo solo si existe la columna
    if "activo" in df.columns:
        df["activo"] = df["activo"].where(df["activo"].isin({"true", "false"}), pd.NA)

    # 3. Validar que id_oficina no esté vacío
    if "id_oficina" in df.columns:
        df = df[df["id_oficina"].notna()]
        df = df[df["id_oficina"] != ""]

    # 4. Eliminar nulos en campos obligatorios que existan
    columnas_obligatorias = [c for c in ["id_oficina", "nombre_oficina", "direccion"] if c in df.columns]
    df = df.dropna(subset=columnas_obligatorias)

    # 5. Eliminar duplicados
    df = df.drop_duplicates()

    return df