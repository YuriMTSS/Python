"""Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de
cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro 
notas de 1 
"""
valor_saque = int(input("Informe o valor do saque: "))
if valor_saque != 0:
    cem = valor_saque // 100
    valor_saque = valor_saque - (cem * 100)

    cinquenta = valor_saque // 50
    valor_saque = valor_saque - (cinquenta * 50)

    vinte = valor_saque // 20
    valor_saque = valor_saque - (vinte * 20)

    dez = valor_saque // 10
    valor_saque = valor_saque - (dez * 10)

    cinco = valor_saque // 5
    valor_saque = valor_saque - (cinco * 5)

    um = valor_saque
else:
    print("Valor inválido")

print("Notas de 100 : R$", cem)
print("Notas de 50 : R$", cinquenta)
print("Notas de 20 : R$", vinte)
print("Notas de 10 : R$", dez)
print("Notas de 5: R$", cinco)
print("Notas de 1: R$", um)
