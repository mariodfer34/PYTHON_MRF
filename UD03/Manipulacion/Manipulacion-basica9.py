"""Leer una cadena y contar cuántas vocales contiene."""

cadena = input("Introduce una frase: ")
vocales = "aeiou"
contador = 0

for i in range (len(cadena)):
    for k in range (len(vocales)):
        if cadena[i].lower() == vocales[k]:
            contador += 1
print(contador)