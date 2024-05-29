atletismo = {
    "participantes":{
        "Documento": {"info: carrera, nombre, rango"}
        }
}

ciclismo = {
    "participantes":{
        "Documento": {"info: carrera, nombre, rango"}
        }
}

patinaje = {
    "participantes":{
        "Documento": {"info: carrera, nombre, rango"}
        }
}

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

    


print("******Bienvenido al programa para organizar la carrera gubernamental ******")

edad=int(input("Ingresa el año de tu nacimiento: "))
depa = input("Ingresa el departamento en el que resides: ")

carreras = ("Escribe 1 si participaste en la carrera de atletismo: ", "Escribe 2 si participaste en la carrera de ciclismo: ", "Escribe 3 si participaste en la carrera de patinaje: ")

if 2024-edad >= 18 and depa.upper() == "SANTANDER":
    print("Puedes continuar")
    for i in carreras:
        print(i)
    carrera_elegida = int(input("Ingresa tu elección: "))  
    
    if (carrera_elegida == 1): 
        recoge_datos(atletismo)
        print(atletismo)
        
    elif (carrera_elegida == 2):
        recoge_datos(ciclismo)

    elif (carrera_elegida == 3):
        recoge_datos(patinaje)
else: 
    print("No puedes continuar")

