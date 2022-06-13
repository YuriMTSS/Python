"""  
Escreva um algoritmo em PORTUGOL que leia um peso na Terra e o número de um
planeta e imprima o valor do seu peso neste planeta. A relação de planetas é dada a
seguir juntamente com o valor das gravidades relativas á Terra:
# Gravidade Relativa Planeta
1 0,37 Mercúrio
2 0,88 Vênus
3 0,38 Marte
4 2,64 Júpiter
5 1,15 Saturno
6 1,17 Urano  
"""
planeta = int(input("Escolha uma opcao: "))
peso = float(input("Informe o peso: "))

if planeta == 1:
    peso *= 0.37 
elif planeta == 2:
    peso *= 0.88
elif planeta == 3:
    peso *= 0.38
elif planeta == 4:
    peso *= 2.64
elif planeta == 5:
    peso *= 1.15
elif planeta == 6:
    peso *= 1.17
else:
    print("Opcao invalida")

print("O novo peso é: ", peso)
