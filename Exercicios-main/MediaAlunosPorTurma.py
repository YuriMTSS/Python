"""Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para
cada turma. As turmas não podem ter mais de 40 alunos."""

turmas = int(input("Quantas turmas? "))
media = 0

for i in range(turmas):
    while True:
        alunos = int(input("Alunos da turma: "))
        if alunos <= 40:
            break
    media = ((media * i) + alunos) // (i + 1)

print("Média: ", media)
