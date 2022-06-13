""" Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
 usando a seguinte fórmula: 
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
 """

altura = float(input("Altura: "))

homens = (72.7 * altura) - 58
mulheres = (62.1 * altura) - 44.7

print("Peso ideal para homens: ", homens)
print("Peso ideal para mulheres: ", mulheres)

