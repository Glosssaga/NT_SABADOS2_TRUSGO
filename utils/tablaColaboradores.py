# Id_Colaboradora int varchar (10)
#Cargo varchar(50)
#Cedula varchar(20)
#Id_Oficina int varchar (10)

import random

def generar_colaboradores(num_colaboradores):
    
    cargos = ["Gerente", "Despachador", "Desarrollador", "Diseñador", "Soporte Técnico"]
    
    colaboradores = []

    for i in range(num_colaboradores):
        
        informacion_colaboradores = {

        "id_colaboradora": random.randint(1,500),
        "cargo": random.choice(cargos),
        "cedula": random.randint(10, 15),
        "id_oficina": random.randint(1,500)

        }
        colaboradores.append(informacion_colaboradores)

        return informacion_colaboradores


