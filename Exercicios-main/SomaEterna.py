soma = 0
while True:
    numero = float(input("Digite 0 para parar o loop: "))
    if numero == 0:
        break
    soma += numero
    print(soma)