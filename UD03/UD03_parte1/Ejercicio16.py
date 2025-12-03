"""Escriba un programa que pida un número entre 0 y 99999, y que diga cuantas cifras tiene."""

num = float(input("Ingresa un número entre 0 y 99999: "))
cifras = 0

while num >= 1 and num <=99999:
    num /= 10
    cifras += 1

print("El número tiene: ", cifras, "cifras")
