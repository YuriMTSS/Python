""" Faça um Programa que pergunte quanto você ganha por hora e o número de horas 
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. """

ganho_hora = float(input("Ganha por hora: "))
tempo_trabalho_mensal = float(input("Horas de trabalho esse mês: "))

salario_mes = ganho_hora * tempo_trabalho_mensal

print("Salário: R$", salario_mes)


