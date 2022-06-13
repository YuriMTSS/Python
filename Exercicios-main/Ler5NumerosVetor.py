"""Faça um Programa que leia um vetor de 5 números inteiros e mostre-os."""
""" 
lista = []
for i in range(5):
    numeros = int(input("Informe um número: "))
    lista.append(numeros)

print(lista)
"""



"""Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa"""
lista = []

for i in range(5):
    lista.append(float(input("Informe o numero: ")))
    contador = len(lista) - 1

while contador >= 0:
    print(lista[contador], end=" - ")
    contador -= 1
