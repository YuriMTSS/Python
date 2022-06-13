""" 
Dado três valores, A, B e C, construa um algoritmo em PORTUGOL para verificar se
estes valores podem ser valores dos lados de um triângulo, e se for, se é um triangulo
escaleno, um triangulo eqüilátero ou um triangulo isósceles.  
"""

LadoA = float(input("Entre com o lado A: "))
LadoB = float(input("Entre com o lado B: "))
LadoC = float(input("Entre com o lado C: "))

if LadoA <= 0 or LadoB <= 0 or LadoC <= 0:
    print("Todos os lados devem ser positivos")
else:
    if LadoA < (LadoB + LadoC) and LadoB < (LadoA + LadoC) and LadoC < (LadoA + LadoB):
        if LadoA == LadoB and LadoA == LadoC:
            print("Equilatero")
        elif LadoA == LadoB or LadoA == LadoC or LadoB == LadoC:
            print("Isoceles")
        else:
            print("Escaleno")
    else:
        print("Não pode ser um triângulo")


