"""
Construir um algoritmo em PORTUGOL para calcular as raízes de uma equação do 2º
grau, sendo que os valores dos coeficientes A, B, e C devem ser fornecidos pelo
usuário através do teclado.  

delta = b*b - 4 * a * c
x1 e x2 = (-b raiz(delta) / (2*a))

delta maior que 0 = ok
delta menor que 0 = error
delta igual a 0 = raizes iguais
"""
import math
A = int(input("Informe o valor A da formula: "))
B = int(input("Informe o valor B da formula: "))
C = int(input("Informe o valor C da formula: "))

delta = B ** 2 - 4 * A * C

if delta > 0:
    print("Raízes diferentes")
    x1 = (-B + math.sqrt(delta) / (2 * A))
    x2 = (-B - math.sqrt(delta) / (2 * A))
elif delta == 0:
    print("Raízes iguais")
    x1 = (-B * math.sqrt(delta) / (2 * A))
    x2 = x1
else:
    print("Delta negativo")

if delta >= 0:
    print("X1: ", x1, " X2: ", x2)