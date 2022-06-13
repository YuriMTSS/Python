"""
Criar um algoritmo em PORTUGOL que receba o valor de x, e calcule e imprima o
valor de f(x).

fx = 8 / (2 - x)

"""

x = int(input("Informe x: "))

if x == 2:
    print("Não é possível calcular FX")
else:
    FX = 8 / (2 - x)
    print("FX: ", FX)


