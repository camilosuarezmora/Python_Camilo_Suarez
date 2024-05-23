#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
#almacena asignaturas.

#por cada asiganura pregunta las notas
#elimina de la lista de asignaturas las materias que aprobó
#mostrar las nueva lista de repetir

asignaturas = [] #crea lista de asignaturas
print("ingresa las asignaturas que cursas y deja un espacio vacio para dejar de escribir ")#mensaje
contador = 1 #para saber que asignatura puso
while True: 
    asig_nueva = input(f"Ingresa la asignatura {contador}: ") #pide la nueva asignatura
    if (asig_nueva == ""): #termina el ciclo y no pide más asignaturas
        break
    else:
        asignaturas.append(asig_nueva) # ingresa la asignatura en la lista
        
    contador += 1

print(f" Ingresaste las asignaturas: {asignaturas}") #muestra las asignaturas que escribió

for i in range(len(asignaturas)):
    asignaturas[i] =  
