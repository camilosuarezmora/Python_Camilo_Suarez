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