import pandas as pd
from utils.simulador_Casa_Matriz import generar_simulacion


def cargar_simulacion_casa_matriz(cantidad=50):
    """Genera un DataFrame con datos de casa matriz usando el simulador."""
    registros = generar_simulacion(cantidad)
    return pd.DataFrame(registros)


def limpieza_datos(dataframe_sucio):
    """Limpia y valida la tabla de casa matriz generada por el simulador."""
    dataframe_limpio = dataframe_sucio.copy()

    # 1. Limpiar las columnas string del DF
    columnas_texto = ["codigo_casa_mx", "nombre", "tipo"]
    for columna in columnas_texto:
        dataframe_limpio[columna] = (
            dataframe_limpio[columna].astype("string").str.strip().str.lower()
        )

    # 1.1 Normalizar valores y marcar invalidos
    valores_validos = {"farmaceuticas", "farmacias", "consumidorfinal"}
    dataframe_limpio["tipo"] = dataframe_limpio["tipo"].where(
        dataframe_limpio["tipo"].isin(valores_validos), pd.NA
    )

    # 2. Validar codigo_casa_mx
    dataframe_limpio["codigo_casa_mx"] = (
        dataframe_limpio["codigo_casa_mx"].str.upper().astype("string")
    )
    patron_codigo = r"^[A-Z]{3}\d{2}$"
    dataframe_limpio["codigo_casa_mx"] = dataframe_limpio["codigo_casa_mx"].where(
        dataframe_limpio["codigo_casa_mx"].str.match(patron_codigo), pd.NA
    )

    # 3. Convertir fecha_registro a datetime, marcando inválidos como NaT
    dataframe_limpio["fecha_registro"] = pd.to_datetime(
        dataframe_limpio["fecha_registro"], errors="coerce"
    )

    # 4. Eliminar filas con campos obligatorios vacíos
    columnas_obligatorias = [
        "codigo_casa_mx",
        "nombre",
        "tipo",
        "fecha_registro",
    ]
    dataframe_limpio = dataframe_limpio.dropna(subset=columnas_obligatorias)

    # 5. Eliminar duplicados
    dataframe_limpio = dataframe_limpio.drop_duplicates().reset_index(drop=True)

    return dataframe_limpio


def ejecutar_ejemplo_casa_matriz(cantidad=20):
    """Genera, limpia y muestra un ejemplo de datos de Casa Matriz."""
    df_sucio = cargar_simulacion_casa_matriz(cantidad)
    df_limpio = limpieza_datos(df_sucio)

    print(f"Registros generados: {len(df_sucio)}")
    print(f"Registros limpios: {len(df_limpio)}")
    return df_sucio, df_limpio


if __name__ == "__main__":
    df_sucio, df_limpio = ejecutar_ejemplo_casa_matriz(20)
    print("\nPrimeros registros sucios:")
    print(df_sucio.head(10).to_string(index=False))
    print("\nPrimeros registros limpios:")
    print(df_limpio.head(10).to_string(index=False))
