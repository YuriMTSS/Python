# A CEF concederá um crédito especial com juros de 2% aos seus clientes de acordo
# com o saldo médio no último ano. Faça um algoritmo que leia o
# saldo médio de um cliente e calcule o valor do crédito de acordo com a tabela a seguir:

# De 0 a 500 - Nenhum crédito
# De 501 a 1000 - 30% do valor do saldo médio
# De 1001 a 3000 - 40% do valor do saldo médio
# Acima de 3001 - 50% do valor do saldo médio 
# Imprimir uma mensagem informando o saldo médio e o valor de crédito. 

SaldoMedio = float(input("Entre com o saldo médio: "))

if SaldoMedio <= 500:
    Credito = 0
elif SaldoMedio <= 1000:
    Credito = 0.3 * SaldoMedio
elif SaldoMedio <= 3000:
    Credito = 0.4 * SaldoMedio
else:
    Credito = 0.5 * SaldoMedio

print("Saldo médio: ", SaldoMedio)
print("Crédito especial: ", Credito)