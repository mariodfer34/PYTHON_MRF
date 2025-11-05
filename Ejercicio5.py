radio = input("Introduce el radio del circulo: ")
radio = float(radio)
diametro = radio / 2
longitud = diametro * 3.14
area = 3.14 * (radio * radio)
volumen = (4/3) * 3.14 * (radio ** 3)
print("longitud:", longitud, "Area:", area, "Volumen:", volumen)