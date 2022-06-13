# Construa um algoritmo que dado quatro valores, A, B, C e D, o
# algoritmo imprima o maior e o menor valor.

A = int(input("Informe o primeiro valor: "))
B = int(input("Informe o segundo valor: "))
C = int(input("Informe o terceiro valor: "))
D = int(input("Informe o quarto valor: "))

maior = A
if B > maior:
    maior = B
if C > maior:
    maior = C
if D > maior:
    maior = D