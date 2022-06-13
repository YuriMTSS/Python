from rich import print
import os

VOTO_BOLSONARO = 0
VOTO_LULA = 0
NULOS_BRANCOS = 0

while True:

    print('*'*20)
#    print(f'[on blue]Total Bolsonaro: [/]{VOTO_BOLSONARO}{os.linesep}[on red]Total Lula: [/]{VOTO_LULA}{os.linesep}[on grey]Nulos e Brancos: [/]{NULOS_BRANCOS}')
    print(f'[on blue]Total Bolsonaro: [/]{VOTO_BOLSONARO}\n[on red]Total Lula: [/]{VOTO_LULA}\n[on grey]Nulos e Brancos: [/]{NULOS_BRANCOS}')

    print('*'*20)

    try:
#        voto = int(input(f'Para quem gostaria de votar?{os.linesep}1 - Bolsonaro{os.linesep}2 - Lula{os.linesep}Seu voto: '))
        voto = int(input(f'Para quem gostaria de votar?\n1 - Bolsonaro\n2 - Lula\nSeu voto: '))

        if voto == 1:
            VOTO_BOLSONARO += 1
        elif voto == 2:
            VOTO_LULA +=1
        else:
            NULOS_BRANCOS += 1
    except:
        print('Informe só números inteiros!!!')
    os.system('cls')
