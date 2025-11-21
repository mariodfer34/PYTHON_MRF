asterisco = "*"
espacios = " "
altura = int(input("Introduce la altura: "))
k = 1
a = altura

for i in range(altura - 1):
    print((espacios * a) + (asterisco * k))
    k += 2
    a -= 1

for l in range(altura):
    print((espacios * a) + (asterisco * k))

    k -= 2
    a += 1