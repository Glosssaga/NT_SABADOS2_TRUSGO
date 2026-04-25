import random
from datetime import datetime, timedelta

def generar_simulacion(numeroCasaMatriz):
    listaCasaMatriz = ["CasaMatrizMedellin", "CasaMatrizRionegro"]
    codigosCasaMatriz = ["CMM01", "CMR02"]
    ciudades = ["Medellín", "Rionegro"]
    tipos = ["Farmaceuticas", "Farmacias", "consumidorFinal"]
    
    casasMatrices = []
    fechaInicial = datetime(2023, 1, 1)

    for i in range(numeroCasaMatriz):
        casaMatriz = {
            "codigo_casa_mx": random.choice(codigosCasaMatriz),
            "nombre": random.choice(listaCasaMatriz),
            "tipo": random.choice(tipos),
            "fecha_registro": fechaInicial + timedelta(days=random.randint(0, 365))
        }

        # --- SUCIEDAD CONTROLADA ---
        probabilidad = random.random()

        if probabilidad < 0.15:
            # Valores nulos
            casaMatriz["codigo_casa_mx"] = None
            casaMatriz["tipo"] = None
            
        elif probabilidad < 0.30:
            # Fecha inválida (string incorrecto pero no rompe el programa)
            casaMatriz["fecha_registro"] = "2023-13-45"
            
        elif probabilidad < 0.50:
            # Espacios en blanco
            casaMatriz["nombre"] = "  " + casaMatriz["nombre"] + "  "
            
        elif probabilidad < 0.75:
            # Inconsistencia de mayúsculas/minúsculas (SIN ERROR)
            if casaMatriz["codigo_casa_mx"] is not None:
                if random.choice([True, False]):
                    casaMatriz["codigo_casa_mx"] = casaMatriz["codigo_casa_mx"].lower()
                else:
                    casaMatriz["codigo_casa_mx"] = casaMatriz["codigo_casa_mx"].upper()

        casasMatrices.append(casaMatriz)
        
    return casasMatrices


