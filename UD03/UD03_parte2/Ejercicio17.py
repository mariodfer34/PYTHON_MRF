"""Programa que suma independientemente los pares y los impares de los números
comprendidos entre 100 y 200, y luego muestra por pantalla ambas sumas."""

pares = 0
impares = 0

for i in range(100, 201):
    if i % 2 == 0:
        pares += i
    else:
        impares += i
print("la suma de los pares es:", pares, "la suma de los impares es:", impares)