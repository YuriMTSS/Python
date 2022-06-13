import random

def print_forca(forca):
    print(' '.join(forca).upper())

palavras = ['progrma', 'arquivo', 'texto', 'aleatoriamente', 'jogador', 'enforcado']
palavra = random.choice(palavras)
forca = ['_' for _ in range(len(palavras))]
erros = 0
ganhou = False

while erros < 6 and not ganhou:
    print_forca(forca)
    print('Digite uma letra: ')
    chute = str(input()).lower()

    if chute not in palavra:
        erros += 1
        print('Você errou pela {} vez! {} tentativas restantes'.format(erros, 6 - erros))
        continue

    for index, letra in enumerate(palavra):
        if letra == chute:
            forca[index] = chute
    
    if '_' not in forca:
        ganhou = True

if ganhou:
    print("You Win!")
else:
    print("You Lose!")
print_forca(forca)


