palavras = ('Aprender', 'Programar', 'Atualizar', 'Usuario', 'Portugal', 'Lendarios')

for i in palavras:
    print(f'\nNa palavra {i.upper()} temos as vogais: ',end=' ')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(f'{letra}',end=' ')