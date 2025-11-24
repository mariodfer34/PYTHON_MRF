"""Leer una cadena y contar cuántos caracteres son letras mayúsculas."""

cadena = input("Introduce una frase: ")
contador = 0

for i in cadena:
    if i.upper() == i:
        if i != " ":
            contador += 1
print(contador)