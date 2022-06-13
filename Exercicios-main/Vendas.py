"""Programa que calcule valor a ser pago por um produto
    A vista: Dinheiro/Cheque (10% desconto)
    A vista cartão: 5% desconto
    Até 2x no cartão: preço normal
    Mais de 2x: 20% juros"""

class Loja:
    def __init__(self):
        self.forma_pagamento = '\n1- A vista: Dinheiro/Cheque\n2- A vista cartão\n3- Até 2x no cartão\n4- Mais de 2x no cartão'

    def Iniciar(self):
        try:    
            print('{:=^40}\n'.format(' LOJA YURI '))
            preco = float(input('Informe o total da compra: '))
            print(self.forma_pagamento)
            escolha = int(input('\nEscolha a forma de pagamento: '))

            if escolha == 1:
                desconto = preco - (0.1 * preco)
                print('O total da compra foi {} então você deva pagar {}.'.format(preco, desconto))
            elif escolha == 2:
                desconto = preco - (0.05 * preco)
                print('O total da compra foi {} então você deva pagar {}.'.format(preco, desconto))
            elif escolha == 3:
                parcela = preco / 2
                print('O total da compra foi {} então você pagar 2x de {}'.format(preco, parcela))
            elif escolha == 4:
                parcelas = int(input('Total de parcelas: '))
                desconto = preco + (0.2 * preco)
                juros = (desconto) / parcelas
                print('O total da compra foi {} parcela por {:.2f} com juros'.format(preco, juros))
        except:
            print('Informação inválida! Informe apenas números!')
            self.Iniciar()


loja = Loja()
loja.Iniciar()