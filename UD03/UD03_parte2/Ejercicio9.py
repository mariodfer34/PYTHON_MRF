"""Programa que lea una secuencia de números no nulos hasta que se introduzca un 0, y luego
muestre si ha leído algún número negativo, cuantos positivos y cuantos negativos"""

numero = int(input("Introduce los número que quiera y introduzca 0 para terminar: "))
positivos = 0
negativos = 0

while numero != 0:
    if numero < 0:
        negativos += 1
    else:
        positivos += 1
    numero = int(input())
if negativos > 0:
    print("Se ha introducido uno más números negativos un número negativo")
else:
    print("No se ha introducido ningún número negativo")
print("Se han introducido ", positivos, " números positivos y ",  negativos, " números negativos")