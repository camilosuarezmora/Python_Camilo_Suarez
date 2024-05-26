# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

info={} #crea el diccionario padre
usuario_nuevo = {} #crea el diccionario del nuevo usuario dentro del diccionario padre
usuario_nuevo["Nombre"] = input("ingresa tu nombre: ") #pide el nombre y lo agrega al diccionario hijo
usuario_nuevo["Edad"] = input("ingresa tu edad: ") #pide la edad y la agrega al diccionario hijo
usuario_nuevo["Sexo"] = input("ingresa tu sexo: ")#pide el sexo y lo agrega al diccionario hijo

cel = input("ingresa tu numero de telefono: ") #pide el telefono y lo agrega a una variable
usuario_nuevo["Telefono"] = cel #la variable que contiene el telefono se agrega al diccionario hijo y más adelante en el diccionario padre

usuario_nuevo["Correo"] = input("ingresa tu correo: ") #pide el correo y lo agrega al diccionario hijo

info[cel] = usuario_nuevo #dentro del diccionario padre crea otro diccionario que almacena cada usuario que se identifica por el numero de telefono
print(info)