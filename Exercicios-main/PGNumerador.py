""" Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em
P.G. contendo 10 valores """

A = int(input("Entre com A: "))
R = int(input("Entre com R: "))
formula = A * R ** (R - 1) 

for i in range(A, formula + R, R):
    print(i, end="->")
print("Acabou")


