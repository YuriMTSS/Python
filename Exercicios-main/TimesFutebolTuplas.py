times = ('Chapecoense','Fortaleza','São Paulo','Corinthians','Palmeiras','Flamengo','Fluminense','Vasco','Curitiba','Ceara')

# Os times
print('='*30)
print(f'Os times são: {times}')

# Os 5 primeiros
print('='*30)
print(f'Os 5 primeiros são: {times[0:5]}')

# Os 4 últimos
print('='*30)
print(f'Os 4 últimos são: {times[-4:]}')

# Os times em ordem alfabetica
print('='*30)
print(f'Em ordem alfabética: {sorted(times)}')

# Em que posicao esta o time da chapecoense
print('='*30)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}º posição.')
print('='*30)



