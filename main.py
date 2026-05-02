import sys
import os
import pandas as pd

try:
    import pandas as pd
except ImportError:
    print("Error: pandas is not installed. Please install it using: pip install pandas")
    sys.exit(1)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
os.makedirs(DATA_DIR, exist_ok=True)

from utils.tablaOficinas import simular_oficinas
from notebook.limpiezatablaoficinas import limpiar_datos_oficinas
from utils.tablaColaboradores import generar_colaboradores
<<<<<<< HEAD
from notebook.limpiezaTablaCasaMatriz import cargar_simulacion_casa_matriz, limpieza_datos
=======
from notebook.descripcionOficinas import describir_datos
from utils.descripcionSucursalClientes import describir_datos
>>>>>>> 00150c26685abd87c13b68144a1e0d8830a849d6


def ejecutar_pipeline(num_registros=1000, guardar_sucios=True, verbose=True):
    """
    Ejecuta el pipeline completo de generación y limpieza de datos de oficinas.

    Args:
        num_registros (int): Número de registros a generar. Default: 1000
        guardar_sucios (bool): Si guardar los datos sin limpiar. Default: True
        verbose (bool): Si mostrar estadísticas detalladas. Default: True
    """

    # GENERAR DATOS SIMULADOS DE OFICINAS

    print("\n" + "=" * 60)
    print("GENERANDO DATOS SIMULADOS DE OFICINAS")
    print("=" * 60)

    simulaciones = simular_oficinas(num_registros)
    simulaciones_sucio = pd.DataFrame(simulaciones)

    print(f"[OK] Se generaron {len(simulaciones_sucio)} registros de oficinas")

    if verbose:
        print(f"\nColumnas: {list(simulaciones_sucio.columns)}")
        print(f"\nPrimeros 5 registros (ANTES DE LIMPIAR):")
        print(simulaciones_sucio.head())

    print(f"\nEstadísticas ANTES de limpiar:")
    print(f"  - Total registros: {len(simulaciones_sucio)}")
    print(
        f"  - Registros con id_oficina inválido: {simulaciones_sucio['id_oficina'].isna().sum() + (simulaciones_sucio['id_oficina'] <= 0).sum()}"
    )
    print(
        f"  - Registros con fecha_apertura vacía: {simulaciones_sucio['fecha_apertura'].isna().sum()}"
    )

    # Guardar datos SUCIOS (opcional)
    if guardar_sucios:
        simulaciones_sucio.to_json(
            "data/simulaciones.json", orient="records", indent=4, date_format="iso"
        )
        simulaciones_sucio.to_csv("data/simulaciones.csv", index=False)
        print(
            f"\n[OK] Datos sin limpiar guardados en data/simulaciones.json y data/simulaciones.csv"
        )

    if verbose:
        print(f"\n{simulaciones_sucio.info()}")

    # APLICAR LIMPIEZA DE DATOS

    print("\n" + "=" * 60)
    print("APLICANDO LIMPIEZA DE DATOS")
    print("=" * 60)

    simulaciones_ordenadas = limpiar_datos_oficinas(simulaciones_sucio)

    print(f"[OK] Limpieza completada")
    print(f"\nEstadísticas DESPUÉS de limpiar:")
    print(f"  - Total registros: {len(simulaciones_ordenadas)}")
    print(
        f"  - Registros eliminados: {len(simulaciones_sucio) - len(simulaciones_ordenadas)}"
    )
    print(
        f"  - Porcentaje retenido: {(len(simulaciones_ordenadas)/len(simulaciones_sucio)*100):.1f}%"
    )

    if verbose:
        print(f"\nPrimeros 5 registros (DESPUÉS DE LIMPIAR):")
        print(simulaciones_ordenadas.head())
        print(f"\n{simulaciones_ordenadas.info()}")

    # Guardar datos LIMPIOS
    simulaciones_ordenadas.to_json(
        "data/simulaciones_limpias.json", orient="records", indent=4, date_format="iso"
    )
    simulaciones_ordenadas.to_csv("data/simulaciones_limpias.csv", index=False)

    print(
        f"\n[OK] Datos limpios guardados en data/simulaciones_limpias.json y data/simulaciones_limpias.csv"
    )

    # DESCRIPCION DEL DATASET
    print("\n" + "=" * 60)
    print("DESCRIPCION DEL DATASET LIMPIO")
    print("=" * 60)
    
    describir_datos(simulaciones_ordenadas)

    print("\n" + "=" * 60)
    print("PROCESO COMPLETADO")
    print("=" * 60 + "\n")

    # Describir datos limpios
    describir_datos(simulaciones_ordenadas)

    return simulaciones_ordenadas


def ejecutar_colaboradores(num_registros=1000, verbose=True):
    """
    Ejecuta la generación y guardado de datos de colaboradores.

    Args:
        num_registros (int): Número de registros a generar. Default: 1000
        verbose (bool): Si mostrar información. Default: True
    """

    print("\n" + "=" * 60)
    print("GENERANDO DATOS DE COLABORADORES")
    print("=" * 60)

    colaboradores_datos = generar_colaboradores(num_registros)
    df_colaboradores = pd.DataFrame(colaboradores_datos)

    print(f"[OK] Se generaron {len(df_colaboradores)} registros de colaboradores")

    if verbose:
        print(f"\nColumnas: {list(df_colaboradores.columns)}")
        print(f"\nPrimeros 5 registros:")
        print(df_colaboradores.head())
        print(f"\n{df_colaboradores.info()}")

    # Guardar colaboradores
    df_colaboradores.to_json(
        "colaboradores.json", orient="records", indent=4, date_format="iso"
    )
    df_colaboradores.to_csv("colaboradores.csv", index=False)

    print(
        f"\n[OK] Datos de colaboradores guardados en colaboradores.json y colaboradores.csv"
    )

    print("\n" + "=" * 60)
    print("PROCESO DE COLABORADORES COMPLETADO")
    print("=" * 60 + "\n")

    # Describir datos de colaboradores
    describir_datos(df_colaboradores)

    return df_colaboradores


def ejecutar_casa_matriz(num_registros=1000, guardar_sucios=True, verbose=True):
    """Genera y limpia datos de Casa Matriz usando el notebook de limpieza."""
    print("\n" + "=" * 60)
    print("GENERANDO DATOS DE CASA MATRIZ")
    print("=" * 60)

    df_sucio = cargar_simulacion_casa_matriz(num_registros)

    print(f"[OK] Se generaron {len(df_sucio)} registros de Casa Matriz")
    if verbose:
        print(f"\nColumnas: {list(df_sucio.columns)}")
        print(f"\nPrimeros 5 registros (ANTES DE LIMPIAR):")
        print(df_sucio.head())

    if guardar_sucios:
        df_sucio.to_json(
            "data/simulaciones_casamatriz.json",
            orient="records",
            indent=4,
            date_format="iso",
        )
        df_sucio.to_csv("data/simulaciones_casamatriz.csv", index=False)
        print(
            f"\n[OK] Datos sin limpiar guardados en data/simulaciones_casamatriz.json y data/simulaciones_casamatriz.csv"
        )

    print("\n" + "=" * 60)
    print("APLICANDO LIMPIEZA DE CASA MATRIZ")
    print("=" * 60)

    df_limpio = limpieza_datos(df_sucio)

    print(f"[OK] Limpieza completada")
    print(f"\nEstadísticas DESPUÉS de limpiar:")
    print(f"  - Total registros: {len(df_limpio)}")
    print(
        f"  - Registros eliminados: {len(df_sucio) - len(df_limpio)}"
    )
    print(
        f"  - Porcentaje retenido: {(len(df_limpio)/len(df_sucio)*100):.1f}%"
    )

    if verbose:
        print(f"\nPrimeros 5 registros (DESPUÉS DE LIMPIAR):")
        print(df_limpio.head())
        print(f"\n{df_limpio.info()}")

    df_limpio.to_json(
        "data/simulaciones_casamatriz_limpias.json",
        orient="records",
        indent=4,
        date_format="iso",
    )
    df_limpio.to_csv("data/simulaciones_casamatriz_limpias.csv", index=False)
    print(
        f"\n[OK] Datos limpios guardados en data/simulaciones_casamatriz_limpias.json y data/simulaciones_casamatriz_limpias.csv"
    )

    print("\n" + "=" * 60)
    print("PROCESO DE CASA MATRIZ COMPLETADO")
    print("=" * 60 + "\n")

    return df_limpio


if __name__ == "__main__":
    # Ejecutar todos los pipelines con configuración por defecto (1000 registros)
    print("\n" + "=" * 60)
    print("INICIANDO PROCESAMIENTO DE DATOS")
    print("=" * 60)

    # Ejecutar pipeline de oficinas
    ejecutar_pipeline(num_registros=1000, guardar_sucios=True, verbose=True)

    # Ejecutar pipeline de colaboradores
    ejecutar_colaboradores(num_registros=1000, verbose=True)

    # Ejecutar pipeline de Casa Matriz
    ejecutar_casa_matriz(num_registros=1000, guardar_sucios=True, verbose=True)

    print("\n" + "=" * 60)
    print("[OK] TODOS LOS PROCESOS COMPLETADOS")
    print("=" * 60)
