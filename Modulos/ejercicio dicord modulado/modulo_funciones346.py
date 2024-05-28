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