"""Programa que calcule el valor A elevado a B (A^B) sin hacer uso del operador de potencia
(^), siendo A y B valores introducidos por teclado, y luego muestre el resultado por pantalla"""

A = int(input("Introduce el número que quiere elevar: "))
B = int(input("Introduce a cuanto quiere elevarlo: "))

resultado = 1
resultado = A ** B
print("El resultado de", A, "elevado a", B, "es:", resultado)
