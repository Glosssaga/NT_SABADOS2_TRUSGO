import pandas as pd

from utils.simulador_Casa_Matriz import generar_simulacion

simulaciones = generar_simulacion(5)
simulaciones_ordenadas = pd.DataFrame(simulaciones)
print(simulaciones_ordenadas)
