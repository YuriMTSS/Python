"""Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de conta. 
    - O programa deverá solicitar ao usuário o valor da prestação 
    - O número de dias em atraso e passar estes valores para a função valorPagamento 
    que calculará o valor a ser pago e devolverá este valor ao programa que a chamou 
    - O programa deverá então exibir o valor a ser pago na tela. 
    - Após a execução o programa deverá voltar a pedir outro valor de prestação ate um valor 0 ser digitado.
    - O cálculo do valor a ser pago é feito da seguinte forma:
        - Para pagamentos sem atraso, cobrar o valor da prestação 
        - Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
    - O programa deverá ser encerrado, exibindo o relatório do dia, que conterá:
        - a quantidade e o valor total de prestações pagas no dia."""

def valorPagamento(vp, da):                         # vp = valor da prestação ///// da = dias em atraso
    if da < 1:                                      # se não tiver dias em atraso ele retorna o valor da prestação
        return vp
    else:
        return vp + 0.03 * vp + (0.001 * vp) * da

valor = []
valor_total = 0
cont = 0

while True:
       valor_prestacao = float(input('Valor da prestacao: '))
       dias_atraso = int(input('Dias em atraso: '))

       if valor_prestacao == 0:                     # Se o valor da prestação for 0 o loop quebra
            break
       cont += 1

       valor_total += valor_prestacao               # Soma o total
       valor.append(valorPagamento(valor_prestacao, dias_atraso)) # Senao passa pela funcao e depois entra na lista com o novo valor

print('\nRelatorio do dia, foram pagas {} prestacoes nos valores: {}' .format(cont, valor))
print('Valor total de prestacoes pagas: {}'.format(valor_total))
D