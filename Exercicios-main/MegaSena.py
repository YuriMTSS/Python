"""from random import randint
from time import sleep
tot_jogadas = 1
lista = []
jogos = []

print('-'*30)
print('     JOGO MEGA SENA     ')
print('-'*30)

qtd_jogos = int(input('Total de jogos sorteados: '))

while tot_jogadas <= qtd_jogos:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break

    lista.sort()
    jogos.append(lista[:]) # Copia a lista
    lista.clear() # Depois de copiar a lista ela é salva em jogos e apagada
    tot_jogadas += 1
print()
print('-=' * 3, f' SORTEANDO {qtd_jogos} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('-=' * 5, ' BOA SORTE ', '-=' * 5)
"""

from random import randint
from time import sleep
print('-' * 40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-' * 40)
quantidade_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'=-=-=-= SORTEANDO {quantidade_jogos} JOGOS =-=-=-=')
sleep(1)
for c in range(0, quantidade_jogos):
    jogo = []
    while len(jogo) != 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    print(f'Jogo {c + 1}: {sorted(jogo)}')
    sleep(1)
print('=-=-=-=-= < BOA SORTE! > =-=-=-=-=')

""" from random import sample

q = int(input('Quantas apostas gerar? '))
nums = [sample(range(1,61), k=6) for x in range(0,q)]

for i in range(0,q):
    print(f'Aposta {i+1}: {sorted(nums)[i]}')
 """