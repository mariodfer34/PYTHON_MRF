"""Tiendas Don Pepe desea un programa para ingresar por teclado el monto de compra y el día
de la semana; si el día es martes o jueves, se realizará un descuento del 15% por la compra.
Visualizar el descuento y el total a pagar por la compra."""

precio = float(input("Ingrese el monto de la compra: "))
dia = input("Ingrese el día de la semana: ").lower()
total_pagar = 0

if dia == "martes" or dia == "jueves":
    total_pagar = precio - (precio * 0.15)
    print("Total a pagar: ", total_pagar)
else:
    print("Total a pagar: ", precio)