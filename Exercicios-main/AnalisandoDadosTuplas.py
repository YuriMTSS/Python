numero = (int(input('Numero 1: ')),
          int(input('Numero 2: ')),
          int(input('Numero 3: ')),
          int(input('Numero 4: ')))

print(f'Você digitou os valores {numero}')
print(f'O valor 9 apareceu {numero.count(9)} vezes!')
if 3 in numero:
    print(f'O valor 3 apareceu na posição {numero.index(3) + 1}!')
else:
    print('Valor 3 não encontrado')
for i in numero:
    if i % 2 == 0:
        print(f'Os pares são: {i}', end='')
