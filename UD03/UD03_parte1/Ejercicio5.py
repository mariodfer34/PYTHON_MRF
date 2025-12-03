"""Escriba un programa que toma como dato de entrada un número que corresponde a la
longitud de un radio (La longitud del radio es la mitad de la del diámetro) y nos escribe la longitud
de la circunferencia (La longitud de una circunferencia es igual a pi por el diámetro), el área del
círculo (El área de un círculo es pi multiplicado por el radio al cuadrado) y el volumen de la esfera
que corresponde con dicho radio."""

radio = float(input("Ingrese el radio del círculo: "))
cirunferencia = (2 * radio) * 3.14
area = 3.14 * (radio ** 2)
volumen = (4/3) * 3.14 * (radio ** 3)
print("La longitud de la circunferencia del círculo es:", cirunferencia, ", el área del círculo es:", area, " y el volumen de la esfera es:", volumen)