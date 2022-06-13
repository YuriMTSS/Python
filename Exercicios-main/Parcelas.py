"""Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: 
valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25 
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67
"""
divida = float(input("Valor da dívida: "))
parcela = 1

for i in range(5):
    if parcela == 1:
        juros = 1
        valor_juros = 0

    elif parcela == 2 or parcela == 3:
        parcela = 3
        juros = 1.10
    
    elif parcela == 6 or parcela == 7:
        parcela = 6
        juros = 1.15
    
    elif parcela == 9 or parcela == 10:
        parcela = 9
        juros = 1.20
    
    elif parcela == 12 or parcela == 13:
        parcela = 12
        juros = 1.25

    valor_juros = divida * (juros - 1)
    divida_com_juros = divida * juros
    valor_parcela = divida_com_juros / parcela

    print("Dívida com juros: R$", divida_com_juros)
    print("Valor dos juros: ", valor_juros)
    print("Parcela: ", parcela)
    print("Valor da parcela: R$ ",valor_parcela)
    parcela += 3
