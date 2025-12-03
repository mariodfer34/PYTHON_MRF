"""Programa que muestre en líneas separadas lo siguiente:
ZYWXVUTSRQPONMLKJIHGFEDCBA, YWXVUTSRQPONMLKJIHGFEDCBA,
WXVUTSRQPONMLKJIHGFEDCBA, ...., DCBA, CBA, BA, A."""

lista = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
longitud = len(lista)
for i in range(longitud):
    print(lista[i:longitud])