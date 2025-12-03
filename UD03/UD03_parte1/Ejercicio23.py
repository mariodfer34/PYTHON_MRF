"""Una farmacia desea un programa para ingresar el valor de compra y calcular lo siguiente: si
el pago se efectúa al “contado”, calcular un descuento del 5%; pero si el pago es con “tarjeta”
se incrementa un recargo del 3% al valor de compra. Calcular y visualizar el descuento o recargo
según sea el caso y el total a pagar de la compra"""

valor_compra = float(input("Ingrese el valor de compra: "))
forma_pago = input("Ingrese cómo va a pagar (contado/tarjeta): ").lower()
total_pagar = 0

if forma_pago == "contado":
    total_pagar = valor_compra - (valor_compra * 0.05)
    print("Total a pagar: ", total_pagar)
elif forma_pago == "tarjeta":
    total_pagar = valor_compra + (valor_compra * 0.03)
    print("Total a pagar: ", total_pagar)
else:
    print("Método de pago no válido.")