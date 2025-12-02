asterisco = "*"
espacios = " "
espacios_interiores = " "
altura = int(input("Introduce la altura: "))
resta = 1
suma = -1

for i in range(altura):
    if i == 0:
        print((espacios * (altura - resta)) + asterisco)
    elif i == altura - 1:
        print(((asterisco * (altura - 1) * 2)) + asterisco)
    elif i == ((altura // 2)):
        print((espacios * (altura - resta)) +  ((asterisco + espacios) * (i + 1)))
    else:
        print((espacios * (altura - resta)) + asterisco + (espacios_interiores * suma) + asterisco)
    resta += 1
    suma += 2

