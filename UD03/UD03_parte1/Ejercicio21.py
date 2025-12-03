"""Escriba un programa que calcula el salario neto semanal de un trabajador en función del
número de horas trabajadas y la tasa de impuestos de acuerdo a las siguientes hipótesis:
• Las primeras 35 horas se pagan a tarifa normal.
• Las horas que pasen de las 35 horas se pagan a 1,5 veces la tarifa normal.
• Las tasas de impuesto son:
o Los primeros 500€ son libres de impuestos.
o Los siguientes 400€ tiene un 25% de impuesto.
o Los restantes un 45% de impuesto.
Escribe el nombre del trabajador, salario bruto, tasas y salario neto."""

nombre = input("Ingrese el nombre del trabajador: ")
horas_trabajadas = float(input("Ingresa las horas trabajadas: "))
tarifa_hora = float(input("Ingresa la tarifa por hora: "))
salario_bruto = 0
salario_neto = 0

if horas_trabajadas > 35:
    horas_trabajadas -= 35
    salario_bruto = (35 * tarifa_hora) + (horas_trabajadas * (tarifa_hora * 1.5))
else:
    salario_bruto = tarifa_hora * horas_trabajadas

if salario_bruto > 900:
    salario_bruto -= 900
    salario_neto = (400 * 0.75) + 500 + (salario_bruto * 0.55)
elif salario_bruto > 500 and salario_bruto < 900:
    salario_bruto -= 500
    salario_neto = (salario_bruto * 0.75) + 500
else:
    salario_neto = salario_bruto
    
print(salario_neto)
    
    
    
    

