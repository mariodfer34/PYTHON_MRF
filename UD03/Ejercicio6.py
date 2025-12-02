asterisco = "*"
espacio = " "
espacio_interior = " "

altura = 7


for i in range(altura):
    if i < 1:
        print(asterisco + (espacio_interior * (altura - (i + 2))) + asterisco)
    elif i == (altura // 2):
         print(asterisco + (espacio_interior * (i - 1)) + asterisco + (espacio_interior * (i - 1)) + asterisco)
    elif i > (altura // 2):
        print(asterisco + (espacio_interior * (altura - 2)) + asterisco)
    else:
        print(asterisco + (espacio_interior * (i - 1)) + asterisco + (espacio_interior * (altura - (i*2 + 2))) + asterisco + (espacio_interior * (i - 1)) + asterisco)