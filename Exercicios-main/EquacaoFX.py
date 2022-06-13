"""
Criar um algoritmo em PORTUGOL que receba o valor de x, e calcule e imprima o
valor de f(x).  
"""

x = int(input("Entre com o valor de X: "))

if x <= 1:
    FX = 1
elif x <= 2:
    FX = 2
elif x <= 3:
    FX = x ** 2
else:
    FX = x ** 3

print("f(x) = ", FX)
