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

    # 2. Limpiar las columnas numéricas del data frame
    #data_frame_limpio[id]=pd.to_numeric(data_frame_limpio["id"]) #,errors="coerce")
    #data_frame_limpio["costo"]=pd.to_numeric(data_frame_limpio["costo"]) #,errors="coerce")

    # 2.1 Limpiando campos numericos que no tengan valores validos
    #data_frame_limpio=data_frame_limpio[data_frame_limpio["costo"]>=100000]
    #data_frame_limpio=data_frame_limpio[data_frame_limpio["id"]>=0]

    # 3. Limpiar las columnas de tipofecha del data frame.
    #data_frame_limpio["fecha"]=pd.to_datetime(data_frame_limpio["fecha"])#,errors="coerce")

    # 3.1 Si una fecha no viene la reemplazamos por un valor por defecto
    #fecha_default=pd.to_datetime("2026-01-01")
    #data_frame_limpio["fecha"]=data_frame_limpio["fecha"].fillna(fecha_default)

    # 4 Eliminar registros que tengan datos obligatorios vacios
    columnas_obligatorias=["id_sucursal","id_cliente","direccion","departament","ciudad","contacto","codigo_casa_mx"]
    data_frame_limpio=data_frame_limpio.dropna(subset=columnas_obligatorias)

    # 5 Eliminar registros duplicados
    data_frame_limpio=data_frame_limpio.drop_duplicates()   

    return data_frame_limpio




