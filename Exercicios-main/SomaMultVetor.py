"""Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números."""
lista = []
soma = 0
multplicacao = 1

for i in range(5):
    numero = int(input("Informe o número: "))
    lista.append(numero)
    soma += numero
    multplicacao *= numero

print("Os números: ", lista)
print("Soma dos valores: ", soma)
print("Multplicação dos valores: ", multplicacao)
