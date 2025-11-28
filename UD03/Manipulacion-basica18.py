"""Leer una cadena y construir una nueva cadena dejando sólo los caracteres que son consonantes (sin listas, usando condiciones y concatenación)."""

cadena = "Hola, soy Mario"
resultado = ""

for i in cadena:
    if i != "a" and i != "e" and i != "i" and i != "o" and i != "u":
        resultado += i
print(resultado)