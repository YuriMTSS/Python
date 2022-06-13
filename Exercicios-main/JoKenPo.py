# Faça um jogo de pedra papel e tesoura com o computador
import random

class game:
    def __init__(self):
        self.pedra = 0
        self.papel = 1
        self.tesoura = 2

    def Iniciar(self):
        while True:
            try:                
                print('{:=^40}'.format(' JO KEN PÔ '))
                print('\n0- Pedra\n1- Papel\n2- Tesoura\n')
                usuario = int(input('Informe sua escolha: '))

                computador = random.randint(0,2)
                print(computador)   

                # Casos que o computador ganha
                if usuario < 0 and usuario > 2:
                    print('Informe um numero entre 0 e 2')
                else:
                    if usuario == 0 and computador == 1:
                        print('Computador ganhou com papel')
                    if usuario == 1 and computador == 2:
                        print('Computador ganhou com tesoura')
                    if usuario == 2 and computador == 0:
                        print('Computador ganhou com pedra')

                    # Casos que o usuario ganha
                    if usuario == 0 and computador == 2:
                        print('Usuário ganhou com pedra')
                    if usuario == 1 and computador == 0:
                        print('Usuario ganhou com papel')
                    if usuario == 2 and computador == 1:
                        print('Usuario ganhou com tesoura')

                    # Se der empate
                    if usuario == computador:
                        print('Empate')

                    continuar = input('Continuar? [s,n]')
                    if continuar is not 'Ss':
                        print('Obrigado por jogar')
                        break
            except:
                print('Informe apenas os valores inteiros!')

jogo = game()
jogo.Iniciar()