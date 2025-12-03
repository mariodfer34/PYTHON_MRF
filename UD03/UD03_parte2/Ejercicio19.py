"""Programa donde el usuario "piensa" un número del 1 al 100 y el ordenador intenta
adivinarlo. Es decir, el ordenador irá proponiendo números una y otra vez hasta adivinarlo (el
usuario deberá indicarle al ordenador si es mayor, menor o igual al número que ha pensado)"""

minimo = 1
maximo = 100
respuesta = ""
intento = 0
print("Piensa un número del 1 al 100 y yo intentaré adivinarlo")
while respuesta != "igual":
    intento = (minimo + maximo) // 2
    print("El número es:", intento, "?")
    respuesta = input("Introduce si tu número es mayor, menor o igual").lower()
    if respuesta == "mayor":
        minimo = intento + 1
    elif respuesta == "menor":
        maximo = intento - 1
print("He adivinado tu número:", intento)