# Se necesita un aplicativo para controlar y cobrar la tarifa de un parqueadero. Para esto se requiere un menú con las siguientes funcionalidades:

#     ·Registrar entrada con placa (Valor único e identificador)
#     ·Marcar salida para cobrar
#     ·consultar histórico de carros parqueados con hora salida y hora entrada de cada una de las visitas de cada carro y los valores  cobrados.
#     ·Consultar cantidades de dinero recaudado.
#     saber cuales carros se encuentran parqueados en el momento.

# Para que el aplicativo funcione correctamente se debe tener en cuenta:
#     ·El valor de la tarifa por hora o fracción se debe registrar y leer desde un archivo txt o csv.
#     ·El registro de carros, visitas se debe realizar en un archivo tipo json. Para cada carro se deben almacenar todas las visitas que haya hecho con entrada, salida y valor pagado. Además, se debe tener un atributo dedicado a saber si el valor fue pagado o no.

print("  ___                                       _ ")
print(" | _ \ __ _  _ _  __ _  _  _  ___  __ _  __| | ___  _ _  ___ ")
print(" |  _// _` || '_|/ _` || || |/ -_)/ _` |/ _` |/ -_)| '_|/ _ \ ")
print(" |_|  \__,_||_|  \__, | \_,_|\___|\__,_|\__,_|\___||_|  \___/")
print("                    |_|                                      ")

print("=====MENU PRINCIPAL=====")

while True:
    try:
        elecc = int(input("·Ingresa 1 para registrar la entrada del vehiculo.\n·Ingresa 2 para marcar la salida del vehiculo. \n·Ingresa 3 para consultar el historial del parqueadero \n·Escribe 4 para conocer cuanto dinero se ha recaudado\n·Escribe 5 para salir \n >>"))
    except Exception as tipo:
        print(f"hubo un error de tipo {tipo}")

    if elecc == 5:
        print("SALIDA EXITOSA")
        break
    elif elecc == 1:
        import main_opc1 
    elif elecc == 2:
        print("pendiente")       
    elif elecc == 3:
        print("pendiente")
    elif elecc == 4:
        print("pendiente")
    else:
        print("Opción no valida, intenta de nuevo")    

#faltan agergar todas las funcioanlidades
