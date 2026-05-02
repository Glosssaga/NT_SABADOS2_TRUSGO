import pandas as pd


def describir_datos(data_frame_limpio):
    """Describe un DataFrame limpio con información del dataset de Casa Matriz."""
    print("* DESCRIPCION DEL DATASET *")
    print(f"Numero de filas del dataset: {data_frame_limpio.shape[0]}")
    print(f"Numero de columnas del dataset: {data_frame_limpio.shape[1]}")
    print(f"Lista de columnas disponibles: {list(data_frame_limpio.columns)}")
    print("\nTipos de datos por columna:")
    print(data_frame_limpio.dtypes)

    print("\n* CONTEOS PARA COLUMNAS DE INTERES *")
    columnas_interes = ["tipo", "codigo_casa_mx", "nombre"]
    for columna in columnas_interes:
        if columna in data_frame_limpio.columns:
            print(f"\nConteo de valores para '{columna}':")
            print(data_frame_limpio[columna].value_counts(dropna=False))

    print("\n* ESTADISTICAS NUMERICAS *")
    datos_numericos = data_frame_limpio.select_dtypes(include=["number"])
    if not datos_numericos.empty:
        print(datos_numericos.describe(percentiles=[0.25, 0.5, 0.75]))
    else:
        print("No hay columnas numericas en el dataset.")

    # Buscar columnas de fecha en base a nombre y tipo
    columnas_fecha = [
        columna
        for columna in data_frame_limpio.columns
        if "fecha" in columna.lower()
    ]

    if columnas_fecha:
        for columna in columnas_fecha:
            fechas = pd.to_datetime(data_frame_limpio[columna], errors="coerce")
            print(f"\nFechas para '{columna}':")
            print(f"  - Fecha mas antigua: {fechas.min()}")
            print(f"  - Fecha mas reciente: {fechas.max()}")
            print(f"  - Valores no validos o nulos: {fechas.isna().sum()}")
    else:
        print("\nNo se detectaron columnas de fecha en el dataset.")


if __name__ == "__main__":
    print("Este modulo proporciona la funcion describir_datos(data_frame_limpio) para Casa Matriz.")
