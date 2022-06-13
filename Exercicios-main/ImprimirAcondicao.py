# Criar um algoritmo em PORTUGOL que leia dois números e imprimir o quadrado do
# menor número e raiz quadrada do maior número, se for possível. 

#numero1 = int(input("Entre com o primeiro numero: "))
#numero2 = int(input("Entre com o segundo numero: "))

#if numero1 < numero2:
#    menor = numero1 ** 2
#    print ("O quadrado é: ", menor)

#    maior = numero2 ** (1/2)
#    print("A raiz é: ", maior)

#else: #numero1 > numero2:
#    maior = numero1 ** (1/2)
#    print("A raiz é: ", maior)
    
#    menor = numero2 ** 2
#    print ("O quadrado é: ",menor)




numero1 = int(input("Digite numero 1: "))
numero2 = int(input("Digite numero 2: "))

# Assume que numero1 eh o menor e numero2 eh o maior
menor = numero1
maior = numero2

# Se nao for o caso, inverte
if numero2 < numero1:
    menor = numero2
    maior = numero1

print(menor * menor)

if maior < 0:
    print("Nao existe raiz quadrada de numero negativo")
else:
    print(maior ** (1/2))
