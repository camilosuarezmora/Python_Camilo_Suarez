# Escribir un programa que guarde en un diccionario los precios de las verduras de la tabla, pregunte al usuario por una verdura, un número de kilos y muestre por pantalla el precio a pagar. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

#Verdura               Precio (Kg)
#Brócoli                2500 COP
#Pimentón               1250 COP
#Arveja                 3500 COP

#diccionario padre
diccionario = { 
    "Brócoli": "2500 COP",
    "Pimentón": "1250 COP",
    "Arveja": "3500 COP"
}

#Print nombre del local
print("*********** Bienvenido al fruver LA VERDURA PICHA ***********")

#pregunta por la verdura y se almacena en "verdura"
verdura = input("ingresa la verdura que quieres averiguar: ")

#Verifica si la verdura existe con el comando.get
if diccionario.get(verdura, "noExiste") == "noExiste":
    #Si no existe se le notifica al usuario
    print("La verdura que ingresaste no se encuentra almacenada en nuestra base de datos")
else:
    #Si sí existe entonces se le muestra al usuario el precio de la fruta en pantalla, dependiendo el genero de la fruta se le cambia el pronombre.
    if(verdura == "Brócoli" or verdura == "Pimentón"):
        print("El", verdura, "vale", diccionario.get(verdura))  
    else:
        print("La", verdura, "vale", diccionario.get(verdura))     