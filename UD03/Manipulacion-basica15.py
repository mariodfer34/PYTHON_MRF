"""Dada una cadena, construir una nueva cadena donde cada vocal se reemplaza por un asterisco '*'."""

cadena = "Hola buenas"
vocales = "aeiou"

for i in cadena:
    for k in vocales:
        if i.lower() == k:
            cadena = cadena.replace(k, "*")
print(cadena)