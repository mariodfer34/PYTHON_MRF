"""Escriba un programa que lea dos números, calcule y muestre el valor de sus suma, resta,
producto y división (Ten en cuenta la división por cero)."""

num1 = 5
num2 = 10

suma = num1 + num2
resta = num1 - num2
producto = num1 * num2
if num2 != 0:
    division = num1 / num2
else:
    division = "Error: División por cero"
    
print("Suma:", suma, "Resta:", resta, "Producto:", producto, "División:", division)