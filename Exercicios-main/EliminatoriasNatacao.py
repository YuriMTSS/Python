# A confederação brasileira de natação irá promover eliminatórias para o próximo
# mundial. Fazer um algoritmo em PORTUGOL que receba a idade de um nadador e
# determine (imprima) a sua categoria segundo a tabela a seguir:
# Categoria Idade
# Infantil A 5 – 7 anos
# Infantil B 8 – 10 anos
# Juvenil A 11 – 13 anos
# Juvenil B 14 – 17 anos
# Sênior Maiores de 18 anos 

idade = int(input("Informe a idade do nadador: "))

if idade < 5:
    print("Não é nadador")
elif idade <= 7:
    print("Infantil A")
elif idade <= 10:
    print("Infantil B")
elif idade <= 13:
    print("Juvenil A")
elif idade <= 17:
    print("Juvenil B")
else:
    print("Sênior maiores de 18")
