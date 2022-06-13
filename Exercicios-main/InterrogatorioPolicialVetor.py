"""Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". """

#Entrada
perguntas = [
    "Telefonou para a vítima? 1 para sim ou 0 para não",
    "Esteve no local do crime? 1 para sim ou 0 para não",
    "Mora perto da vítima? 1 para sim ou 0 para não",
    "Devia para a vítima? 1 para sim ou 0 para não",
    "Já trabalhou com a vítima? 1 para sim ou 0 para não"
]
jugamento = [
    "Inocente",
    "Suspeita",
    "Cumplice",
    "Assassino"
]
resposta = []
soma_respotas = 0

#Processamento
for i in range(len(perguntas)):             # Percorre a lista de perguntas exibindo numa de cada vez
    print(perguntas[i])                     # Mostra a pergunta
    resposta.append(input())                # Adiciona as repostas na lista
    soma_respotas += int(resposta[i])       # Converte a lista para int e soma com a resposta

#Saída
if soma_respotas < 2:
    print(jugamento[0])                     # A suspeita for menor que 2 ele é inocente
elif soma_respotas == 2:                    
    print(jugamento[1])                     # Se for igual a 2 é suspeita
elif soma_respotas <= 4:
    print(jugamento[2])                     # Se for maior que 2 e menor ou igual a 4 é cumplice
else:
    print(jugamento[3])                     # De qualquer outro modo é o assassino
