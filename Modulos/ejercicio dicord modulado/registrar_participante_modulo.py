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