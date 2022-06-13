"""Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973."""

#meses = ['janeiro', 'favereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

#dia, mes, ano = input("Data: (dd,mm,aa): ").split('/')

#print("Você nasce em: ")
#print(dia, meses[int(mes) - 1], ano)

meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

data = input("Data (dd,mm,aa): ")
print (data.split("/")[0],
       "de",
       meses[(int(data.split("/")[1])-1)],
       "de",
       data.split("/")[2])
"""
O método Python split é uma das funções disponíveis em Python utilizada para a manipulação de strings. 
Na prática, ele permite dividir o conteúdo da variável de acordo com as condições especificadas em cada 
parâmetro da função ou com os valores predefinidos por padrão. """
