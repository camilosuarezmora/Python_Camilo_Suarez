#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

dicc = {} #crea un diccionario vacio

#pregunta por todos los datos
nombre_ingr = input("Ingresa tu Nombre: ")
dicc["Nombre"] = nombre_ingr

edad_ingr = input("Ingresa tu Edad: ")
dicc["Edad"] = edad_ingr

direccion_ingr = input("Ingresa tu dirección: ")
dicc["Direccion"] = direccion_ingr

tel_ingr = input("Ingresa tu telefono: ")
dicc["Telefono"] = tel_ingr


print({dicc.get("Nombre")}, "tiene", {dicc.get("Edad")}, "años, vive en", {dicc.get("Direccion")}, "y su número de teléfono es", {dicc.get("Telefono")})
