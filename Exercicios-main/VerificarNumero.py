# Construir um algoritmo em PORTUGOL que leia um número e imprima se ele é igual
# a 5, a 200, a 400, se está no intervalo entre 500 e 1000, inclusive, ou se ela está fora
# dos escopos anteriores.

numero = int(input("Entre com o número: "))

if numero == 5:
    print("Numero igual a ", numero)
elif numero == 200:
     print("Numero igual a ", numero)
elif numero == 400:
    print("Numero igual a ", numero)

if numero >= 500 and numero <= 1000:
    print("Está no intervalo entre 500 e 1000!")
else:
    print("Está fora dos escopos propostos!")
