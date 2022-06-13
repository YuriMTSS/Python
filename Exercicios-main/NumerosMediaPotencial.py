"""
Desenvolver um algoritmo que leia um número não determinado de valores e calcule e escreva a
média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores
negativos e o percentual de valores negativos e positivos.  
"""
Positivos = 0
Negativos = 0
Soma = 0
SomaNumeros = 0
Continuar = "S"
while Continuar in "Ss":
    numero = int(input("Digite um número: "))
    if numero > 0:
        Positivos += numero
    else:
        Negativos += numero
    SomaNumeros += numero
    Soma += 1
    Continuar = str(input("Quer continuar? [S/N]")).upper().strip()[0]
print("Media: ", SomaNumeros / Soma)
print("Valores positivos: ", Positivos)
print("Valores negativos: ", Negativos)
