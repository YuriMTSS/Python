"""
Criar um algoritmo em PORTUGOL que leia o número correspondente ao mês atual e
os dígitos (somente os quatro números) de uma placa de veículo, e através do número
finalizador da placa (algarismo da casa das unidades) determine se o IPVA do veículo
vence no mês corrente.
Final 1 – mês (1) – Janeiro Final 6 – mês (6) – Junho
Final 2 – mês (2) – Fevereiro Final 7 – mês (7) – Julho
Final 3 – mês (3) – Março Final 8 – mês (8) – Agosto
Final 4 – mês (4) – Abril Final 9 – mês (9) – Setembro
Final 5 – mês (5) – Maio Final 0 – mês (10) – Outubro
"""

mes = int(input("Mês: "))
placa = int(input("Placa: "))
digito = placa % 10

if digito == mes:
    print("Este mês vence o IPVA")
else:
    print("O IPVA não vence esse mês")


