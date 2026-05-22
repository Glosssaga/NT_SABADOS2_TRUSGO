import requests

def consumo_api_tabla_colaboradores():

    url = "http://localhost:8080/api/colaboradores"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        colaboradores = response.json()
        return colaboradores
    else:
        print(f"Error al consumir la API: {response.status_code}")
        return None