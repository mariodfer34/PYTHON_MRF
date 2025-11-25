"""Leer una cadena y eliminar todos los espacios, construyendo una cadena continua."""

cadena = "Hola buenas"
cadena2 = ""

for i in cadena:
    if i != " ":
        cadena2 += i

print(cadena2)