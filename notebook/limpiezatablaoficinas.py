import pandas as pd
from datetime import datetime


def limpiar_datos_oficinas(data_frame_sucio):
    """
    Limpia y valida los datos de la tabla de oficinas.
    
    Procesos de limpieza:
    1. Limpia columnas de texto (strip, lowercase)
    2. Valida columnas numéricas (id_oficina positivo)
    3. Procesa y valida fechas
    4. Elimina filas con datos obligatorios vacíos
    5. Elimina registros duplicados
    """
    
    data_frame_limpio = data_frame_sucio.copy()
    
    # 1. Limpiar las columnas string del DF
    columnas_texto = ["nombre_oficina", "direccion", "departamento", "ciudad"]
    
    for columna in columnas_texto:
        # Eliminar espacios en blanco al inicio y al final, convertir a minúsculas
        data_frame_limpio[columna] = (
            data_frame_limpio[columna]
            .astype("string")
            .str.strip()
            .str.lower()
        )
    
    # 2. Limpiar las columnas numéricas del DF
    data_frame_limpio["id_oficina"] = pd.to_numeric(
        data_frame_limpio["id_oficina"], errors="coerce"
    )
    
    # 2.1 Validar que id_oficina sea mayor a 0
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id_oficina"] > 0]
    
    # 3. Limpiar columna de teléfono (verificar que tenga formato correcto)
    data_frame_limpio["telefono"] = data_frame_limpio["telefono"].astype("string").str.strip()
    
    # 4. Organizar las columnas de tipo fecha
    data_frame_limpio["fecha_apertura"] = pd.to_datetime(
        data_frame_limpio["fecha_apertura"], errors="coerce"
    )
    
    # 4.1 Si una fecha no es válida, la reemplazamos por un valor por defecto
    fecha_defecto = pd.to_datetime("2026-01-01")
    data_frame_limpio["fecha_apertura"] = (
        data_frame_limpio["fecha_apertura"].fillna(fecha_defecto)
    )
    
    # 5. Eliminar registros que tengan datos obligatorios vacíos
    columnas_obligatorias = [
        "id_oficina",
        "nombre_oficina",
        "ciudad",
        "departamento",
        "fecha_apertura",
    ]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)
    
    # 6. Eliminar registros duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()
    
    return data_frame_limpio