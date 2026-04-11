import sys
import os
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.tablaOficinas import simular_oficinas

simulaciones = simular_oficinas(5)

simulaciones_ordenadas=pd.DataFrame(simulaciones)

#Convirtiendo nuestra simulación en dos formatos diferrentes
#json
simulaciones_ordenadas.to_json("data/simulaciones.json",orient="records",indent=4)

#csv
simulaciones_ordenadas.to_csv("data/simulaciones.csv")