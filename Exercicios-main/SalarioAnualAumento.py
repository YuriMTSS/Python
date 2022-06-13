"""
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro 
do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. 
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário."""

salario = float(input("Digite o salário inicial do funcionário em 1995: "))
ano = 1995
ano_atual = int(input("Informe o ano atual: "))
aumento = 0.015 

for _ in range(ano, ano_atual):
    salario *= 1 + aumento
    aumento *= 2

print("Salário atual: R$", salario)
