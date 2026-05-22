import requests
import pandas as pd


def consumo_api_tabla_colaboradores():

    url = "http://localhost:8082/colaboradores"

    try:
        response = requests.get(url)
        response.raise_for_status()
        colaboradores = response.json()
        print(f"[OK] Se obtuvieron {len(colaboradores)} registros de colaboradores")

        # Convertir a DataFrame
        df = pd.DataFrame(colaboradores)

        # Renombrar columnas del API al formato de limpieza
        renombrar = {
            "idColaborador"    : "id_colaborador",
            "nombreColaborador": "nombre_colaborador",
            "cargo"            : "cargo",
            "telefono"         : "telefono",
            "activo"           : "activo"
        }
        df = df.rename(columns=renombrar)

        print(f"\nColumnas obtenidas: {list(df.columns)}")
        print(df.head())

        return df

    except Exception as e:
        print(f"[ERROR] No se pudo conectar a la API: {e}")
        return None