# Dados três valores A, B e C, construa um algoritmo em PORTUGOL, que imprima os
# valores de forma descendente (do maior para o menor).

numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))
numero3 = int(input("Informe o terceiro número: "))

if numero1 >= numero2 and numero2 >= numero3:
    print(numero1, numero2, numero3)
elif numero1 >= numero3 and numero3 >= numero2:
    print(numero1, numero3, numero1)
elif numero2 >= numero1 and numero1 >= numero3:
    print(numero2, numero1, numero3)
elif numero2 >= numero3 and numero3 >= numero1:
    print(numero2, numero3, numero1)
elif numero3 >= numero2 and numero3 >= numero1:
    print(numero3, numero2, numero1)
else:
    print(numero3, numero1, numero2)