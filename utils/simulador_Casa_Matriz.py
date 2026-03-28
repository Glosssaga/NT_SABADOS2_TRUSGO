import random
from datetime import datetime, timedelta

def simular_casa_matriz (numeroCasaMatriz):
    
    listaCasaMatriz=["CasaMatrizMedellin", "CasaMatrizRionegro"]

    codigosCasaMatriz = ["CMM01", "CMR02"]

    ciudades = ["Medellín", "Rionegro"]

    tipos = ["Farmaceutricas", "Farmacias" "consumidorFinal"]

    casasMatrices = []

    fechaInicial = datetime (2023, 1, 1)
    for i in range (numeroCasaMatriz):
        casaMatriz= {
            "codigo_casa_mx" : random.randint(0,10000),
            "nombre": random.choice(listaCasaMatriz),
            "tipo": random.choice(tipos),
        }

        casasMatrices.append(casaMatriz)
        return casasMatrices


    