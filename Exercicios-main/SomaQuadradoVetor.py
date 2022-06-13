"""Faça um Programa que leia um vetor A com 10 números inteiros, 
calcule e mostre a soma dos quadrados dos elementos do vetor"""
lista = []
quadrado = 1
soma = 0
for i in range(5):
    valores = int(input("Informe os valores: "))

    quadrado = valores ** 2
    lista.append(quadrado)

    soma += quadrado

print("Os valores ao quadrado: ", lista)
print("Soma do quadrado deles: ", soma)
