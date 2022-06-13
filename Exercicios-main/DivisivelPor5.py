# Escreva um algoritmo que leia um número 
# e informe se ele é ou não divisível por 5. 

n = int(input("Informe o número: "))

if n % 5 == 0:
    print(n, "é divisivel por 5!")
else:
    print(n, "não é divisivel por 5!")