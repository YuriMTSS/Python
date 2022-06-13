"""Faça um programa, com uma função que necessite de um argumento. 
A função retorna o valor de caractere ‘P’, se seu argumento for positivo, 
e ‘N’, se seu argumento for zero ou negativo."""

def testando_numero(numero):
    if numero < 0:
        print("N")
    elif numero > 0:
        print("P")
    else:
        print("Neutro")


numero = float(input("Informe um numero: "))
testando_numero(numero)
