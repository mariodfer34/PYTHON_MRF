"""Leer una cadena y contar cuántos caracteres numéricos ('0' a '9') contiene."""

cadena = "Hola234 buenas467"
numeros = "1234567890"
contador = 0


for i in cadena:
    for k in numeros:
        if i == k:
            contador += 1

print(contador)
