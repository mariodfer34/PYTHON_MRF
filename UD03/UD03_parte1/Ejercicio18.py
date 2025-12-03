"""Escriba un programa que pida un número por teclado y diga si dicho número es múltiplo de
10."""


num = int(input("Ingrese un número: "))
if num % 10 == 0:
    print("El número es múltiplo de 10")
else:
    print("El número no es múltiplo de 10")