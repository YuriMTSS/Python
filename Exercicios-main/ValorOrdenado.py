# Construa um algoritmo, que receba três valores, A, B e C, e
# armazene-os em três variáveis com os seguintes nomes: MAIOR, INTER e MENOR
# (os nomes correspondem aos valores ordenados). 

A = int(input("Informe o primeiro número: "))
B = int(input("Informe o segundo número: "))
C = int(input("Informe o terceiro número: "))

menor = A
inter = B
maior = C

if menor <= inter and inter <= maior:
    print(menor, inter, maior)
elif menor <= maior and maior <= inter:
    print(menor, maior, menor)
elif inter <= menor and menor <= maior:
    print(inter, menor, maior)
elif inter <= maior and maior <= menor:
    print(inter, maior, menor)
elif maior <= inter and maior <= menor:
    print(maior, inter, menor)
else:
    print(maior, menor, inter)