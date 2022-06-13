""" Faça um programa que peça um número inteiro e 
determine se ele é ou não um número primo. Um número 
primo é aquele que é divisível somente por ele mesmo
e por 1 , informe por quais numeros ele e divisivel"""

numero = int(input("Numero: "))
eh_primo = True

for i in range(2, numero):
    if numero % i == 0:
        eh_primo = False
        break

print(eh_primo)
