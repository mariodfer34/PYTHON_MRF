n = int(input("Introduce el número límite (N): "))

print("Contando del 1 a " + str(n) + ":")

for num in range(1, n + 1):
    print(num, end=" ")
print()