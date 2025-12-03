asterisco = "*"
espacios = " "

contador = 1
altura = int(input("Introduce la altura de la figura"))

print(asterisco * altura)
for i in range(altura // 2):
    if contador < altura - 3:
        print(asterisco + (espacios * contador) + asterisco + (espacios * (altura - contador - 3)) + asterisco)
    contador += 1
contador -= 2
for l in range(altura // 2 - 1):
    print(asterisco + (espacios * contador) + asterisco + (espacios * (altura - contador - 3)) + asterisco)
    contador -= 1
print(asterisco * altura)