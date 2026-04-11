import random
from datetime import datetime, timedelta


def simular_oficinas(numero_oficinas):
    nombres_oficina = [
        "Oficina Central",
        "Sucursal Norte",
        "Sucursal Sur",
        "Sucursal Este",
        "Sucursal Oeste",
        "Oficina Principal",
        "Oficina Secundaria",
        "Oficina Regional",
        "Oficina Local",
        "Oficina de Ventas"
    ]
    direcciones = [
        "Calle 123 #45-67",
        "Avenida 456 #78-90",
        "Carrera 789 #12-34",
        "Calle 321 #54-76",
        "Avenida 654 #87-09",
    ]
    departamentos = [
        "Antioquia",
        "Cundinamarca",
        "Valle del Cauca",
        "Atlántico",
        "Santander",    
    ]
    ciudades = [
        "Medellín",
        "Bogotá",
        "Cali",
        "Barranquilla",
        "Bucaramanga",
    ]

    fecha_inicial = datetime(2010, 1, 1)
    oficinas = []

    for _ in range(numero_oficinas):
        fecha_simulada = fecha_inicial + timedelta(days=random.randint(0, 3650))
        oficina = {
            "id_oficina"   : random.randint(1, 9999),
            "nombre_oficina": random.choice(nombres_oficina),
            "direccion"    : random.choice(direcciones),
            "departamento" : random.choice(departamentos),
            "ciudad"       : random.choice(ciudades),
            "telefono"     : f"60{random.randint(10000000, 99999999)}",
            "fecha_apertura": fecha_simulada.strftime("%Y/%m/%d"),
        }
        # Inyectando errores controlados 
        probabailidadError=random.random()
        if probabailidadError<0.1:
            oficina["id_oficina"]=random.choice([None,-1,0])
        elif probabailidadError<0.3:
            oficina["nombre_oficina"]=" "+oficina["nombre_oficina"]+" "
        elif probabailidadError<0.6:
            oficina["ciudad"]=oficina["ciudad"].upper()
        elif probabailidadError<0.9:
            oficina["fecha_apertura"]=None
        elif probabailidadError<0.95:
            oficina["telefono"]=f"60{random.randint(1000000, 9999999)}"
        elif probabailidadError<0.98:
            oficina["direccion"]=oficina["direccion"].lower()
        elif probabailidadError<0.99:
            oficina["departamento"]=oficina["departamento"].upper()

        oficinas.append(oficina)

    return oficinas

