"""Programa que lee una secuencia de notas (con valores que van de 0 a 10) que termina con
el valor -1 y nos dice si hubo o no alguna nota con valor 10."""

nota = float(input("Introduzca notas del 0 - 10 (introduzca -1 para terminar): "))
boolean = False

while nota != -1:
    if nota == 10:
        boolean = True
    nota = float(input())

if boolean:
    print("Se ha introducido al menos un 10")
else:
    print("No se ha introducido ningún 10")
