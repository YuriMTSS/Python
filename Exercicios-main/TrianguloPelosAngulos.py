"""
Dados três valores A, B e C, construa um algoritmo para verificar se
estes valores podem ser valores dos lados de um triângulo, e se for, classificá-los
segundo os ângulos. (Triângulo Retângulo = 90º, Triângulo Obtusângulo
> 90º , Triângulo Acutângulo < 90º)  
"""

LadoA = float(input("Entre com o lado A: "))
LadoB = float(input("Entre com o lado B: "))
LadoC = float(input("Entre com o lado C: "))

if LadoA < (LadoB + LadoC) and LadoB < (LadoA + LadoC) and LadoC < (LadoA + LadoB):
        print("É um triângulo")
        if (LadoA ** 2 == LadoB ** 2 + LadoC ** 2) or (LadoB ** 2 == LadoA ** 2 + LadoC ** 2) or (LadoC ** 2 == LadoA ** 2 + LadoB ** 2):
            print("Retângulo")
        elif (LadoA ** 2 > LadoB ** 2 + LadoC ** 2) or (LadoB ** 2 > LadoA ** 2 + LadoC ** 2) or (LadoC ** 2 > LadoA ** 2 + LadoB ** 2):
            print("Obtusângulo")
        elif (LadoA ** 2 < LadoB ** 2 + LadoC ** 2) or (LadoB ** 2 < LadoA ** 2 + LadoC ** 2) or (LadoC ** 2 < LadoA ** 2 + LadoB ** 2):
            print("Acutângulo")
else:
    print("Não é um triângulo")
