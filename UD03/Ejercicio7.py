asterisco = "*"
espacios = " "
espacios_interiores = " "

altura = int(input("Introduce la altura de  la figura: "))

print(asterisco * altura)

for i in range(altura - 2):
    if i % 2 == 0:
            print((asterisco + espacios) * (altura // 2 + 1) )
    else:
            print(asterisco + (espacios * (altura - 1)) + asterisco)

print(asterisco * altura)