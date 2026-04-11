import pandas as pd

from utils.tablaColaboradores import generar_colaboradores

colaboradores = generar_colaboradores(5)

simulaciones_ordenadas = pd.DataFrame(colaboradores)

#convirtiendo nuestra simulacion en dos diferentes formatos

#json

simulaciones_ordenadas.to_json("colaboradores.json",orient="records",indent=4)

#csv
simulaciones_ordenadas.to_csv("colaboradores.csv")

print("Archivos generados:") 
print("colaboradores.json")
print("colaboradores.csv")  