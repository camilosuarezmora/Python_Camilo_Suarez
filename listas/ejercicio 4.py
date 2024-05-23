#Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas

lista = [] #declara lista vacia


for i in range(1,11,1): #imprime los numeros del 1 al 10
    lista.append(i) #agrega estos numeros nuevos a la lista

lista.reverse() #le da vuelta a la  lista


print(lista) #imprime lista

