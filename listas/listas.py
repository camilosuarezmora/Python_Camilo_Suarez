#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

asignaturas = [] #lista vacía que va a almacenar las asignaturas

while True: #cilo infinto
    ingresada = input("Escribe tus asignaturas: ") # ingresa la asignatura
    if(ingresada == ""): #si no ingresa nada se acaba el ciclo
        print("FIN")
        break
    else: # si ingresa cualquier cosa, esta se agrega a la lista
        asignaturas.append(ingresada) #almacena la asiganción
print(asignaturas)
