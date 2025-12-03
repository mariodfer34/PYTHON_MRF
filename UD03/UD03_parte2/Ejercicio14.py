"""Crea una aplicación que dibuje una pirámide de asteriscos. Nosotros le pasamos la altura
de la pirámide por teclado. Este es un ejemplo, si introducimos 5 de altura:"""

asterisco = "*"
espacios = " "

altura = 5
l = altura
contador = 1

for i in range(altura):
    print((espacios * (l - 1)), asterisco * contador)
    l -= 1
    contador += 2