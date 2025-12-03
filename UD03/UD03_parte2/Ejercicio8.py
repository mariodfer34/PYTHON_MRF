"""Programa que lea 100 números no nulos y luego muestre un mensaje indicando cuántos
son positivos y cuantos negativos"""

positivos = 0
negativos = 0

for i in range(100):  
    numero = int(input("Introduce un número no nulo: "))
    if numero < 0:
        negativos += 1
    else:
        positivos += 1
print("Se han introducido ", positivos, " números positivos y ", negativos, " números negativos")