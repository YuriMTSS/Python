""" Faça um programa que calcule o mostre a média aritmética de N notas. """

quantidade = int(input("Quantas notas irá calcular? "))
media = 0

for _ in range(quantidade):
    notas = float(input("Digite a nota: "))
    media += notas

print("Media: ", media/quantidade)




