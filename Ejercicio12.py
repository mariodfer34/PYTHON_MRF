LIMITE = 200

print("Números pares entre 1 y 200:")

for num in range(1, LIMITE + 1):
    if num % 2 == 0:
        print(num, end=" ")

print()