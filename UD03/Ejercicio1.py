asterisco = "*"
espacios = " "
espacios_dentro = " "
altura = int(input("Introduce la altura: "))
k = -1
a = altura

for i in range(altura - 1):
    if i == 0:
        print((espacios * a) + asterisco + (espacios_dentro * k))
        k += 2
        a -= 1
    else:
        print((espacios * a) + asterisco + (espacios_dentro * k) + asterisco)
        k += 2
        a -= 1
    primeroYultimo = True

for l in range(altura):
    if l == altura - 1:
        print((espacios * a) + asterisco + (espacios_dentro * k))

        k -= 2
        a += 1
    else:
        print((espacios * a) + asterisco + (espacios_dentro * k) + asterisco)

        k -= 2
        a += 1