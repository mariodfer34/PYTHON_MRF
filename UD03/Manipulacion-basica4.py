"""Construir manualmente una nueva cadena añadiendo un carácter a la vez (ejemplo: filtrar caracteres o construir cadenas invertidas)."""

resultado = ""
letra = input("Inserta una letra y para terminar la cadena inserta 0: ")

while letra != "0":
    if len(letra) > 1:
        print("Pon una sola letra a la vez")
    else:
        resultado += letra
        print(resultado)
    letra = input("ingresa un caracter: ")

print("Tu palabra es: ", resultado)


