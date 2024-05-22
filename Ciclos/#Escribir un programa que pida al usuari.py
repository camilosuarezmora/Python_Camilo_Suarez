#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
num1 = float(input("Escribe el dividendo de tu división "))
num2 = float(input("Escribe el divisor de tu división "))
division = num1 / num2 
if(num2 == 0):
    print("ERROR")
else:
    print(division)
