# Escreva um algoritmo que leia um número e imprima a raiz quadrada do número caso ele seja positivo 
# ou igual a zero e o quadrado do número caso ele seja negativo. 

n = int(input("Entre com o número: "))

if n >= 0:
    n = n ** (1/2)
    print (n)

if n < 0:
    n = n** 2
    print (n)
