import pandas as pd


def limpiar_datos(data_frame_sucio):

    df = data_frame_sucio.copy()

    # 1. Limpiar columnas de texto solo si existen
    columnas_texto = ["id_sucursal", "nombre_sucursal", "direccion_sucursal", "telefono_sucursal", "activo"]

    for columna in columnas_texto:
        if columna in df.columns:
            df[columna] = df[columna].astype("string").str.strip().str.lower()

    # 2. Validar activo solo si existe
    if "activo" in df.columns:
        df["activo"] = df["activo"].where(df["activo"].isin({"true", "false"}), pd.NA)

    # 3. Validar que id_sucursal no esté vacío
    if "id_sucursal" in df.columns:
        df = df[df["id_sucursal"].notna()]
        df = df[df["id_sucursal"] != ""]

    # 4. Eliminar nulos en campos obligatorios
    columnas_obligatorias = [c for c in ["id_sucursal", "nombre_sucursal", "direccion_sucursal"] if c in df.columns]
    df = df.dropna(subset=columnas_obligatorias)

    # 5. Eliminar duplicados
    df = df.drop_duplicates()

    return df