altura = 5
numero = "4"
espacio = " "
k = -1

for i in range(altura - 1):
    if k == -1:
        print((espacio * k) + (numero))
    else:
        print((numero) + (espacio * k) + (numero))
        
    k += 1
    
print(numero * altura)