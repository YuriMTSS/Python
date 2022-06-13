from random import randint
def Numero_Aleatorio():
    print('Sou seu computador!')
    nome = str(input('Informe seu nome: '))
    menor = int(input('Informe o menor valor: '))
    maior = int(input('Informe o maior valor: '))
    computador = randint(menor, maior)
    print('Ola {}, pensei em um número entre {} e {}, vamos ver se pode advinhar!'.format(nome, menor, maior))

    acertou = False
    tentativas = 0

    while not acertou:
        jogador = int(input('Informe seu palpite: '))
        tentativas += 1

        if jogador == computador:
            acertou = True
        else:
            if jogador < computador:
                print('Mais.. Tente de novo!')
            if jogador > computador:
                print('Menos... Tente de novo!')
                
    if tentativas == 1:
        print('O número era {}'.format(computador))
        print('Perfeito {}, acertou de primeira'.format(nome))
    if tentativas >= 2 and tentativas <= 3:
        print('\nVocê acertou, o número era {}'.format(computador))
        print('Excelente {}, conseguiu em {} tentativas'.format(nome, tentativas))
    if tentativas >= 4 and tentativas <= 6:
        print('\nVocê acertou, o número era {}'.format(computador))
        print('Boa {}, conseguiu em {} tentativas'.format(nome, tentativas))
    if tentativas > 6:
        print('\nVocê acertou, o número era {}'.format(computador))
        print('Continue praticando {} a prática leva a perfeição, conseguiu em {} tentativas'.format(nome, tentativas))

Numero_Aleatorio()
