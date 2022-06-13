""" Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo """

inteiro1 = int(input("Primeiro inteiro: "))
inteiro2 = int(input("Segundo inteiro: "))
real = float(input("Número real: "))

caso1 = (inteiro1 ** 2) * (inteiro2 / 2)
caso2 = (inteiro1 ** 3) + real
caso3 = real ** 3

print("Produto do dobro do primeiro com metade do segundo: ",caso1)
print("A soma do triplo do primeiro com o terceiro: ",caso2)
print("O terceiro elevado ao cubo: ",caso3)
