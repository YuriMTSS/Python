""" Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?" "Esteve no local do crime?" "Mora perto da vítima?" "Devia para a vítima?" "Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões será classificada como "Suspeita", entre 3 e 4 "Cúmplice" 
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". """

resposta1 = int(input("Telefonou para a vítima? \n1 - Sim ou 0 - Não: "))
resposta2 = int(input("Esteve no local do crime? \n1 - Sim ou 0 - Não: "))
resposta3 = int(input("Mora perto da vítima? \n1 - Sim ou 0 - Não: "))
resposta4 = int(input("Devia para a vítima? \n1 - Sim ou 0 - Não: "))
resposta5 = int(input("Já trabalhou com a vítima? \n1/Sim ou 0/Não: "))

soma_respostas = resposta1 + resposta2 + resposta3 + resposta4 + resposta5

if (soma_respostas < 2):
    print("Inocente")

elif (soma_respostas == 2):
    print("Suspeita")

elif (3 <= soma_respostas <= 4):
    print("Cúmplice")

elif (soma_respostas == 5):
    print("Assassino")
