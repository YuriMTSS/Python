""" Escreva um algoritmo que leia um valor inicial A e imprima a seqüência de valores do cálculo de
A! e o seu resultado """


numero = int(input("Fatorial de "))
c = numero
f = 1

print("Calculando {}! = ". format(numero), end=" ")
while c > 0:
    print("{}".format(c), end=" ")
    print(" x " if c > 1 else " = ", end=" ")

    f *= 1
    c -= 1
print("{}".format(f))



