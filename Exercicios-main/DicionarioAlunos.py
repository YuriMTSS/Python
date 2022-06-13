aluno = {}
aluno['Nome'] = str(input('Digite o nome: '))
aluno['Média'] = float(input(f'Média do {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif aluno['Média'] <= 5 and aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

print()
for k,v in aluno.items():
    print(f'    - {k} é igual a {v}')