print("========================================================================")
print("Ejercicio Practico N°3")
print("El numero mas grande")
print("========================================================================")

numero_uno = int(input("Ingrese el primer numero: "))
numero_dos = int(input("Ingrese el segundo numero: "))
numero_tres = int(input("Ingrese el tercer numero: "))

if numero_uno > numero_dos and numero_uno > numero_tres:
    print("El numero ",numero_uno, " es el mas grande de los 3")
elif numero_dos > numero_uno  and numero_dos > numero_tres:
    print("-El numero ",numero_dos, " es el mas grande de los 3")
elif numero_tres > numero_uno and numero_tres > numero_dos:
    print("El numero ", numero_tres," es el mas grande de los 3")

elif numero_uno == numero_dos:
    print("El primer numero ",numero_uno, " y el segundo numero ", numero_dos, " son iguales")
elif numero_dos == numero_tres:
    print("El segundo numero ",numero_dos, " y el tercer numero ", numero_tres, " son iguales")
elif numero_tres == numero_uno:   
    print("El primer numero ",numero_uno, " y el tercer numero ", numero_tres, " son iguales")

    if numero_uno == numero_dos and numero_tres < numero_uno:
        print("El primer numero", numero_uno, " y el segundo numero ", numero_dos, " son los mayores")
    if numero_dos == numero_tres and numero_uno < numero_dos:
        print("El segundo numero", numero_dos, " y el tercer numero ", numero_tres, " son los mayores")
    if numero_uno == numero_tres and numero_dos < numero_uno:
        print("El primer numero", numero_uno, " y el tercer numero ", numero_tres, " son los mayores")

else:
    print("Todos los numeros son iguales :D")