import pandas as pd


def limpiar_datos(data_frame_sucio):

    data_frame_limpio = data_frame_sucio.copy()

    # 1. Limpiar las columnas string del data frame
    columnas_texto = ["id_sucursal","id_cliente","direccion","departament","ciudad","contacto","codigo_casa_mx"]
    for columna in columnas_texto:
        data_frame_limpio[columna] = (
            data_frame_limpio[columna].astype("string").str.strip().str.lower()
        )


    # 1.1 Definir valore de string esperados
    valores_validos_aliados = ["Farmatodo", "Copidrogas", "Drogas la rebaja", "Drogueria pepos"]
    data_frame_limpio["aliado"] = data_frame_limpio["aliados"].where(

        data_frame_limpio["aliados"].isin(valores_validos_aliados), pd.NA
    )

    # 4 Eliminar registros que tengan datos obligatorios vacios
    columnas_obligatorias=["id_sucursal","id_cliente","direccion","departament","ciudad","contacto","codigo_casa_mx"]
    data_frame_limpio=data_frame_limpio.dropna(subset=columnas_obligatorias)

    # 5 Eliminar registros duplicados
    data_frame_limpio=data_frame_limpio.drop_duplicates()   

    return data_frame_limpio




