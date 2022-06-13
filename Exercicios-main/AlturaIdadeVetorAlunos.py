"""Foram anotadas as idades e alturas de 30 alunos. 
Faça um Programa que determine quantos alunos com mais de 
13 anos possuem altura inferior à média de altura desses alunos"""
lista_idades = []
lista_alturas = []
soma = 0
media_altura = 0
quantidade_alunos = 0

print("Vamos começar com as alturas!")
for i in range(5):
    alturas = float(input("Informe as alturas na ordem dos alunos: "))
    lista_alturas.append(alturas)
    soma += lista_alturas[i]

media_altura = soma / 5
print("Média: ", media_altura)

print("\nIdade dos alunos em ordem!")
for i in range(len(lista_alturas)):
    idade = int(input("Informe a idade: "))
    lista_idades.append(idade)

for i in range(len(lista_idades and lista_alturas)):
    if lista_idades[i] > 13 and lista_alturas[i] < media_altura:
        quantidade_alunos += 1

print("\nTem no total ", str(quantidade_alunos) + " alunos possuem mais de 13 anos e altura inferior a  média de altura dos alunos")
