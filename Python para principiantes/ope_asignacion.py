#ASIGNACION LDE OPERADORES ASIGNACION

"""

    |   Tipo de Asignaciones    |   Simbologia      |   Implementación  |   Expresión equivalente   |
    =================================================================================================
    |        Asignacion         |        =          |       x = y       |          x = y            |
    |          Suma             |       +=          |       x += y      |         x = x + y         |
    |          Resta            |       -=          |       x -= y      |         x = x - y         |
    |      Multiplicacion       |       *=          |       x *= y      |         x = x * y         |
    |         Division          |       /=          |       x /= y      |         x = x / y         |
    |     Division Entera       |      //=          |       x //= y     |         x = x // y        |
    |         Exponente         |      **=          |       x **= y     |         x = x ** y        |
    |     Modulo o Resto        |       %=          |       x %= y      |         x = x % y         |

"""

"""

    |   Tipo de Asignaciones    |   Simbologia      |   Implementación  |
    =====================================================================
    |        Asignacion         |        =          |       x = y       |
    |          Suma             |       +=          |       x += y      |
    |          Resta            |       -=          |       x -= y      |
    |      Multiplicacion       |       *=          |       x *= y      |
    |         Division          |       /=          |       x /= y      |
    |     Division Entera       |      //=          |       x //= y     |
    |         Exponente         |      **=          |       x **= y     |
    |     Modulo o Resto        |       %=          |       x %= y      |


"""
"""

mensaje = "Hola"
mensaje += " Soy Batman"

numero = 5
numero += 3

print(mensaje, " tu numero es ", numero)

"""

nombre = ("Hola ")
nombre += input("Escribe tu nombre: ")
print( nombre, ", Esto es el incremento y decremento de una variable ")

print("============================================================")
print("INCREMENTO O AUMENTO :")
x = 1
print("Valor inicial: ", x)

x += 2
x += 2
x += 2
x += 2
x += 2

print("Valor final: ", x)

print("DECREMENTO O DISMINUCION: ")
print("Valor inicial: ", x)
x -= 1
x -= 1
x -= 1
x -= 1
x -= 1

print("Valor final 2: ", x)