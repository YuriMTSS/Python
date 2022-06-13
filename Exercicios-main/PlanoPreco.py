# Criar um algoritmo que entre com a idade de uma pessoa e imprima o valor que ela deverá
# pagar do plano de saúde, segundo a seguinte tabela:
# Até 10 anos R$ 30,00
# Acima de 10 até 29 anos R$ 60,00
# Acima de 29 até 45 anos R$ 120,00
# Acima de 45 até 59 anos R$ 150,00
# Acima de 59 até 65 anos R$ 250,00
# maior que 65 anos R$ 400,00

idade = int(input("Informe a idade da pessoa: "))

if idade <= 10:
    print("Mensalidade: R$ 30,00")
elif idade <= 29:
    print("Mensalidade: R$ 60,00")
elif idade <= 45:
    print("Mensalidade: R$ 120,00")
elif idade <= 59:
    print("Mensalidade: R$ 150,00")
elif idade <= 65:
    print("Mensalidade: R$ 250,00")
else:
    print("Mensalidade: R$ 400,00")

