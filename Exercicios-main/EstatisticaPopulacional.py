""" Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual 
de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento 
de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população
 do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. """

""" pais_A = 80000
pais_B = 200000
ano = 0

while pais_A <= pais_B:
	pais_A += pais_A * 0.03
	pais_B += pais_B * 0.015
	ano += 1

print ("A ultrapassa ou iguala a B em ", ano," anos" )
"""
""" 
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de 
crescimento iniciais. Valide a entrada e permita repetir a operação. """
pais_A = 0
pais_B = 0
taxa_A = 0
taxa_B = 0
anos = 0

while pais_A < 1:
    pais_A = int(input('Informe a população do país A '))

while taxa_A <= 0:
    taxa_A = float(input('Informe a taxa de crescimento da população do país A '))
    taxa_A /= 100

while pais_B < 1:
    pais_B = int(input('Informe a população do país B '))

while taxa_B <= 0:
    taxa_B = float(input('Informe a taxa de crescimento da população do país B '))
    taxa_B /= 100

while pais_A <= pais_B:
    anos  += 1    
    pais_A += pais_A * taxa_A
    pais_B += pais_B * taxa_B

print("Em ", anos, " anos a população do país A será maior que a população do país B")
