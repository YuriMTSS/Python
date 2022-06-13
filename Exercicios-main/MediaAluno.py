""" 
Escreva um algoritmo que leia as duas notas bimestrais de um aluno
e determine a média das notas semestral. Através da média calculada o algoritmo deve
imprimir a seguinte mensagem: “Aprovado”, “Reprovado” ou em “Exame” (a média é
7 para Aprovação, menor que 3 para Reprovação e as demais em Exame). 
 """

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
media = (nota1 + nota2) / 2
print("A média é: ", media)

if media < 3:
    print("Reprovado") 
elif media > 7:
    print("Aprovado")
else:
    print("Exame")