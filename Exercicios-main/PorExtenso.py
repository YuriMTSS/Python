contar = ('zero','um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

continuar = ''
while continuar in 'Ss':
    while True:
        numero = int(input('Digite um numero entre 0 e 20: '))
        if 0 <= numero <= 20:
            break
        print('Tente novamente!',end='')
    print(f'Você digitou {contar[numero]}')

    continuar = str(input('Continuar?\n[S/N]')).strip().upper()[0]
    while continuar not in 'SsNn':        
        continuar = str(input('Informe apenas S ou N: ')).strip().upper()[0]

    if continuar in 'Nn':
        break


