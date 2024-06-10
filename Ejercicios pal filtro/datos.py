import json
def carga_datos(ruta, modo):
    with open(ruta, modo) as data:
        data_abierta = json.load(data)
    return data_abierta    

def modifica_datos(ruta, modo, retorno_anterior):
    with open(ruta, modo) as datico:
        json.dump(retorno_anterior, datico, indent=4)