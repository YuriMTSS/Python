from random import randint

jogador_vence = 0
computador_vence = 0

while True:
    jogador = int(input('\nInforme um valor: '))

    computador = randint(0,10)
    total = jogador + computador
    par_impar = ' '
    
    while par_impar not in 'PI':
        par_impar = str(input('Escolha: [P/I]')).strip().upper()[0]
    
    print(f'O jogador jogou {jogador} e o computador {computador}. Total de {total}')

    if par_impar == 'P' and total % 2 == 0:
        jogador_vence += 1
        print(f'\nJogador: {jogador_vence}')
        print(f'Computador: {computador_vence}')
    
    elif par_impar == 'I' and total % 2 == 1:
        jogador_vence += 1
        print(f'\nJogador: {jogador_vence}')
        print(f'Computador: {computador_vence}')
    else:
        computador_vence += 1
        print(f'\nJogador: {jogador_vence}')
        print(f'Computador: {computador_vence}')

    if computador_vence != 0:
        print('\nFim de jogo!')
        break
