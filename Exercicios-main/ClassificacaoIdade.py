# Escreva um algoritmo em PORTUGOL que dada a idade de uma pessoa, determine
# sua classificação segundo a seguinte tabela:
# - maior de idade;
# - menor de idade;
# - pessoa idosa (idade superior ou igual a 65 anos).

idade = int(input("Idade: "))

if idade < 18:
    print("Menor de idade")
elif idade >= 18 and idade < 65:
    print("Maior de idade")
else:
    print("Idosa")
    