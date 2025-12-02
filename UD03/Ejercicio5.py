punto = "."
asterisco = "*"

altura = int(input("Introduce la altura de la figura"))
contador_asteriscos = 0
contador_puntos = 0

print(punto * altura)
for i in range(altura // 2 - 1):
    print((punto * contador_puntos) + ((punto + asterisco) * ((altura - contador_asteriscos) // 2)) + (punto * (contador_puntos + 1)))
    contador_asteriscos += 2
    contador_puntos += 1
print(asterisco * altura)
contador_asteriscos -= 2
contador_puntos -= 1
for i in range(altura // 2 - 1):
    print((punto * contador_puntos) + ((punto + asterisco) * ((altura - contador_asteriscos) // 2)) + (punto * (contador_puntos + 1)))
    contador_asteriscos -= 2
    contador_puntos -= 1
print(punto * altura)
