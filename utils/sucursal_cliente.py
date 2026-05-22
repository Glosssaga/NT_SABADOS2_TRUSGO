import random


def generar_sucursal_cliente(numero_sucursales):

    nombres  = ["Sucursal Norte", "Sucursal Sur", "Sucursal Este", "Sucursal Oeste", "Sucursal Central"]
    direcciones = ["Calle 123 #45-67", "Avenida 456 #78-90", "Carrera 789 #12-34", "Calle 321 #54-76"]
    telefonos   = ["6011234567", "6027654321", "6039876543", "6041234567"]
    activos     = ["true", "false"]

    sucursales = []

    for i in range(numero_sucursales):
        sucursal = {
            "id_sucursal"      : f"SUC{str(i + 1).zfill(3)}",
            "nombre_sucursal"  : random.choice(nombres),
            "direccion_sucursal": random.choice(direcciones),
            "telefono_sucursal": random.choice(telefonos),
            "activo"           : random.choice(activos)
        }

        probabilidad = random.random()

        if probabilidad < 0.1:
            sucursal["id_sucursal"]       = random.choice([None, "", "0"])
            sucursal["nombre_sucursal"]   = None
        elif probabilidad < 0.3:
            sucursal["nombre_sucursal"]   = " " + sucursal["nombre_sucursal"] + " "
        elif probabilidad < 0.6:
            sucursal["direccion_sucursal"] = sucursal["direccion_sucursal"].upper()
        elif probabilidad < 0.8:
            sucursal["telefono_sucursal"] = f"60{random.randint(1000000, 9999999)}"

        sucursales.append(sucursal)

    return sucursales