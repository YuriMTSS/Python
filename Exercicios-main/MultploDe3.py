# Escreva um algoritmo que receba um número e imprima uma das
# mensagens: “é múltiplo de 3” ou “não é múltiplo de 3”. 

n = int(input("Informe um número: "))

if n % 3 == 0:
    print(n, "é multiplo de 3!")
else:
    print(n, "não é multiplo de 3")