print("Calculadora con una sola variable")

print("""
*************************
|   Menú de opciones    |
*************************
1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Division entera
6. Exponente 
7. Modulo 
""")

factor = int(input("Introduce la opción deseada: "))
numero_uno = int(input("Introduce el primer número: "))
numero_dos = int(input("Introduce el segundo número: "))

if factor == 1:
    
    print("Elegiste SUMA ")
    numero_uno += numero_dos
    print("Su resultado es: ", numero_uno)

elif factor == 2:
    
    print("Elegiste RESTA")
    numero_uno -= numero_dos
    print("Su resultado es: ", numero_uno)

elif factor == 3:

    print("Elegiste MULTIPLICACION")
    numero_uno *= numero_dos
    print("Su resultado es: ", numero_uno)

elif factor == 4:

    print("Elegiste DIVISION")
    numero_uno /= numero_dos
    print("Su resultado es: ", round(numero_uno, 2))

elif factor == 5:

    print("Elegiste DIVISION ENTERA")
    numero_uno //= numero_dos
    print("Su resultado es: ", numero_uno)

elif factor == 6:

    print("Elegiste EXPONENTE")
    numero_uno **= numero_dos
    print("Su resultado es: ", numero_uno)

elif factor == 7:

    print("Elegiste MODULO")
    numero_uno %= numero_dos
    print("Su resultado es: ", numero_uno)

print("Fin.")