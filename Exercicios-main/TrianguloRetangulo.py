"""Dados três valores A, B e C, construa um algoritmo para verificar se estes valores podem ser valores dos lados de um triângulo, 
e se for um triângulo retângulo, determinar (imprimir) os seus ângulos internos."""
import math
LadoA = float(input("Lado A: "))
LadoB = float(input("Lado B: "))
LadoC = float(input("Lado C: "))

if LadoA < (LadoB + LadoC) and LadoB < (LadoA + LadoC) and LadoC < (LadoA + LadoB):
    print("É um triângulo")
    Angulo3 = 90
    if LadoA > LadoB and LadoA > LadoC:
        Angulo1 = math.sin(LadoB / LadoA)
        Angulo2 = math.cos(LadoC / LadoA)
    elif LadoB > LadoA and LadoB > LadoC:
        Angulo1 = math.sin(LadoA / LadoB)
        Angulo1 = math.sin(LadoC / LadoB)
    else:
        Angulo1 = math.sin(LadoA / LadoC)
        Angulo2 = math.sin(LadoB / LadoC)
    print(Angulo1)
    print(Angulo2)
    print(Angulo3)
else:
    print("Não é triângulo")

