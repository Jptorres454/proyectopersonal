print("============================================")
print("\n Ejercicio Practico N°1 \n")
print("Sistema Control Vacacional ")
print("============================================")

nombre = input("Digita tu nombre: ")

print("========================================================================")
print("Las opciones de clave son: ")
print("Gerencia marque 1.")
print("Logistica marque 2.")
print("Gerencia marque 3.")
print("========================================================================")

clave = int(input("Digite el numero: de clave que corresponde: "))
print("========================================================================")
años = float(input("Digite los años en los que ha trabajado: "))

if clave == 1:

    if clave == 1 and clave < 2:
        print("El empleado ", nombre, " tiene derecho a 6 dias de vacaciones.")
    elif clave >= 22 and clave <= 6:
        print("El empleado ", nombre, " tiene derecho a 14 dias de vacaciones.")
    elif clave >= 7:
        print("El empleado ", nombre, " tiene derecho a 20 dias de vacaciones.")
    else:
        print("El empleado ", nombre, " aun no tiene derecho a vacaciones.")

elif clave == 2:

    if clave == 1 and clave < 2:
        print("El empleado ", nombre, " tiene derecho a 7 dias de vacaciones.")
    elif clave >= 22 and clave <= 6:
        print("El empleado ", nombre, " tiene derecho a 15 dias de vacaciones.")
    elif clave >= 7:
        print("El empleado ", nombre, " tiene derecho a 22 dias de vacaciones.")
    else:
        print("El empleado ", nombre, " aun no tiene derecho a vacaciones.")

elif clave == 3:

    if clave == 1 and clave < 2:
        print("El empleado ", nombre, " tiene derecho a 10 dias de vacaciones.")
    elif clave >= 22 and clave <= 6:
        print("El empleado ", nombre, " tiene derecho a 20 dias de vacaciones.")
    elif clave >= 7:
        print("El empleado ", nombre, " tiene derecho a 30 dias de vacaciones.")
    else:
        print("El empleado ", nombre, " aun no tiene derecho a vacaciones.")

else:
    print("La clave de departamento no existe, vuelve a intentarlo.")
print("========================================================================")
print("Fin. ")