"""Calcular el perímetro y área de un rectángulo dada su base y su altura."""

base = float(input("Ingresa la base del rectángulo: "))
altura = float(input("Ingresa la altura del rectángulo: "))

perimetro = 2 * (base + altura)
area = base * altura

print("El perímetro del rectángulo es:", perimetro, "y el área es:", area)