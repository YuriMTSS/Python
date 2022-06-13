from time import sleep
from random import randint
from operator import itemgetter
jogadores = {
    'Jogador1': randint(1,6),
    'Jogador2': randint(1,6),
    'Jogador3': randint(1,6),
    'Jogador4': randint(1,6),
}
ranking = []

print('Valores sorteados: ')
for c, v in jogadores.items():
    print(f'{c} tirou o valor {v} no dado.')
    sleep(1)
ranking = sorted(jogadores.items(), key = itemgetter(1), reverse = True)

print()
print('===  RANKING DOS JOGADORES   ===')
for i, v in enumerate(ranking):
    print(f'    {i + 1}º lugar: {v[0]} com {v[1]}.')

