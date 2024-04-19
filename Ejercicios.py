# Ejercicio 1
cadena = "Hola, mundo!"
numero = 42
lista = [1, 2, 3, 4, 5]
booleano = True

# Ejercicio 2
primeras_tres_letras = cadena[:3]

# Ejercicio 3
primer_elemento = lista[0]

# Ejercicio 4
nuevo_numero = numero + 10

# Ejercicio 5
ultimo_elemento = lista[-1]

# Ejercicio 6
nombres = "harry,alex,susie,jared,gail,conner"
lista_nombres = nombres.split(',')

# Ejercicio 7
primera_palabra = nombres.split(',')[0].upper()
nueva_cadena = primera_palabra + nombres[len(primera_palabra):]

# Ejercicio 8
print(f"El número es: {numero}")

# Ejercicio 9
print("hello world")

# Ejercicio practico externo

# Crear una cadena que contenga la palabra "Hola"
cadena = "¡Hola, mundo! Hola a todos."

# Buscar y seleccionar "Hola" en la cadena
indice_hola = cadena.find("Hola")

# Reemplazar "Hola" con "adiós" en la cadena
nueva_cadena = cadena[:indice_hola] + "adiós" + cadena[indice_hola + len("Hola"):]

print(nueva_cadena)
