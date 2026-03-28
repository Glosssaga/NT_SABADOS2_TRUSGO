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
        oficinas.append(oficina)

    return oficinas
