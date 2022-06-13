"""Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973."""

meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

data = input("Informe a data no formato (dd/mm/aaaa): ")

print (data.split("/")[0],
       "de",
       meses[(int(data.split("/")[1])-1)],
       "de",
       data.split("/")[2])

