"""Faça um Programa que leia 4 notas, mostre as notas e a média na tela."""
notas = []
media = 0
soma = 0

for i in range(4):
	notas.append(float(input("Nota: ")))
	soma += notas[i]

media = soma / 4

print ("Notas: ", notas) 
print ("Media: ", media)
