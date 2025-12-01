"""Contar cuántas veces aparece un carácter dado en una cadena usando for y un contador."""

cadena = "Patata"
letra = "a"
contador = 0

for i in range(len(cadena)):
    if cadena[i] == letra:
        contador += 1

print("La letra", letra, "aparece", contador, "veces.")