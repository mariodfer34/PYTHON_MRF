"""Escriba un programa que lea tres números y nos diga cual es mayor, cual menor y cuales
son iguales."""

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))


if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        print("Mayor:", num1, "Medio:", num2, "Menor:", num3)
    else:
        print("Mayor:", num1, "Medio:", num3, "Menor:", num2)
elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        print("Mayor:", num2, "Medio:", num1, "Menor:", num3)
    else:
        print("Mayor:", num2, "Medio:", num3, "Menor:", num1)
elif num3 >= num1 and num3 >= num2:
    if num1 >= num2:
        print("Mayor:", num3, "Medio:", num1, "Menor:", num2)
    else:
        print("Mayor:", num3, "Medio:", num2, "Menor:", num1)
if num1 == num2 == num3:
    print("Todos los números son iguales")
