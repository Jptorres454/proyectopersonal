# inicio para realizar una cadena de caracteres

print("========================================")
mensaje="hola"
mensaje+=" "
mensaje+="Soy batman"
print(mensaje)

print("========================================")
print("Concatenación: ")
mensaje="hola"
espacio=" "
nombre="Soy batman"
print(mensaje + espacio + nombre)

print("========================================")
numero_1 = 7
numero_2 = 5
resultado = numero_1 + numero_2
resultado = str(resultado)
print("El resultado es: " + resultado)

print("========================================")
print("Busqueda: ")
mensaje = "Hola soy Batman"
buscar_subcadena= mensaje.find("Batman")
print(buscar_subcadena)

print("========================================")
mensaje = "Soy Batman"
extraer_subcadena = mensaje[5:7]
print(extraer_subcadena)

print("========================================")
mensaje_1="Hola soy Batman"
mensaje_2="Hola soy Batman"
print(mensaje_1 == mensaje_2)