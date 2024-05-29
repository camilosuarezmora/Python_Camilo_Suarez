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
    while True:
        edad=int(input("Ingresa el año de tu nacimiento: "))
        depa = input("Ingresa el departamento en el que resides: ")

        carreras = ("Escribe 1 si participaste en la carrera de atletismo: ", "Escribe 2 si participaste en la carrera de ciclismo: ", "Escribe 3 si participaste en la carrera de patinaje: ", "Escribe 4 para salir: ")

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
                break
        else:
            print("No puedes continuar")
            break
        

def recoge_datos(carrera):
    name = input("Ingresa tu nombre: ")
    edad = input("Ingresa tu edad: ")
    doc = input("Ingresa tu documento: ")
    score = float(input("Escribe el tiempo en segundos que sacaste en cada carrera: "))
    usuario_nuevo={}

    usuario_nuevo["Nombre"] = name
    usuario_nuevo["Edad"] = edad
    usuario_nuevo["score"] = score

    carrera["participantes"][doc]= usuario_nuevo
    
    print("Usuario registrado exitosamente")
    print("****************************")

def compara_tiempos(carrera):
    print(carrera["participantes"]) 

print("******Bienvenido al programa para organizar la carrera gubernamental ******")
eleccion = ("Escribe 1 para registrar un usuario: ", "Escribe 2 para conocer el ranking de resultados en la carrera", "Escribe 3 para salir")

for i in eleccion:
    print(i)
while True:
    eleccionprincipal = int(input("Escribe tu elección: "))
    if eleccionprincipal == len(eleccion):
        print("salida exitosa")
        break
    elif eleccionprincipal == 1:
        menu()
    elif eleccionprincipal == 2: 
        menu_ranking_carrera = ("Escribe 1 si quieres conocer el ranking de atletismo", "Escribe 2 si quieres conocer el ranking de ciclismo", "Escribe 3 si quieres conocer el ranking de patinaje", "Escribe 1 si quieres conocer el ranking de atletismo")

        elecc_ranking = input("Ingresa el nombre de la carrera a la cual deseas conocer el ranking: ")    
        elecc_ranking.upper()
        if elecc_ranking == "ATLETISMO":
            compara_tiempos(atletismo)
        elif elecc_ranking == "CICLISMO":
            compara_tiempos(ciclismo)
        elif elecc_ranking == "PATINAJE":
            compara_tiempos(patinaje) 
