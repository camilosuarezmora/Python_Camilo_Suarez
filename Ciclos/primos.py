def primo (num):
    hola = True
    for iterable in range(2, num):
        if (num % iterable == 0):
            return False  
    return(hola)

numi = int(input("escribe un numero"))   
veri=primo(numi)

if (veri):
    print("El número es primo")
else:
    print("El número no es primo")
