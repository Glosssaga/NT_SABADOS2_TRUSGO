import random
from datetime import datetime, timedelta


def generar_sucursal_cliente(numeroClientes):

    listaClientes = ["Farmatodo", "Copidrogas", "Drogas la rebaja", "Drogueria pepos"]
    codigosClientes = ["FAR01", "COP02", "REB03", "PEP04"]
    ciudades = ["Medellín", "Bogotá", "Cali", "Cartagena"]
    direcciones = ["Calle 123", "Avenida 456", "Carrera 789", "Transversal 321"]
    clientes = []

    fechaInicial = datetime(2023, 1, 1)
    for i in range(numeroClientes):
        cliente = {
            "id_sucursal": random.choice(listaClientes) + str(i),
            "id_cliente": random.randint(0, 1000000),
            "direccion": random.choice(direcciones),
            "departament": codigosClientes[i % len(codigosClientes)],
            "ciudad": random.choice(ciudades),
            "contacto": random.choice(listaClientes),
            "codigo_casa_mx": random.randint(100000, 999999),
        }
        clientes.append(cliente)
    return clientes
