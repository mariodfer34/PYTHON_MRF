"""La universidad ha categorizado las matrículas de acuerdo a la facultad que va a estudiar el
postulante. Ingrese por teclado el nombre del postulante y la facultad que va a estudiar, muestre
el importe, la mensualidad, el IGV 18% (importe + mensualidad) y el monto final a pagar. (Use el
control switch)."""

nombre = input("Ingresa el nombre del postulante: ")
facultad = input("Ingresa la facultad en la que va a estudiar (Ingeniería de sistemas, Derecho, Ing.Naviera, Ing.Pesquera, Contabilidad, Administración): ").lower()
importe = 0
mensualidad = 0
invalido = False

match facultad:
    case "ingeniería de sistemas":
        importe = 350
        mensualidad = 650
    case "derecho":
        importe = 300
        mensualidad = 550
    case "ing.naviera":
        importe = 300
        mensualidad = 300
    case "ing.pesquera":
        importe = 310
        mensualidad = 460
    case "contabilidad":
        importe = 280
        mensualidad = 490
    case "administración":
        importe = 360
        mensualidad = 520
    case _:
        print("Facultad no válida")
        invalido = True
        
if invalido == False:
    precio = importe + mensualidad + ((importe + mensualidad) * 0.18)
    print("El precio final es: ", precio)
