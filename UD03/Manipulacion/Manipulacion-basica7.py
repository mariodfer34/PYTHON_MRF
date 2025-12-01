"""Reemplazar un carácter por otro recorriendo la cadena y concatenando a una nueva cadena."""

cadena = "ejemplo de cadena"
cadena2 = ""
reemplazar = input("Que letra quieres reemplazar?: ")
sustituto = input("Elige la letra sustituta: ")

for i in range(len(cadena)):
    if cadena[i] == reemplazar:
        cadena2 = cadena.replace(reemplazar, sustituto)

print(cadena2)