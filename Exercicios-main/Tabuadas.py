def tabuada_soma():
    while True:
        try:    
            valor = int(input('\nQuer ver tabuada de qual valor: '))
            for c in range(1, 11):
                print(f'{valor} + {c} = {c + valor}')
            pergunta = str(input('Outra tabuada desse operador [S/N]?\n'))        
            if pergunta in 'Nn':
                break
        except:
            print('Informe um valor aceitável')

def tabuada_subtracao():
    while True:
        try:    
            valor = int(input('\nQuer ver tabuada de qual valor: '))
            for c in range(1, 11):
                print(f'{valor} - {c} = {c - valor}')
            pergunta = str(input('Outra tabuada desse operador [S/N]?\n'))        
            if pergunta in 'Nn':
                break
        except:
            print('Informe um valor aceitável')

def tabuada_multplicacao():
    while True:
        try:        
            valor = int(input('\nQuer ver tabuada de qual valor: '))
            for c in range(1, 11):
                print(f'{valor} x {c} = {c * valor}')
            pergunta = str(input('Outra tabuada desse operador [S/N]?\n'))        
            if pergunta in 'Nn':
                break
        except:
            print('Informe um valor aceitável')

def tabuada_divisao():
    while True:
        try:        
            valor = int(input('\nQuer ver tabuada de qual valor: '))
            for c in range(1, 11):
                produto_divisao = c * valor
                print(f'{produto_divisao} / {valor} = {produto_divisao // valor}')
            
            pergunta = ''
            while pergunta not in 'SsNn':
                pergunta = str(input('Outra tabuada desse operador [S/N]?\n'))        
                if pergunta in 'Nn':
                    break
        except:
            print('Informe um valor aceitável')


def menu():
    while True:    
        try:    
            print('\nEscolha uma opção: ')
            menu = int(input('1- Soma\n2- Subtração\n3- Multplicação\n4- Divisão\n5- Sair do programa!\n\n'))

            if menu == 1:
                tabuada_soma()    
            if menu == 2:
                tabuada_subtracao()
            if menu == 3:
                tabuada_multplicacao()
            if menu == 4:
                tabuada_divisao()

            if menu == 5:
                print('='*30)
                print('     FIM DO PROGRAMA!     ')
                print('='*30)
                break
        except:
            print('Valor inválido!')

menu()
