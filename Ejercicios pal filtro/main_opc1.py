print("REGISTRA INGRESOD DE VEHICULO")
import datetime
from datos import *
json_usable = carga_datos("Ejercicios pal filtro//datos//ejemplo.json", "r")
modifica_datos("Ejercicios pal filtro//datos//ejemplo.json", "w", json_usable)

def ingreso():
    x = datetime.datetime.now()
    horaingreso = x.strftime("%H")
    minutosingreso = x.strftime("%M")

    ingreso_en_minutos = (horaingreso*60)+minutosingreso
    return ingreso_en_minutos

def salida():
    x = datetime.datetime.now()
    horasalida = x.strftime("%H") 
    minutossalida = x.strftime("%M")

    salida_en_minutos = (horasalida*60)+minutossalida
    return salida_en_minutos

def lapso():
    lapso = (salida-ingreso)/60

def agrega_vehiculo():
    global ingreso
    global salida
    ingreso = ingreso()
    salida = salida()
    nuevo_vehiculo = {}
    placa = input("Ingresa la placa de tu vehiculo")
    nuevo_vehiculo[placa]["H_Ingreso"] = ingreso()
    nuevo_vehiculo[placa]["H_salida"] = salida()
    nuevo_vehiculo[placa]["lapso"] = lapso()
    return nuevo_vehiculo
    

for dicc_dentro in json_usable: #ingresa dentro de cada diccionario
    dicc_dentro = agrega_vehiculo()
        
        

# import json
# with open("Ejercicios pal filtro//datos//ejemplo.json","r") as dat:
#     data = json.load(dat)
# with open("Ejercicios pal filtro//datos//ejemplo.json", "w")    
# print(data)    