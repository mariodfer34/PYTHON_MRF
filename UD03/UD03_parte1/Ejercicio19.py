"""Escriba un programa que simule un cajero automático con un saldo inicial de 1000 dólares,
con el siguiente menú de opciones:
Bienvenido a su Cajero Virtual
1. Ingresar dinero en cuenta
2. Retirar dinero de la cuenta
3. Salir"""

saldo = 1000

print("Bienvenido a su Cajero Virtual")
print("1. Ingresar dinero en cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Salir")

opcion = int(input("Seleccione una opción: "))

if opcion == 1:
    ingresar = float(input("Introduce la cantidad que quieres ingresar: "))
    saldo += ingresar
    print("Su saldo es:", saldo, " Euros")
elif opcion == 2:
    retirar = float(input("Ingresa la cantidad que quieres retirar: "))
    if retirar > saldo:
        saldo -= retirar
        print("Su nuevo saldo es:", saldo)
    else:
        print("Fondos insuficientes")
elif opcion == 3:
    print("Gracias por usar el Cajero Virtual. ¡Hasta luego!")
else:
    print("Opción no válida")

