dinero = int(input("cuanto dinero quieres calcular?"))
qui = 0
dos = 0
cie = 0
cin = 0
vei = 0
diez = 0
cinco = 0


while dinero >= 500:
        dinero -= 500
        qui += 1
while dinero >= 200:
        dinero -= 200
        dos += 1
while dinero >= 100:
        dinero -= 100
        cie += 1
while dinero >= 50:
        dinero -= 50
        cin += 1
while dinero >= 20:
        dinero -= 20
        vei += 1
while dinero >= 10:
        dinero -= 10
        diez += 1
while dinero >= 5:
        dinero -= 5
        cinco += 1

print("Hay: ", qui, "billetes de 500,", dos, "billetes de 200, ", cie, "billetes de 100, ", cin, "billetes de 50, ", vei, "billetes de 20, ", diez, "billetes de 10, ", cinco, "billetes de 5")
