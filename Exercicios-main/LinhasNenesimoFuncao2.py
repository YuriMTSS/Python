"""Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
"""

def imprimir_linhas(numero):
    for i in range(numero):
        print('{}'.format(i), end=' ')
    print()

def imprimir_sequencias(numero):
    for numero in range(numero + 1):
        imprimir_linhas(numero)

numero = input("Informe um número: ")
imprimir_sequencias(int(numero))
