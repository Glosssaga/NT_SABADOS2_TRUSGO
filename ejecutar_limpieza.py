import pandas as pd
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.tablaOficinas import simular_oficinas
from notebook.limpiezatablaoficinas import limpiar_datos_oficinas

# Generar datos de oficinas con errores controlados
print("=" * 60)
print("GENERANDO DATOS SIMULADOS DE OFICINAS")
print("=" * 60)

datos_simulados = simular_oficinas(100)
df_sucio = pd.DataFrame(datos_simulados)

print(f"\n✓ Se generaron {len(df_sucio)} registros de oficinas")
print(f"\nColumnas: {list(df_sucio.columns)}")
print(f"\nPrimeros 5 registros (ANTES DE LIMPIAR):")
print(df_sucio.head())

print(f"\nEstadísticas ANTES de limpiar:")
print(f"  - Total registros: {len(df_sucio)}")
print(f"  - Registros con id_oficina inválido (<=0 o NaN): {df_sucio['id_oficina'].isna().sum() + (df_sucio['id_oficina'] <= 0).sum()}")
print(f"  - Registros con fecha_apertura vacía: {df_sucio['fecha_apertura'].isna().sum()}")
print(f"\n{df_sucio.info()}")

# Aplicar limpieza
print("\n" + "=" * 60)
print("APLICANDO LIMPIEZA")
print("=" * 60)

df_limpio = limpiar_datos_oficinas(df_sucio)

print(f"\n✓ Limpieza completada")
print(f"\nEstadísticas DESPUÉS de limpiar:")
print(f"  - Total registros: {len(df_limpio)}")
print(f"  - Registros eliminados: {len(df_sucio) - len(df_limpio)}")
print(f"  - Porcentaje retenido: {(len(df_limpio)/len(df_sucio)*100):.1f}%")

print(f"\nPrimeros 5 registros (DESPUÉS DE LIMPIAR):")
print(df_limpio.head())

print(f"\n{df_limpio.info()}")

# Guardar datos limpios
ruta_salida = './data/oficinas_limpias.csv'
df_limpio.to_csv(ruta_salida, index=False)
print(f"\n✓ Datos limpios guardados en: {ruta_salida}")

print("\n" + "=" * 60)
print("PROCESO COMPLETADO")
print("=" * 60)
