"""Convertir todas las letras a mayúsculas o minúsculas usando ciclos y sumas de caracteres (sin usar los métodos upper() o lower())."""

cadena2 = ""
cadena = "Hola Putita"
mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnñopqrstuvwxyz"
contador = 0

for i in (cadena):
    if i == " ":
        cadena2 += i
    for ma in (mayusculas):
        if i == ma:
            cadena2 += minusculas[contador]
        contador += 1
    contador = 0
    for mi in (minusculas):
        if i == mi:
            cadena2 += mayusculas[contador]
        contador += 1
    contador = 0
print(cadena2)