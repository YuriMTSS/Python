""" 
Dado três valores, A, B e C, construa um algoritmo em PORTUGOL para verificar se
estes valores podem ser valores dos lados de um triângulo.  
"""

LadoA = float(input("Entre com o lado A: "))
LadoB = float(input("Entre com o lado B: "))
LadoC = float(input("Entre com o lado C: "))

if LadoA < (LadoB + LadoC) and LadoB < (LadoA + LadoC) and LadoC < (LadoA + LadoB):
    print("Pode ser um triângulo!")
else:
    print("Não pode ser um triângulo")
