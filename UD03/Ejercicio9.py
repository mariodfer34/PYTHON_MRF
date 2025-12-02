asterisco = "*"
espacio = " "

altura = int(input("Introduce la altura de la figura: "))
contador = 6

if altura % 2 == 0:
    print(asterisco * altura)
    for i in range(altura // 2 - 1):
        if altura - contador >= 0:
            print(asterisco + (espacio * (i + 1)) + asterisco + (espacio * (altura - (contador - 1))) + asterisco + (espacio * (i + 1)) + asterisco)
        else:
            print(asterisco + (espacio * (i + 1)) + asterisco + (espacio * (i + 1)) + asterisco)
        contador += 2
        
    print(asterisco + espacio * (altura - 1) + asterisco)
    contador -= 2

    for n in range(altura // 2 - 1):
        if altura - contador >= 0:
            print(asterisco + (espacio * (i + 1)) + asterisco + (espacio * (altura - (contador - 1))) + asterisco + (espacio * (i + 1)) + asterisco)
        else:
            print(asterisco + (espacio * (i + 1)) + asterisco + (espacio * ( i + 1)) + asterisco)
        contador -= 2
        i -= 1
    print(asterisco * altura)
else:
    print(asterisco * altura)
    for i in range(altura // 2 - 1):
        if altura - contador >= 0:
            print(asterisco + (espacio * (i + 1)) + asterisco + (espacio * (altura - contador)) + asterisco + (espacio * (i + 1)) + asterisco)
        else:
            print(asterisco + (espacio * (i + 1)) + asterisco + (espacio * (altura - contador)) + (espacio * (i + 1)) + asterisco)
        contador += 2
        
    print(asterisco + espacio * (altura - 2) + asterisco)
    contador -= 2

    for n in range(altura // 2 - 1):
        if altura - contador >= 0:
            print(asterisco + (espacio * (i + 1)) + asterisco + (espacio * (altura - contador)) + asterisco + (espacio * (i + 1)) + asterisco)
        else:
            print(asterisco + (espacio * (i + 1)) + asterisco + (espacio * (altura - contador)) + (espacio * (i + 1)) + asterisco)
        contador -= 2
        i -= 1
    print(asterisco * altura)