"""Verificar si un carácter específico está en la cadena con un ciclo y comparaciones."""

caracter = "a"
cadena = "camaleon"
"""cadena = "comaleon"""
verificar = False

for i in range(len(cadena)):
    if cadena[i] == "a":
        verificar = True
if verificar:
    print("La letra seleccionada está en la cadena") 
else:
    print("La letra seleccionada no está en la cadena")
