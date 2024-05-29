atletismo = {
    "participantes":{}
}

ciclismo = {
    "participantes":{}
}

patinaje = {
    "participantes":{}
}

def menu(): 
    carreras = ("Escribe 1 si participaste en la carrera de atletismo: ", "Escribe 2 si participaste en la carrera de ciclismo: ", "Escribe 3 si participaste en la carrera de patinaje: ", "Escribe 4 para salir: ")

    print("**********")
    print("Elegiste la opción 1, ahora sigue los pasos para registarte")

    edad=int(input("Ingresa el año de tu nacimiento: "))
    depa = input("Ingresa el departamento en el que resides: ")

    if 2024-edad >= 18 and depa.upper() == "SANTANDER":
        print("Puedes continuar")
        for i in carreras:
            print(i)
        carrera_elegida = int(input("Ingresa tu elección: "))  
            
        if (carrera_elegida == 1): 
            recoge_datos(atletismo)
            
        elif (carrera_elegida == 2):
            recoge_datos(ciclismo)
        elif (carrera_elegida == 3):
            recoge_datos(patinaje)
        elif(carrera_elegida == len(carreras)):
            print("Salida exitosa")
        
    else:
        print("No puedes continuar")

    print("****************************")      

def recoge_datos(carrera):
    print("******************************")
    name = input("Ingresa tu nombre: ")
    edad = input("Ingresa tu edad: ") #atrás le había pedido el año de nacimiento, de ahi debería sacar la info de la edad
    doc = input("Ingresa tu documento: ")
    score = float(input("Escribe el tiempo en segundos que sacaste en cada carrera: "))
    usuario_nuevo={}

    usuario_nuevo["Nombre"] = name
    usuario_nuevo["Edad"] = edad
    usuario_nuevo["score"] = score

    carrera["participantes"][doc]= usuario_nuevo
    print("Usuario registrado exitosamente")
    print("****************************")
    print(carrera)

def compara_tiempos(carrera):
    print(carrera["participantes"].keys()) 




print("****** Bienvenido al programa para organizar la carrera gubernamental ******")

while True:
    eleccion = ("Escribe 1 para registrar un usuario: ", "Escribe 2 para conocer el ranking de resultados en la carrera", "Escribe 3 para salir")

    for i in eleccion:
        print(i)

    eleccionprincipal = int(input("Escribe tu elección: "))
    if eleccionprincipal == len(eleccion):
        print("salida exitosa")
        break
    elif eleccionprincipal == 1:
        menu()
    elif eleccionprincipal == 2: 
        print("*********")
        
        menu_ranking_carrera = ("Escribe 1 si quieres conocer el ranking de atletismo", "Escribe 2 si quieres conocer el ranking de ciclismo", "Escribe 3 si quieres conocer el ranking de patinaje")

        for i in menu_ranking_carrera:
            print(i)

        elecc_ranking = int(input("Ingresa aquí el numero del deporte del que quieres conocer el ranking: "))    

        if elecc_ranking == 1:
            compara_tiempos(atletismo)
        elif elecc_ranking == 2:
            compara_tiempos(ciclismo)
        elif elecc_ranking == 3:
            compara_tiempos(patinaje) 
        elif elecc_ranking == len(menu_ranking_carrera):
            print("Salida exitosa")

            

