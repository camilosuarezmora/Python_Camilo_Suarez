#Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

li = [50, 75, 46, 22, 80, 65, 8] # crea la listya con los valores indicados.
li.sort() #organiza de primero al ultimo

print(f"El primer elemento de la lista es:  {li[0]}")# imprime el primer elemento de la lista "li" que se encuentre en posición cero [0]
contador = 0 #inicializa variable contador
for i in li: #recorre la lista
    contador += 1 #busca la posición de cada elemento
    maximo = contador
print(f"El ultimo elemento del la lista es: {li[maximo-1]}")