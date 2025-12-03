"""Crea una aplicación que dibuje una pirámide invertida de asteriscos. Nosotros le pasamos
la altura de la pirámide por teclado. Este es un ejemplo"""

asterisco = "*"
espacios = " "

altura = 5
l = altura
contador = 0

for i in range(altura):
    print((espacios * contador), asterisco * ((l * 2) - 1))
    contador += 1
    l -= 1