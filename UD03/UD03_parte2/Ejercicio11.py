"""Crea una aplicación que dibuje una escalera de asteriscos. Nosotros le pasamos la altura de
la escalera por teclado. Este es un ejemplo si insertaras un 5 de altura:"""

asterisco = "*"
altura = int(input("Introduce la altura de la escalera: "))
for i in range(altura + 1):
    print(asterisco * i)