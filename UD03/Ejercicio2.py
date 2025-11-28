asterisco = "*"
espacios = " "
espacios_interiores = " "
altura = int(input("Introduce la altura: "))
resta = 3
partes = altura // 3

for i in range(partes):
    print((espacios * i) + asterisco + (espacios_interiores * ((altura - resta) // 2)) + asterisco + (espacios_interiores * ((altura - resta) // 2)) + asterisco)
    resta += 2
print(asterisco * altura)
for l in range((partes), 0, -1):
    resta -= 2
    print((espacios * (l - 1)) + asterisco + (espacios_interiores * ((altura - resta) // 2)) + asterisco + (espacios_interiores * ((altura - resta) // 2)) + asterisco)