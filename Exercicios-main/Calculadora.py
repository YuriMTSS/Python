def soma(parcela_1, parcela_2):
    return parcela_1 + parcela_2

def subtracao(minuendo, subtraendo):
    return minuendo - subtraendo

def multplicar(multplicando, multplicador):
    return multplicando * multplicador

def dividir(dividendo, divisor):
    if divisor == 0:
        print("Impossível dividor por 0!!!")
    else:
        return dividendo / divisor

def calculadora(numero_1, numero_2, opcao):
    if opcao == 1:
        print("A soma dos valores {} e {} é {}".format(numero_1, numero_2,soma(numero_1, numero_2)))
    elif opcao == 2:
        print("A diferença dos valores {} e {} é {}".format(numero_1, numero_2, subtracao(numero_1, numero_2)))
    elif opcao == 3:
        print("O produto dos valores {} e {} é {}".format(numero_1, numero_2, multplicar(numero_1, numero_2)))
    elif opcao == 4:
        print("O quociente dos valores {} e {} é {} com resto {}".format(numero_1, numero_2, dividir(numero_1, numero_2), numero_1 % numero_2))
    else:
        print("Opcão inválida!!!")

n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))
escolha = int(input("Selecione a opção:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n"))

print(calculadora(n1,n2,escolha))
