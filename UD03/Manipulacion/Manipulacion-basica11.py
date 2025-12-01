"""Construir una nueva cadena con todos los caracteres de la cadena original, pero duplicando cada vocal."""

cadena = "Hola bUenas"
cadena2 = ""
vocales = "aeiou"

for i in cadena:
    for k in vocales:
        if i.lower() == k:
            cadena2 += i
    cadena2 += i
print(cadena2)