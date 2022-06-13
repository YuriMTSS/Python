""" 
Criar um algoritmo em PORTUGOL que receba o valor de x, e calcule e imprima o
valor de f(x).
fx = 5x + 3 / (x*x - 16)
 """

import math

x = int(input("Informe o valor de X: "))

if x >= -4 and x <= 4:
    print("Impossível calcular fx")
else:
    FX = (5*x + 3) / math.sqrt(x * x - 16)
    print("FX: ", FX)

