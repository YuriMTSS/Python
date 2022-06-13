# Escreva um algoritmo em PORTUGOL que leia um número e informe se ele é
# divisível por 10, por 5 OU por 2 OU se não é divisível por nenhum deles. 

numero = int(input("Informe um numero inteiro: "))

if numero % 10 == 0 or numero % 5 == 0 or numero % 2 == 0:
    print(numero, "é divisível por 10, 5 ou por 2")
else:
    print("Não é divisível por nenhum!")