"""Faça um Programa que peça as quatro notas de 10 alunos, 
calcule e armazene num vetor a média de cada aluno, imprima 
o número de alunos com média maior ou igual a 7.0."""
lista_media = []
aprovados = 0

for i in range(10):
    soma = 0
    for x in range(1 ,5):
        numero = float(input("Informe a %dº nota: " % x))
        soma += numero

    lista_media.append(soma / 4)

    if lista_media[i] >= 7.0:
        aprovados += 1

print(soma)
print("As medias dos alunos foram:", lista_media)
print("Total de alunos que tiveram média acima de 7: ", aprovados)
