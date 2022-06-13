# Escreva um algoritmo para determinar se um número A é divisível
# por um outro número B. Esses valores devem ser fornecidos pelo usuário.

A = int(input("Informe um número: "))
B = int(input("Informe outro número: "))

if A % B == 0:
    print("É divisível!")
else:
    print("Não é divisível!")