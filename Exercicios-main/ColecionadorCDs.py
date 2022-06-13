""" Faça um programa que calcule o valor total
investido por um colecionador em sua coleção
de CDs e o valor médio gasto em cada um deles.
O usuário deverá informar a quantidade de CDs
e o valor para em cada um """

Qtd_CDS = int(input("Quantidade de CDS: "))

valor_total = 0

for _ in range(Qtd_CDS):
    valor_CD = int(input("Valor do CD: "))
    valor_total += valor_CD

valor_medio = valor_total / Qtd_CDS
print("Valor total: ", valor_total)
print("Valor médio: ", valor_medio)


