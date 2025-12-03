"""Escriba un programa que lea una calificación numérica entre 0 y 10 y la transforme en la
calificación alfabética, escribiendo el siguiente resultado (switch).
• De 0 a < 3 Muy Deficiente.
• De 3 a < 5 Insuficiente.
• De 5 a < 6 Suficiente.
• De 6 a < 7 Bien.
• De 7 a <9 Notable.
• De 9 a 10 Sobresaliente."""

nota = float(input("Ingresa una nota entre 0 y 10: "))

match nota:
    case n if n >= 0 and n < 3:
        print("Muy Deficiente")
    case n if n >= 3 and n < 5:
        print("Insuficiente")
    case n if n >= 5 and n < 6:
        print("Suficiente")
    case n if n >= 6 and n < 7:
        print("Bien")
    case n if n >= 7 and n < 9:
        print("Notable")
    case n if n >= 9 and n <= 10:
        print("Sobresaliente")
    case _:
        print("Nota no válida")
