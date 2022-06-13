"""Faça um programa que leia uma quantidade indeterminada de números positivos e 
conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. 
A entrada de dados deverá terminar quando for lido um número negativo"""

intervalo_1 = 0
intervalo_2 = 0
intervalo_3 = 0
intervalo_4 = 0

numeros = int(input("Informe um número, caso queira terminar informe um negativo: "))
while numeros >= 0:
    numeros = int(input("Informe um número, caso queira terminar informe um negativo: "))
    if numeros >= 0 and numeros < 26:
        intervalo_1 += 1

    elif numeros >= 26 and numeros < 51:
        intervalo_2 += 1

    elif numeros >= 51 and numeros < 76:
        intervalo_3 += 1
        
    elif numeros >= 76 and numeros < 101:
        intervalo_4 += 1

print("Intervalo entre 0 e 25 tem: ", intervalo_1, " números")
print("Intervalo entre 26 e 50 tem: ", intervalo_2, " números")
print("Intervalo entre 51 e 75 tem: ", intervalo_3, " números")
print("Intervalo entre 76 e 100 tem: ", intervalo_4, " números")
