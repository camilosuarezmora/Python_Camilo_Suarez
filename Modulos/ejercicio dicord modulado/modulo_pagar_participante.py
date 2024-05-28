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