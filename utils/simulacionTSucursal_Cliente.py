import random

# Constants
ALIADOS = ["Farmatodo", "Copidrogas", "Drogas la rebaja", "Drogueria pepos"]


def generar_simulacion(numero_simulaciones):

    simulaciones = []
    for _ in range(numero_simulaciones):
        simulacion = {
            "aliado": random.choice(ALIADOS),
        }

        simulaciones.append(simulacion)
    return simulaciones
