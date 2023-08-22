#==============================================================================

#Sentencias de condicionales simples 

"""   if Condición logica:
            instrucción
            instrucción
            instrucción 
"""

"""
num_uno = 5
if num_uno == 5:
    print("El numero es cinco")
print("Fin.")

"""
"""
print("Vamos a mirar si pasaste el periodo :D")

nombre = input("Antes de comenzar para ver si pasaste tu periodo dame tu nombre: ")

num1 = float(input(nombre + " ¿Cuanto sacaste en biologia?: "))
num2 = float(input(nombre + " ¿Cuanto sacaste en geometria?: "))
num3 = float(input(nombre + " ¿Cuanto sacaste en educacion fisica?: "))

resultado = (num1 + num2 + num3) / 3


if resultado >= 3:
    print("Pasaste :D :  " + nombre + " tu calificación es: ", resultado)
print("Fin.")
"""

#==============================================================================

#Sentencias de Condicionales Compuestas
"""
    if condición logica:
        Instructivo
        Instructivo
    else:
        Instructivo
    
"""
"""
num_uno = 5

if num_uno == 5:
    print("Si es igual :D")
else:
    print("No es el numero D:")

"""
"""

print("Vamos a ver si pasaste inutil :D")

nombre = input("Escribe tu nombre: ")
nota1 = float(input("Cuanto sacaste en el periodo 1: "))
nota2 = float(input("Cuanto sacaste en el periodo 2: "))
nota3 = float(input("Cuanto sacaste en el periodo 3: "))

resultado = (nota1 + nota2 + nota3) / 3


if resultado >= 3.0:
    print("Pasaste :D: ", int(resultado))
    print("Pasaste :D: ", round(resultado,2))                               # PARA TENER UN RESULTADO CON UN APROXIMADO CON CIFRAS ANTES SEÑALIZADOS "round(,"Numero de cifras")"

else:
    print("NooOoOO, no pasaste retrasado mental: ", int(resultado))
    print("NooOoOO, no pasaste retrasado mental: ", round(resultado,1))

print ("Fin.")

"""

#==============================================================================

"""
if condicion logica:
    instruccion
elif condicion logica:
    instruccion
else:
    instruccion
"""
"""
num = int(input("Escribe un numero: "))

if num == 1:
    print("El numero UNO")
elif num ==2:
    print("El numero DOS")
else:
    print("El numero se desconoce :D")
print("Fin.")
"""

print("=========================================")
print("¡¡Convertidor de números a letras!!")
print("=========================================")

num = int(input("Escribe un numero para convertirlo en letras: "))

if num == 1:
    print("El numero es 'UNO'")
elif num == 2:
    print("El numero es 'DOS'")
elif num == 3:
    print("El numero es 'TRES'")
elif num == 4:
    print("El numero es 'CUATRO'")
elif num == 5:
    print("El numero es 'CINCO'")
else:
    print("El numero se desconoce., solo se convierte hasta el numero 5")

print("Fin. ")
"""
"""
print("=================================")
print("Conversor :D")
print("=================================")

print("Numero de opciones 2")
print("Escribe 1 si deseas que el numero sea letras")
print("Escribe 2 si deseas que el la palabra sea numero")

numero = int(input("Escribe un numero :D: "))

if numero == 1:
    
    print("\n CONVERSOR DE NUMEROS A LETRAS \n")
    numero_uno = int(input("ESCRIBE EL NUMERO QUE DESEAS CONVERTIR A LETRAS: "))

    if numero_uno == 1:
        print("El número es 'UNO'. ")
    elif numero_uno ==2:
        print("El número es 'DOS'. ")
    elif numero_uno ==3:
        print("El número es 'TRES'. ")
    elif numero_uno ==4:
        print("El número es 'CUATRO'. ")
    elif numero_uno ==5:
        print("El número es 'CINCO'. ")
    else:
        print("La opcion no esta disponible. ")

elif numero == 2:
    print("\n CONVERSOR DE LETRAS A NUMEROS \n")
    numero_dos = input("Escribe el numero en letras que desea convertir en letras en mayusculas: ")
    numero_dos = numero_dos.lower()     #Esta funcion de ".lower()" se basa para que se pueda alternar entre mayusculas y minusculas 

    if numero_dos == 'uno':
        print("El numero es 1")
    elif numero_dos == 'dos':
        print("El numero es 2")
    elif numero_dos == 'tres':
        print("El numero es 3")
    elif numero_dos == 'cuatro':
        print("El numero es 4")
    elif numero_dos == 'cinco':
        print("El numero es 5")
    else:
        print("La opcion no se encuentra disponible. ")

else:
    print("Opción no disponible")

print("Fin. ")
