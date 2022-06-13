""" Faça um programa que receba dois números inteiros e 
gere os números inteiros que estão no intervalo 
compreendido por eles. """

""" numero1 = int(input("Primeiro número: "))
numero2 = int(input("Segundo número: "))

for i in range(numero1,numero2,1):
    print(i, end=" ")
 """
""" Altere o programa anterior para mostrar no final a soma dos números """
numero1 = int(input("Primeiro número: "))
numero2 = int(input("Segundo número: "))
soma = 0
for i in range(numero1,numero2,1):
    print(i, end=" ")
    soma += i
print("\nSoma:",soma)

