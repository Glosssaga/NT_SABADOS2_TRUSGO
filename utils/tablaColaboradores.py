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
            "id_colaboradora": random.randint(1, 500),
            "cargo": random.choice(cargos),
            "cedula": str(random.randint(1000000000, 9999999999)),
            "id_oficina": random.randint(1, 500)
        }

        # Inyectando errores controlados
        probabilidadError = random.random()

        if probabilidadError < 0.1:
            informacion_colaboradores["id_colaboradora"] = random.choice([None, -1, 0])
            informacion_colaboradores["cargo"] = None
            informacion_colaboradores["cedula"] = "invalid_cedula"

        elif probabilidadError < 0.3:
            informacion_colaboradores["id_oficina"] = " " + str(informacion_colaboradores["id_oficina"]) + " "  # inyectamos espacios

        elif probabilidadError < 0.6:
            informacion_colaboradores["cedula"] = informacion_colaboradores["cedula"].upper()  # inyectamos cedula en mayúsculas

        colaboradores.append(informacion_colaboradores)

    return colaboradores
