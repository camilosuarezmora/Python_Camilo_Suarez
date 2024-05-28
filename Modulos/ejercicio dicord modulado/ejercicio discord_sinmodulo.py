#Una empresa está organizando la agenda de eventos para el mes de agosto. Por lo tanto requiere un programa que:

# -Permita registrar a los participantes de los eventos de agosto pidiendo: documento, nombre, edad y cargo.
# -Permita registrar los eventos  pidiendo: nombre del evento, locación y día del mes
# -Permita quitar del registro a los participantes .
# -Permita eliminar y/o modificar eventos.

# Para participar los empleados deben cancelar un aporte de 50.000 COP. Por lo tanto el programa también debe:

# -Saber cuantos empleados no han cancelado aún el aporte y cuanto dinero suma la deuda.
# -Saber cuales empleados (listarlos) no han cancelado.
# -No permitir quitar del registro a participantes que ya hayan pagado, pues no se aceptan devoluciones
# -Marcar eventos ya realizados.
# -No permitir eliminar o modificar eventos ya realizados.

# Aspectos a tener en cuenta:
 
# -La estructura a utilizar es libre, solo se pide que sea ordenada y coherente. 
# -Todo debe ser dentro de un menú que se repite para no perder la información y al presionar la opción de salida se debe pedir confirmación de la misma.

import diccionario_eventos #importa todo lo que está en el modulo diccionario_eventos
from registrar_participante_modulo import registrar_participante
import modulo_pagar_participante
from modulo_funciones346 import *
from modulo_ejercicios_7_8_9_10 import *




opc_menu = ("1. Para registrar participante", "2. Para pagar", "3. Para eliminar participante", "4. Para registrar un evento", "5. Para modificar un evento", "6. Para eliminar un evento", "7. Para marcar un evento como completado",
            "8. Para saber cuantos empleados no han cancelado aún el aporte", "9. Para saber cuales empleados (listarlos) no han cancelado.", "10. Para mostrar eventos", "11. Para salir")


while True:
    print("*********************************************************")
    print("Seleccione ->")
    for i in opc_menu:
        print(i)
    opc = int(input("Ingrese la opción deseada: "))
    if opc == len(opc_menu):
        print("Saliendo...")
        break
    elif opc == 1:
        registrar_participante(diccionario_eventos.eventos) #el diccionario que se busca llama de "diccionario eventos" la función que se llame "eventos"
    elif opc == 2:
        modulo_pagar_participante.pagar_participante(diccionario_eventos.eventos)    
    elif opc == 3:
        eliminar_participante(diccionario_eventos.eventos)
    elif opc == 4:
        registrar_evento(diccionario_eventos.eventos)
    elif opc == 5:#Pendiente
        print("pendiente")
    elif opc == 6:
        eliminar_evento(diccionario_eventos.eventos)
    elif opc == 7:
        completar_evento(diccionario_eventos.eventos)
    elif opc == 8:
        saber_cuantos_empleados_no_han_pagado(diccionario_eventos.eventos)
    elif opc == 9:
        saber_cuales_empleados_no_han_pagado(diccionario_eventos.eventos)
    elif opc == 10:
        mostrar_eventos(diccionario_eventos.eventos)
    elif opc == 0:
        print(diccionario_eventos["participantes"])
