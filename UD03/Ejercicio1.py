altura = int(input("Introduce la altura del rombo: "))

asterisco = "*"
espacio = " "
espacio_interior = " "

k = altura
l = -1
primero = False

for i in range(altura):
    
    if i == 0:
        print((espacio * k) + (asterisco) + (espacio_interior * l))
    else:
        print((espacio * k) + (asterisco) + (espacio_interior * l) + asterisco)
    k -= 1
    l += 1
    primero = True

k = 2
l -= 2
    
for j in range(altura - 1):
    if l < 0:
        print((espacio * k) + asterisco)
    else:
        print((espacio * k) + asterisco + (espacio_interior * l) + asterisco)
    l -= 1
    k += 1