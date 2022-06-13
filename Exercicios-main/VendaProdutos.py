""" 
Um comerciante calcula o valor da venda, tendo em vista a tabela a seguir:
Valor da Compra Valor da Venda
Valor < R$ 10,00 - Lucro de 70%
R$ 10,00 ≤ Valor < R$ 30,00 - Lucro de 50%
R$ 30,00 ≤ Valor < R$ 50,00 - Lucro de 40%
Valor ≥ R$ 50,00 - Lucro de 30%
Criar um algoritmo que leia o valor da compra e imprima o valor da venda 
"""

ValorCompra = float(input("Entre com o valor da compra: "))

if ValorCompra < 10:
    Venda = 1.7 * ValorCompra 
elif ValorCompra < 30:
    Venda = 1.5 * ValorCompra
elif ValorCompra < 50:
    Venda = 1.4 * ValorCompra 
else:
    Venda = 1.3 * ValorCompra

print("Valor da venda: ", Venda)
