def registrar_usuario(data): #Función para crear un nuevo usuario y almacenarlo en el diccionario padre "usuarios"
    print("**************************************************")
    data = dict(data) #verifica que lo que se ingresa es un diccionario
    usuario = {} #crea un diccionario para el usuario nuevo, si no hay usuario nuevo, este no se guarda
    doc = input("Ingrese el documento: ") #Almacena el documento UNICO del usuario 
    if data.get(doc, None) == None: #si cuando busca el usuario "doc" dentro del diccionario de usuario no lo encuentra, crea un nuevo usuario
        usuario["Nombre"] = input("Ingrese el nombre: ") #ingresa el nombre del usuario y lo almacena en el diccionario creado para cada persona, en la sección "Nombre". todo esto dentro del diccionario general "Usuarios". 
        usuario["Edad"] = int(input("Ingrese la edad: "))#ingresa la edad del usuario y lo almacena en el diccionario creado para cada persona, en la sección "Edad". todo esto dentro del diccionario general "Usuarios".
        data[doc] = usuario #crea un usuario nuevo dentro del diccionario
    else: #si se encuentra el usuario dentro de la base de datos entonces existe y notifica al usuario que ya existe.
        print("Usuario ya existe!")
    print("**************************************************")
    return data #devuelve el nuevo diccionario

def mostrar_usuarios(data): #función para mostrar todos los usuarios almacenados en el diccionario padre "usuarios"
    print("**************************************************")
    data = dict(data) # cerciorarse que el diccionario ingresado es un diccionario
   
    #for KEY_DEL_DICCIONARIO_PADRE, VALUE_DEL_DICCIONARIO_PADRE in DICCIONARIO_PADRE.items() 
    for clave, valor in data.items(): #data.items() -> separa un diccionario en key y value, estos se colocan en el for 
        print("Nombre:", valor["Nombre"], ", Edad:", valor["Edad"], ", Documento: ", clave) #imprime el diccionario con todos los datos disponibles
    print("**************************************************")

def mostrar_usuario(data): #función para mostrar un usuario en especifico dentro del diccionario padre "usuarios"
    print("**************************************************")
    data = dict(data) #"convierte el diccionario ingresado a diccionario para cerciorarse"
    documento = input("Ingrese el documento a buscar: ") #ingresa el documento  y lo almacena en documento
    usuario = data.get(documento, None) #Busca el documento del usuario ingresado dentro del diccionario padre 
    if  usuario == None: #si no encuentra el usuario muestra en pantalla que no existe
        print("Usuario no existe!")
    else: #si sí encuentra el usuario ingresado, muestra el los datos de ese usuario
        print("Nombre:", usuario["Nombre"], ", Edad:", usuario["Edad"], ", Documento: ", documento)
    
    print("**************************************************")
    
#crea el diccionario "usuarios", donde cada usuario es un diccionario nuevo.    
usuarios = { 
   # key:       value         
    "10989979": {"Nombre": "Juan", "Edad": 20},
                # key:     value,   key:    value
    "10989279": {"Nombre": "Maria", "Edad": 20},
}

#tupla para almacenar el menú
opciones_menu = ("1. Para registrarse", "2. Para mostrar todos los usuarios", "3. Para mostrar un solo usuario", "4. Para ir")

while True: #ciclo while para que muestre el menú y ejecute la opcion de cada menú hasta que se le indique que pare
    print("*********************************************************")
    print("Seleccione ->")
    for i in opciones_menu: #recorre el menú y lo muestra al usuario
        print(i)
    opc = int(input("Ingrese la opción deseada: ")) #Lee la opcion del usuario y lo almacena en "opc"
    
    if opc == len(opciones_menu): #si se seleccionó la ultima opcion del menú se sale y se acaba el ciclo
        print("Saliendo...")
        break
    elif opc == 1: #si eligió la opción 1, se ejecutara la función "registrar_usuarios()"  con el parametro "usuarios"  que hace referencia al primer diccionario.
        usuarios = registrar_usuario(usuarios) #Al ejecutar la función esta va a        devolver el diccionario con el nuevo usuario ingresado, y se almacena en el antiguo diccionario.
    elif opc == 2:
        mostrar_usuarios(usuarios) #si se elige la opcioón 2, entonces se ejecuta la función "mostrar_usuarios()", que devuelve el diccionario con la info de todos los usuarios.
    elif opc == 3:
        mostrar_usuario(usuarios) #si se elige la opción 3, entonces se ejecuta la función "mostar_usuario()", que devuelve la info de un usuario en especifico.
        
        