""" 
Criar um algoritmo em PORTUGOL que informe a quantidade total de calorias de
uma refeição a partir do usuário que deverá informar o prato, a sobremesa e a bebida

Vegetariano 180 cal 
Abacaxi 75 cal 
Chá 20 cal
Peixe 230 cal 
Sorvete diet 110 cal 
Suco de laranja 70 cal
Frango 250 cal 
Mouse diet 170 cal 
Suco de melão 100 cal
Carne 350 cal 
Mouse chocolate 200 cal 
Refrigerante diet 65 cal
Sugestão: enumere cada opção de prato, sobremesa e bebida. Ou seja: Prato: 1 -
vegetariano, 2 – Peixe, 3 – Frango, 4 – Carne; Sobremesa: 1 – Abacaxi, 2 – Sorvete
diet, 3 – Mouse diet, 4 – Mouse chocolate; Bebida: 1 – Chá, 2 - Suco de laranja, 3 –
Suco de melão, 4 – Refrigerante diet.
"""
Prato1 = int(input("Prato 1:"))
Prato2 = int(input("Prato 2:"))
Prato3 = int(input("Prato 3:"))
Calorias = 0

if Prato1 == 1:
    Calorias += 180
elif Prato1 == 2:
    Calorias += 230
elif Prato1 == 3:
    Calorias += 250
elif Prato1 == 4:
    Calorias += 350
else:
    print("Operação inválida")

if Prato2 == 1:
    Calorias += 75
elif Prato2 == 2:
    Calorias += 110
elif Prato2 == 3:
    Calorias += 170
elif Prato2 == 4:
    Calorias += 200
else:
    print("Operação inválida")

if Prato3 == 1:
    Calorias += 20
elif Prato3 == 2:
    Calorias += 70
elif Prato3 == 3:
    Calorias += 100
elif Prato3 == 4:
    Calorias += 65
else:
    print("Operação inválida")

print("O total de calorias é: ", Calorias)