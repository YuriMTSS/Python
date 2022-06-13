"""Faça um Programa que peça a idade e a altura de 5 pessoas, 
armazene cada informação no seu respectivo vetor. Imprima a 
idade e a altura na ordem inversa a ordem lida"""
idade = []
altura = []

for i in range(5):
    idade.append(int(input("Idades: ")))
    altura.append(float(input("Alturas: ")))

for i in range(5):
    print("Idades inversas: ",idade[len(idade) - 1 - i])

for i in range(5):
    print("Alturas inversas: ", altura[len(altura) - 1 - i])
