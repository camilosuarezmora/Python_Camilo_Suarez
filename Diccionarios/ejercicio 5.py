#Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total

cesta = {} #diccionario vacio que simula la cesta de la compra
opciones = ("Escribe 1 para Ingresar un nuevo articulo", "Escribe 2 para mostrar el carrito", "Ingresa 3 para salir") #tupla que almacena las opciones
for i in opciones: #recorre la tupla e imprime cada opción
    print(i)
print("********************")
    
while True: #ciclo infito para que yo se lo diga
    eleccion = int(input("Escribe tu eleccion: ")) #se pide la elección y se almacena en la variable "eleccion"
    if eleccion == len(opciones):#si la opción fue la ultima de la lista, termina el programa
        print("Saliendo...")
        break
    elif(eleccion == 1):
        cesta[input("Ingresa el nombre del articulo que deseas ingresar: ")] = input("Ingresa el precio de este producto: ") #pregunta por el precio y el valor y luego lo almacena en el diccionario
    elif(eleccion == 2):
        for clave, valor in cesta.items():
            print(clave, "->", valor)
    else: 
        print("Ingresa solo una de las 3 opciones")