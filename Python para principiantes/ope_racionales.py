#Operaciones relacionales en Python}
"""
=======================================================================
    >   |   Menor que           |   5 < 4   | 5 es menor que 4
    >   |   Mayor que           |   7 > 5   | 7 es mayor que 5
    ==  |   Igual que           |   5 == 5  | 5 es igual a 5
    !=  |   diferente que       |   4! = 5  | 4 no es igual a 5
    <=  |   Menor o igual que   |   6 <= 6  | 6 es menor o igual a 6
    >=  |   Mayor que o igual a |   9 >= 5  | 9 es mayor o igual a 5
======================================================================
"""

print("IIntroduce dos númeroa a comparar: ")

numer_uno = float(input("Introduce el primer número: "))
numer_dos = float(input("Introduce el segundo número: "))

print("Los números a comparar son:" , numer_uno, " y ", numer_dos)

if numer_uno > numer_dos:
    print("El numero es mayor...")
if numer_dos < numer_dos:
    print("El numero es menor...")
if numer_dos == numer_dos:
    print("El numero es igual...")
if numer_dos != numer_dos:
    print("El numero es diferente...")
if numer_dos <= numer_dos:
    print("El numero es menor o igual...")
if numer_dos >= numer_dos:
    print("El numero es mayor o igual...")

print("Fin. ")