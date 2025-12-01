"""Leer una cadena y crear una nueva donde sólo aparezcan los caracteres que se repiten más de una vez."""

cadena = "Hola, soy Mario"
cadena2 = ""
resultado= ""
contador = 0

for i in cadena:
    if cadena.count(i) > 1 and i != " ":
        resultado += i
print(resultado)