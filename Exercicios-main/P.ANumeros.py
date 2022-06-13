""" Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em
P.A. contendo 10 valores. 

a(n) = a(l) + (n - 1) x r

"""

A = int(input("Entre com A: "))
R = int(input("Entre com R: "))
formula = A + (10 - 1) * R

for i in range(A, formula + R, R):
    print(i, end="->")
print("Acabou")




