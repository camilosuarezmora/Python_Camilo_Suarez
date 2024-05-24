#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

divisas = {
    'EURO':'€',
    'DOLAR':'$',
    'YEN':'¥'
}

tupla_mensaje = ("Escribe Euro, Dolar o Yen para saber su icono: ")
ingresado = input(tupla_mensaje)


print(divisas.get(ingresado, "La divisa que ingresaste no existe"))

