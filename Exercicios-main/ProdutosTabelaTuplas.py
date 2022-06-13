listagem_produtos = ('Lapis', 1.75,
                     'Caderno', 10.90,
                     'Livro', 31.95,
                     'Estojo', 21.35,
                     'Agenda', 31.99)

print('='*30)
print('------Listagem de preços------')
print('='*30)

for pos in range(0, len(listagem_produtos)):
    if pos % 2 == 0:
        print(f'{listagem_produtos[pos]:.<30}',end='')
    else:
        print(f'R$ {listagem_produtos[pos]:.2f}')

print('='*30)

