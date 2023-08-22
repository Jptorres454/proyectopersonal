# En Python, contamos con tres tipos de operadores lógicos 
"""
=====================================
    Operador Lógico ||  Símbolo     |
=====================================
    Conjución       ||    and       |
    Disyuncion      ||    or        |
    Negación        ||    not       |
=====================================

"""
"""
=========================================================
    |   EJEMPLO     |    AND    |
=========================================================
"""

"""
if num_uno == 5 and num_dos >= 5:
    print("Ambas condiciones se han cumplido")
else:
    print("Una o ambas condiciones no se han cumplido")

"""

"""
=========================================================
    |   EJEMPLO     |    OR    |
=========================================================
"""
"""
if num_ uno == 5 or num_dos >= 5:
    print("Una o ambas condiciones se han cumplido.")
else:
    print("Ninguna condición se ha cumplido. ")

"""
"""
=========================================================
    |   EJEMPLO     |    NOT    |
=========================================================
"""
"""
if not num_dos > 5:
    print("La condicion se invistio y se cumple al ser un numero menor o igual a 5 ")
else:
    print("No se cumple la condicion poruqe el número es mayor a 5.")
"""
#===================================================================
#   Conjunción
#===================================================================

print("Conjunción (AND)")

num_uno = int(input("Escribe un número mayor a 2 y menor a 5:"))

if num_uno > 2 and num_uno < 5:
    print("El número ", num_uno, " cumple con la condicion.\n")
else :
    print("El número ",num_uno," no cumple con la condicion. \n")

#===================================================================
#   Disyuncion
#===================================================================

print("Disyuncion (OR)")

palabra = input("Para cumplir con la condicion escribe 'SI' o 'yes': ")

if palabra == "si" or palabra == "yes":
    print("La condición se han cumplido. \n")
else:
    print("La condicion no se cumple")

#===================================================================
#   Negación
#===================================================================

print("Negación (NOT)")

numero_uno = int(input("Introduce un numero igual a 5: "))

if not numero_uno == 5:
    print("\n El numero es diferente de cinco y si cumple la condición. \n")
else:
    print("\n El numero es igual a cinco y no cumple la condición\n")