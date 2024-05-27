#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

divisas = { #Dicioario que almacena las divisas
    'EURO':'€', 
    'DOLAR':'$',
    'YEN':'¥'
}

tupla_mensaje = ("Escribe Euro, Dolar o Yen para saber su icono: ") #da las opciones
ingresado = input(tupla_mensaje) #busca por la divisa dentro del diccionario

print(divisas.get(ingresado, "La divisa que ingresaste no existe")) #Inprime lo que encontro, si existe lo muestra y si no muestra el mensaje

