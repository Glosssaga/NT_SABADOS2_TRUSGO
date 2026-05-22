import sys
import os
import pandas as pd
import requests

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
from notebook.limpiezaTablaCasaMatriz import cargar_simulacion_casa_matriz, limpieza_datos
from notebook.descripcionOficinas import describir_datos
from utils.sucursal_cliente import generar_sucursal_cliente
from notebook.limpiezaTSucursal_Cliente import limpiar_datos as limpiar_sucursal


def ejecutar_pipeline(num_registros=1000, guardar_sucios=True, verbose=True):
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

    if guardar_sucios:
        simulaciones_sucio.to_json("data/simulaciones.json", orient="records", indent=4, date_format="iso")
        simulaciones_sucio.to_csv("data/simulaciones.csv", index=False)
        print(f"\n[OK] Datos sin limpiar guardados en data/simulaciones.json y data/simulaciones.csv")

    if verbose:
        print(f"\n{simulaciones_sucio.info()}")

    print("\n" + "=" * 60)
    print("APLICANDO LIMPIEZA DE DATOS")
    print("=" * 60)

    simulaciones_ordenadas = limpiar_datos_oficinas(simulaciones_sucio)
    print(f"[OK] Limpieza completada")
    print(f"  - Total registros: {len(simulaciones_ordenadas)}")
    print(f"  - Registros eliminados: {len(simulaciones_sucio) - len(simulaciones_ordenadas)}")
    print(f"  - Porcentaje retenido: {(len(simulaciones_ordenadas)/len(simulaciones_sucio)*100):.1f}%")

    simulaciones_ordenadas.to_json("data/simulaciones_limpias.json", orient="records", indent=4, date_format="iso")
    simulaciones_ordenadas.to_csv("data/simulaciones_limpias.csv", index=False)
    print(f"\n[OK] Datos limpios guardados en data/simulaciones_limpias.json y data/simulaciones_limpias.csv")

    describir_datos(simulaciones_ordenadas)

    print("\n" + "=" * 60)
    print("PROCESO COMPLETADO")
    print("=" * 60 + "\n")

    return simulaciones_ordenadas


def ejecutar_colaboradores(num_registros=1000, verbose=True):
    print("\n" + "=" * 60)
    print("GENERANDO DATOS DE COLABORADORES")
    print("=" * 60)

    colaboradores_datos = generar_colaboradores(num_registros)
    df_colaboradores = pd.DataFrame(colaboradores_datos)
    print(f"[OK] Se generaron {len(df_colaboradores)} registros de colaboradores")

    if verbose:
        print(f"\nColumnas: {list(df_colaboradores.columns)}")
        print(df_colaboradores.head())
        print(f"\n{df_colaboradores.info()}")

    df_colaboradores.to_json("colaboradores.json", orient="records", indent=4, date_format="iso")
    df_colaboradores.to_csv("colaboradores.csv", index=False)
    print(f"\n[OK] Datos guardados en colaboradores.json y colaboradores.csv")

    print("\n" + "=" * 60)
    print("PROCESO DE COLABORADORES COMPLETADO")
    print("=" * 60 + "\n")

    describir_datos(df_colaboradores)
    return df_colaboradores


def ejecutar_casa_matriz(num_registros=1000, guardar_sucios=True, verbose=True):
    print("\n" + "=" * 60)
    print("GENERANDO DATOS DE CASA MATRIZ")
    print("=" * 60)

    df_sucio = cargar_simulacion_casa_matriz(num_registros)
    print(f"[OK] Se generaron {len(df_sucio)} registros de Casa Matriz")

    if verbose:
        print(f"\nColumnas: {list(df_sucio.columns)}")
        print(df_sucio.head())

    if guardar_sucios:
        df_sucio.to_json("data/simulaciones_casamatriz.json", orient="records", indent=4, date_format="iso")
        df_sucio.to_csv("data/simulaciones_casamatriz.csv", index=False)

    print("\n" + "=" * 60)
    print("APLICANDO LIMPIEZA DE CASA MATRIZ")
    print("=" * 60)

    df_limpio = limpieza_datos(df_sucio)
    print(f"[OK] Limpieza completada")
    print(f"  - Total registros: {len(df_limpio)}")
    print(f"  - Registros eliminados: {len(df_sucio) - len(df_limpio)}")
    print(f"  - Porcentaje retenido: {(len(df_limpio)/len(df_sucio)*100):.1f}%")

    df_limpio.to_json("data/simulaciones_casamatriz_limpias.json", orient="records", indent=4, date_format="iso")
    df_limpio.to_csv("data/simulaciones_casamatriz_limpias.csv", index=False)
    print(f"\n[OK] Datos limpios guardados en data/simulaciones_casamatriz_limpias.json y data/simulaciones_casamatriz_limpias.csv")

    print("\n" + "=" * 60)
    print("PROCESO DE CASA MATRIZ COMPLETADO")
    print("=" * 60 + "\n")

    return df_limpio


def ejecutar_oficinas_api(verbose=True):
    print("\n" + "=" * 60)
    print("CONSUMIENDO API DE OFICINAS")
    print("=" * 60)

    try:
        respuesta = requests.get("http://localhost:8082/oficinas")
        respuesta.raise_for_status()
        datos = respuesta.json()
    except Exception as e:
        print(f"[ERROR] No se pudo conectar a la API: {e}")
        return None

    df = pd.DataFrame(datos)
    print(f"[OK] Se obtuvieron {len(df)} registros de la API")

    renombrar = {
        "idOficina"        : "id_oficina",
        "nombreOficina"    : "nombre_oficina",
        "direccionOficina" : "direccion",
        "telefonoOficina"  : "telefono",
        "activo"           : "activo"
    }
    df = df.rename(columns=renombrar)
    df["departamento"]   = "sin_dato"
    df["ciudad"]         = "sin_dato"
    df["fecha_apertura"] = pd.to_datetime("2026-01-01")

    df_limpio = limpiar_datos_oficinas(df)
    print(f"[OK] Limpieza completada - Total registros: {len(df_limpio)}")

    df_limpio.to_json("data/oficinas_api_limpias.json", orient="records", indent=4, date_format="iso")
    df_limpio.to_csv("data/oficinas_api_limpias.csv", index=False)
    print(f"\n[OK] Guardado en data/oficinas_api_limpias.json y data/oficinas_api_limpias.csv")

    print("\n" + "=" * 60)
    print("PROCESO DE OFICINAS API COMPLETADO")
    print("=" * 60 + "\n")

    describir_datos(df_limpio)
    return df_limpio


def ejecutar_sucursal_cliente(num_registros=1000, guardar_sucios=True, verbose=True):
    print("\n" + "=" * 60)
    print("GENERANDO DATOS DE SUCURSAL CLIENTE")
    print("=" * 60)

    datos = generar_sucursal_cliente(num_registros)
    df_sucio = pd.DataFrame(datos)
    print(f"[OK] Se generaron {len(df_sucio)} registros de sucursal cliente")

    if verbose:
        print(f"\nColumnas: {list(df_sucio.columns)}")
        print(df_sucio.head())

    if guardar_sucios:
        df_sucio.to_json("data/sucursal_cliente.json", orient="records", indent=4, date_format="iso")
        df_sucio.to_csv("data/sucursal_cliente.csv", index=False)
        print(f"\n[OK] Datos sin limpiar guardados en data/sucursal_cliente.json y data/sucursal_cliente.csv")

    print("\n" + "=" * 60)
    print("APLICANDO LIMPIEZA DE SUCURSAL CLIENTE")
    print("=" * 60)

    df_limpio = limpiar_sucursal(df_sucio)
    print(f"[OK] Limpieza completada")
    print(f"  - Total registros: {len(df_limpio)}")
    print(f"  - Registros eliminados: {len(df_sucio) - len(df_limpio)}")
    print(f"  - Porcentaje retenido: {(len(df_limpio)/len(df_sucio)*100):.1f}%")

    df_limpio.to_json("data/sucursal_cliente_limpias.json", orient="records", indent=4, date_format="iso")
    df_limpio.to_csv("data/sucursal_cliente_limpias.csv", index=False)
    print(f"\n[OK] Datos limpios guardados en data/sucursal_cliente_limpias.json y data/sucursal_cliente_limpias.csv")

    print("\n" + "=" * 60)
    print("PROCESO DE SUCURSAL CLIENTE COMPLETADO")
    print("=" * 60 + "\n")

    describir_datos(df_limpio)
    return df_limpio


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("INICIANDO PROCESAMIENTO DE DATOS")
    print("=" * 60)

    ejecutar_pipeline(num_registros=1000, guardar_sucios=True, verbose=True)
    ejecutar_colaboradores(num_registros=1000, verbose=True)
    ejecutar_casa_matriz(num_registros=1000, guardar_sucios=True, verbose=True)
    ejecutar_oficinas_api(verbose=True)
    ejecutar_sucursal_cliente(num_registros=1000, guardar_sucios=True, verbose=True)

    print("\n" + "=" * 60)
    print("[OK] TODOS LOS PROCESOS COMPLETADOS")
    print("=" * 60)