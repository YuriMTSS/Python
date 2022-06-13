from datetime import date, datetime

dados = {}
dados['Nome'] = str(input('Nome do trabalhador: '))
nascimento = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - nascimento
dados['CTPS'] = int(input('Carteira de trabalho, 0 - não tem: '))

if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - datetime.now().year)
print('-=-' * 30)
for k, v in dados.items():
    print(f'    - {k} tem o valor {v}.')

