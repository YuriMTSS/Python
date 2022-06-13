n1 = int(input("Entre com o primeiro valor: "))
n2 = int(input("Entre com o segundo valor: "))

soma = n1 + n2
if soma > 20:
    soma += 8
    print (soma)
elif soma <= 20:
    soma -= 5
    print(soma)

