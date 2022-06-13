"""
Desenvolver um algoritmo que leia a altura de 15 pessoas. 
Este programa deverá calcular e mostrar:
A menor altura do grupo
A maior altura do grupo
"""

primeiro_numero = int(input())
maior = primeiro_numero
menor = primeiro_numero

for _ in range(15):
    numero = int(input())
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(menor, maior)
