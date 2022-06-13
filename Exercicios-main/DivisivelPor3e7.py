# Escreva um algoritmo que leia um número e informe se ele é
# divisível por 3 e por 7. 

n = int(input("Informe um número: "))

if n % 3 == 0 and n % 7 == 0:
    print("É divisível!")
else:
    print("Não é divisível!") 