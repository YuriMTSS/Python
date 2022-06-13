"""Faça uma função que retorne o reverso de um número inteiro
informado. Por exemplo: 127 -> 721."""

# Ordem de precedencia // -> %

""" def inverso(numero):
    unidade = 0
    dezena = 0
    centena = 0
    milhar = 0

    unidade = numero % 10          # O resto da divisao por 10 imprime o ultimo numero da sequencia
    
    dezena = numero // 10 % 10     # A centena e dezena é extraida com a divisao inteira por 10 e o resto da divisao por 10 imprime a dezena
                                   # Se o numero tiver 4 digitos ele imprime os 3 primeiros, tira o resto da divisao que se mostra a dezena

    centena = numero // 100 % 10   # Divisao inteira por 100 pega a centena e unidade de milhar de 4 digitos

    milhar = numero // 1000 % 10   # A divisao inteira por 1000 imprime o primeiro numero de uma sequencia de 4 digitos

    print(unidade, dezena, centena, milhar)
 
numero = int(input("Numero inteiro de ate 4 digitos: "))
print(inverso(numero))
"""



unidade = 0
dezena = 0
centena = 0
milhar = 0
x = int
n = int(input("numero "))

x = len(n)

if x <= 0:
    print("Informe um número inteiro positivo")
elif x > 0 and x < 2:
    unidade = n % 10          # O resto da divisao por 10 imprime o ultimo numero da sequencia
elif x > 1 and x < 3:
    dezena = n // 10 % 10     # A centena e dezena é extraida com a divisao inteira por 10 e o resto da divisao por 10 imprime a dezena
elif x > 2 and x < 4:
    centena = n // 100 % 10   # Divisao inteira por 100 pega a centena e unidade de milhar de 4 digitos
elif x > 4 and x < 6:
    milhar = n // 1000 % 10   # A divisao inteira por 1000 imprime o primeiro numero de uma sequencia de 4 digitos

print(unidade, dezena, centena, milhar)
