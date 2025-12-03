asterisco = "*"
espacios = " "
altura = int(input("Introduce la altura: "))
k = -1
a = altura

for i in range(altura - 1):
    if i == 0:
        print((espacios * a) + asterisco + (espacios * k))
        k += 2
        a -= 1
    else:
        print((espacios * a) + asterisco + (espacios * k) + asterisco)
        k += 2
        a -= 1

for l in range(altura):
    if l == altura - 1:
        print((espacios * a) + asterisco + (espacios * k))

        k -= 2
        a += 1
    else:
        print((espacios * a) + asterisco + (espacios * k) + asterisco)

        k -= 2
        a += 1