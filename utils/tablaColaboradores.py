import random


def generar_colaboradores(num_colaboradores):

    cargos   = ["Gerente", "Despachador", "Desarrollador", "Diseñador", "Soporte Técnico"]
    nombres  = ["Carlos", "Maria", "Juan", "Ana", "Pedro", "Laura", "Luis", "Sofia", "Jorge", "Diana"]
    activos  = ["true", "false"]

    colaboradores = []

    for i in range(num_colaboradores):

        colaborador = {
            "id_colaborador"    : f"COL{str(i + 1).zfill(3)}",
            "nombre_colaborador": random.choice(nombres),
            "cargo"             : random.choice(cargos),
            "telefono"          : f"60{random.randint(10000000, 99999999)}",
            "activo"            : random.choice(activos)
        }

        # Inyectando errores controlados
        probabilidad = random.random()

        if probabilidad < 0.1:
            colaborador["id_colaborador"]     = random.choice([None, "", "0"])
            colaborador["cargo"]              = None
        elif probabilidad < 0.3:
            colaborador["nombre_colaborador"] = " " + colaborador["nombre_colaborador"] + " "
        elif probabilidad < 0.6:
            colaborador["cargo"]              = colaborador["cargo"].upper()
        elif probabilidad < 0.8:
            colaborador["telefono"]           = f"60{random.randint(1000000, 9999999)}"

        colaboradores.append(colaborador)

    return colaboradores