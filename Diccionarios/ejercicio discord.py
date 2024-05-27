#Una empresa está organizando la agenda de eventos para el mes de agosto. Por lo tanto requiere un programa que:

# -Permita registrar a los participantes de los eventos de agosto pidiendo: documento, nombre, edad y cargo.
# -Permita registrar los eventos  pidiendo: nombre del evento, locación y día del mes
# -Permita quitar del registro a los participantes .
# -Permita eliminar y/o modificar eventos.

# Para participar los empleados deben cancelar un aporte de 50.000 COP. Por lo tanto el programa también debe:

# -Saber cuantos empleados no han cancelado aún el aporte y cuanto dinero suma la deuda.
# -Saber cuales empleados (listarlos) no han cancelado.
# -No permitir quitar del registro a participantes que ya hayan pagado, pues no se aceptan devoluciones
# -Marcar eventos ya realizados.
# -No permitir eliminar o modificar eventos ya realizados.

# Aspectos a tener en cuenta:
 
# -La estructura a utilizar es libre, solo se pide que sea ordenada y coherente. 
# -Todo debe ser dentro de un menú que se repite para no perder la información y al presionar la opción de salida se debe pedir confirmación de la misma.

eventos = {
    "participantes": {
        "121312313": {"nombre": "Juan", "Edad": 50, "Cargo": "Contador", "Pago": False},
        "123456789": {"nombre": "Maria", "Edad": 30, "Cargo": "Secretaria", "Pago": True},
        "789456123": {"nombre": "Laura", "Edad": 40, "Cargo": "Ingeniera", "Pago": False}
    },
    "eventos": [
        {"Nombre": "Paseo de olla", "Locacion": "Rio", "Dia": 25, "Hecho": False},
        {"Nombre": "Fiesta del mes", "Locacion": "Salón principal", "Dia": 15, "Hecho": True},
        {"Nombre": "Cumpleaños Jefe", "Locacion": "Oficinas", "Dia": 2,  "Hecho": True}
    ]
}

def registrar_participante(data):
    print("**************************************************")
    participante = {}
    doc = input("Ingrese el documento: ")    
    if data["participantes"].get(doc, None) == None:
        participante["Nombre"] = input("Ingrese el nombre: ")
        participante["Edad"] = int(input("Ingrese la edad: "))
        participante["Cargo"] = input("Ingrese el cargo: ")
        participante["Pago"] = False
        data[doc] = participante
    else:
        print("Participante ya existe!")
    print("**************************************************")

def pagar_participante(data):
    print("**************************************************")
    doc = input("Ingrese el documento: ")
    participante = data["participantes"].get(doc, None)
    if participante != None and participante["Pago"] == False:
        data["participantes"][doc]["Pago"] = True
        print("Pago existoso!")
    else:
        print("Participante no existe o ya pagó!")
    print("**************************************************")

def eliminar_participante(data):
    print("**************************************************")
    doc = input("Ingrese el documento: ")
    participante = data["participantes"].get(doc, None)
    if participante != None and participante["Pago"] == False:
        data["participantes"].pop(doc)
        print("Eliminación existosa!")
    else:
        print("Participante no existe o ya perdió!")
    print("**************************************************")

def registrar_evento(data):
    print("**************************************************")
    evento = {}
    evento["Nombre"] = input("Ingrese el nombre del evento: ")
    evento["Locacion"] = input("Ingrese la locacion del evento: ")
    evento["Dia"] = int(input("Ingrese el dia del evento: "))
    evento["Hecho"] = False
    data["eventos"].append(evento)
    print("Evento registrado")
    print("**************************************************")

def eliminar_evento(data):
    print("**************************************************")
    cont = 1
    print("Ingrese el numero del evento a eliminar ->")
    for i in data["eventos"]:
        print(cont,"-", i["Nombre"], "que será el dia", i["Dia"])
        cont += 1
    opc = int(input("Ingrese su elección: "))
    evento = data["eventos"][opc-1] #Falta validar que el indice sea válido
    if evento["Hecho"] == False:
        data["eventos"].pop(opc-1)
        print("Evento eliminado!!")
    else:
        print("Evento ya realizado, no se puede eliminar!")
    print("**************************************************")

def completar_evento(data):
    print("**************************************************")
    cont = 1
    print("Ingrese el numero del evento a completar ->")
    for i in data["eventos"]:
        print(cont,"-", i["Nombre"], "que será el dia", i["Dia"])
        cont += 1
    opc = int(input("Ingrese su elección: "))
    evento = data["eventos"][opc-1] #Falta validar que el indice sea válido
    if evento["Hecho"] == False:
        data["eventos"][opc-1]["Hecho"] = True
        print("Evento completado!!")
    else:
        print("Evento ya realizado, no se puede completar de nuevo!")
    print("**************************************************")

def saber_cuantos_empleados_no_han_pagado(data):
    print("**************************************************")
    cont = 0
    for valor in data["participantes"].values():
        if valor["Pago"] == False:
            cont += 1
    print("Existen", cont, "Participantes por pagar")
    print("La deuda total es:", cont*50000)
    print("**************************************************")

def saber_cuales_empleados_no_han_pagado(data):
    print("**************************************************")
    print("Los participantes que no han pagado son:")
    for valor in data["participantes"].values():
        if valor["Pago"] == False:
            print("-",valor["nombre"], "que tiene el cargo de",valor["Cargo"])    
    print("**************************************************")

def mostrar_eventos(data):
    print("**************************************************")
    print("Los eventos son:")
    for valor in data["eventos"]:
        print("-",valor["Nombre"], ", con locación",valor["Locacion"], ", el dia", valor["Dia"])    
    print("**************************************************")

opc_menu = ("1. Para registrar participante", "2. Para pagar", "3. Para eliminar participante", "4. Para registrar un evento", "5. Para modificar un evento", "6. Para eliminar un evento", "7. Para marcar un evento como completado",
            "8. Para saber cuantos empleados no han cancelado aún el aporte", "9. Para saber cuales empleados (listarlos) no han cancelado.", "10. Para mostrar eventos", "11. Para salir")


while True:
    print("*********************************************************")
    print("Seleccione ->")
    for i in opc_menu:
        print(i)
    opc = int(input("Ingrese la opción deseada: "))
    if opc == len(opc_menu):
        print("Saliendo...")
        break
    elif opc == 1:
        registrar_participante(eventos)
    elif opc == 2:
        pagar_participante(eventos)    
    elif opc == 3:
        eliminar_participante(eventos)
    elif opc == 4:
        registrar_evento(eventos)
    elif opc == 5:
        print("Modificar evento")#Pendiente
    elif opc == 6:
        eliminar_evento(eventos)
    elif opc == 7:
        completar_evento(eventos)
    elif opc == 8:
        saber_cuantos_empleados_no_han_pagado(eventos)
    elif opc == 9:
        saber_cuales_empleados_no_han_pagado(eventos)
    elif opc == 10:
        mostrar_eventos(eventos)
    elif opc == 0:
        print(eventos["participantes"])
