"""Escriba un programa que lea dos números y lo visualiza en orden ascendente."""

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 > num2:
    print(num1, num2)
else:
    print(num2, num1)