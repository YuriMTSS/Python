"""Faça um Programa que leia dois vetores com 10 elementos cada. 
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser 
compostos pelos elementos intercalados dos dois outros vetores."""

lista1 = []
lista2 = []
lista3 = []

for i in range(5):
    lista1.append(int(input("Informe os valores da lista 1: ")))

for i in range(5):
    lista2.append(int(input("Informe os valores da lista 2: ")))

for i in range(5):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print(lista3)
