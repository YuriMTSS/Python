""" Faça um programa que leia 5 números e informe a soma e a média dos números. """

contador = 0
soma = 0
while contador < 5:
    numero = float(input("Informe o número: "))
    soma += numero

    contador += 1
    media = soma / contador

print("Soma: ", soma)
print("Média: ",media)


