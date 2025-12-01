"""Leer dos cadenas y concatenarlas manualmente sin usar el operador + en una sola operación (concatenar carácter a carácter con un ciclo)."""

cadena1 = "Hola, soy Mario"
cadena2 = ", tengo 21 años"
cadena3 = ""

for i in cadena1:
    cadena3 += i
for k in cadena2:
    cadena3 += k

print(cadena3)