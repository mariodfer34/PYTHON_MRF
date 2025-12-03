"""Programa que lea 100 números no nulos y luego muestre un mensaje de si ha leído algún
número negativo o no."""

boolean = False
for i in range(100):  
    numero = int(input("Introduce un número no nulo: "))
    if numero < 0:
        boolean = True
if boolean:
    print("Se ha introducido uno más números negativos un número negativo")
else:
    print("No se ha introducido ningún número negativo")
