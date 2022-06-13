# Dados três valores A, B e C, construa um algoritmo, que imprima os
# valores de forma ascendente (do menor para o maior)

numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))
numero3 = int(input("Informe o terceiro número: "))

if numero1 < numero2:
    if numero2 < numero3:
        print(numero1, numero2, numero3)
    elif numero1 < numero3:
        print(numero1, numero3, numero2)
    else:
        print(numero3, numero1, numero2)
else:
    if numero2 < numero3:
        if numero1 < numero3:
            print(numero2, numero1, numero3)
        else:
            print(numero2, numero3, numero1)
    else:
        print(numero3, numero2, numero1)