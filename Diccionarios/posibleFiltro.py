def registrar_usuario(data):
    print("**************************************************")
    data = dict(data)
    usuario = {}
    doc = input("Ingrese el documento: ")    
    if data.get(doc, None) == None:
        usuario["Nombre"] = input("Ingrese el nombre: ")
        usuario["Edad"] = int(input("Ingrese la edad: "))
        data[doc] = usuario #crea un usuario nuevo dentro del diccionario
    else:
        print("Usuario ya existe!")
    print("**************************************************")
    return data

def mostrar_usuarios(data):
    print("**************************************************")
    data = dict(data) # estar seguro que el siccionario ingresado es un diccionario
    for clave, valor in data.items(): #data.items() -> separa un diccionario en key y value, estos se colocan en el for 
        print("Nombre:", valor["Nombre"], ", Edad:", valor["Edad"], ", Documento: ", clave)
    print("**************************************************")

def mostrar_usuario(data):
    print("**************************************************")
    data = dict(data)
    documento = input("Ingrese el documento a buscar: ")
    usuario = data.get(documento, None)
    if  usuario == None:
        print("Usuario no existe!")
    else:
        print("Nombre:", usuario["Nombre"], ", Edad:", usuario["Edad"], ", Documento: ", documento)
    
    print("**************************************************")
    
    
usuarios = {
    "10989979": {"Nombre": "Juan", "Edad": 20},
    "10989279": {"Nombre": "Maria", "Edad": 20},
}

opcionsales_menu = ("1. Para registrarse", "2. Para mostrar todos los usuarios", "3. Para mostrar un solo usuario", "4. Para ir")

while True:
    print("*********************************************************")
    print("Seleccione ->")
    for i in opciones_menu:
        print(i)
    opc = int(input("Ingrese la opción deseada: "))
    
    if opc == len(opciones_menu):
        print("Saliendo...")
        break
    elif opc == 1:
        usuarios = registrar_usuario(usuarios)
    elif opc == 2:
        mostrar_usuarios(usuarios)
    elif opc == 3:
        mostrar_usuario(usuarios)
        
        