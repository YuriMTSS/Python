"""Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
Imprima os três vetores."""

lista = []
par = []
impar = []

for x in range(1, 21):
    numero = int(input(f"Informe o {x}º número: "))
    lista.append(numero)

    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print("Pares: ", par)
print("Ímpares: ", impar)
print("Números: ", lista)
