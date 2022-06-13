"""Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, 
o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o 
gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). 
Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. 
Após todos os alunos terem respondido informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova: 01 - A, 02 - B, 03 - C, 04 - D, 05 - E, 06 - E, 07 - D, 08 - C, 09 - B, 10 - A"""
maior_nota = 0
menor_nota = 0
total_usuarios = 0
nota_usuario = 0
media = 0

total_notas = 0

gabarito = list()

qtd_perguntas = int(input("Informe o total de perguntas: "))

for posicao in range(qtd_perguntas):
    pergunta = str(input("Digite o gabarito: "))
    gabarito.append(pergunta)

while True:
    for posicao, resposta in enumerate(gabarito):
        pergunta = str(input("Digite a resposta da pergunta: "))
        if pergunta == resposta:
            nota_usuario += 1

    total_usuarios += 1

    if nota_usuario > maior_nota:
        maior_nota = nota_usuario

    if nota_usuario < menor_nota or menor_nota == 0:
        menor_nota = nota_usuario

    total_notas += nota_usuario

    answer = input("\nFazer a prova novamente: [S/n]: ")
    if answer == '' or answer.lower() == 's':
        user_note = 0
        continue
    break

media = total_notas // total_usuarios

print("Maior acerto: ", maior_nota)
print("Menor acerto: ", menor_nota)
print("Total de alunos: ", total_usuarios)
print("Média das notas: ", media)
