from tkinter import font
import pygame, sys
from pygame.locals import *
from random import randint

# Funções para o jogo
def mensagem_fim_jogo():
    texto = 'GAME OVER' # Armazena o texto
    pygame.font.init() # Inicia a fonte
    fonte = pygame.font.get_default_font() # Carrega com a fonte padrão
    fonte_padrao = pygame.font.SysFont(fonte, 40) # Usa a fonte padrão
    texto_tela = fonte_padrao.render(texto, 1, (preto)) # Coloca o texto na cor desejada
    tela.blit(texto_tela, (200,250)) # Coloca na posição da tela

def coisas_na_tela():
    texto = 'Snake Game' # Armazena o texto
    pygame.font.init() # Inicia a fonte
    fonte = pygame.font.get_default_font() # Carrega com a fonte padrão
    fonte_padrao = pygame.font.SysFont(fonte, 30) # Usa a fonte padrão
    texto_tela = fonte_padrao.render(texto, 1, (vermelho)) # Coloca o texto na cor desejada
    tela.blit(texto_tela, (230,10)) # Coloca na posição 50, 900 da tela

def posicao_comida_par():
    x = randint(0, 59) * 10
    y = randint(0, 59) * 10
    # return (x // 10 * 10, y // 10 * 10) # Se for um numero com casa decimal ele pega o inteiro e retorna o valor * 10
    return(x,y)
def colisao(celula1, celula2):
    return(celula1[0] == celula2[0]) and (celula1[1] == celula2[1])
#===============================================================================================================================================================

pygame.init()

# Definindo cores
preto = (0,0,0)
ciano = (0,255,255)
vermelho = (255,0,0)
azul = (0,0,255)
verde = (0,255,0)
branco = (255,255,255)
#===============================================================================================================================================================

# Tela
largura_tela = 600
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Yuri') # Título na tela
#===============================================================================================================================================================

# Cores da tela
cor_fundo = (ciano) # Cor ciano
tela.fill(cor_fundo) # Coloca a cor na tela
#===============================================================================================================================================================

# Cobra
# Uma cobra é uma lista de segmentos
cobra = [(200, 200), (210, 200), (220, 200)] # Posição 

UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3
direcao_cobra = LEFT

relogio = pygame.time.Clock() # Controla a velocidade da cobra

imagem_cobra = pygame.Surface((10,10)) # Desenha formas simles, gira, escala a figura
imagem_cobra.fill(vermelho) # Cor da cobra


posicao_comida = posicao_comida_par() # Quadrinhos de tamanho 10, então 590 é o máximo.
comida_cobra = pygame.Surface((10,10))
comida_cobra.fill(azul) # Cor da comida

#===============================================================================================================================================================
while True:
    relogio.tick(10) # Velocidade da cobra
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # Colocando a cobra na tela
    # Um blit significa basicamente cópia de cores de pixel de uma imagem para outra. 
    # Nós passamos ao método blit uma fonte Surface para ele copiar e uma posição para colocar a fonte no destino.
    tela.fill((cor_fundo)) # Limpa a tela
    coisas_na_tela()
    tela.blit(comida_cobra, posicao_comida)
    for posicao in cobra:
        tela.blit(imagem_cobra, posicao)

#===============================================================================================================================================================
    # Movimentando a cobra
        if event.type == KEYDOWN:
            # Pega a chave que direciona a cobra e verifica se seu oposto esta sendo precionado 
            # Esta indo a direita e aperta a esquerda, ele ignora e continua a esquerda
            # Se estiver sendo precionado ele segue reto e ignora seu comando de direção oposta
            if event.key == K_UP and direcao_cobra != DOWN:
                direcao_cobra = UP
            if event.key == K_DOWN and direcao_cobra != UP:
                direcao_cobra = DOWN
            if event.key == K_RIGHT and direcao_cobra != LEFT:
                direcao_cobra = RIGHT
            if event.key == K_LEFT and direcao_cobra != RIGHT:
                direcao_cobra = LEFT

    # Mechendo na cabeça da cobra, a cobra é uma lista, então posições 0 1 são a cabeça
    if direcao_cobra == UP:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10) # (x,y)
    if direcao_cobra == DOWN:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10) 
    if direcao_cobra == RIGHT:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1]) 
    if direcao_cobra == LEFT:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1]) 
    

    # Mechendo o resto do corpo da cobra
    # Cada posição do corpo da cobra vai ocupar a posição que a cabeça estava ocupando.
    for i in range(len(cobra) - 1, 0, -1): # Pega o comprimento da lista, começa do final e vai ate 0, -1 para decrementar
        # Então pega a ultima posicao da lista e coloca no lugar que a posicao anterior estava, por isso -1
        cobra[i] = (cobra[i - 1][0], cobra[i - 1][1])
#===============================================================================================================================================================
    # Checando colisões
    if colisao(cobra[0], posicao_comida):
        posicao_comida = posicao_comida_par()
        cobra.append((0,0)) # Quando a cobra passar na posicao da comida e colidir com ela, ela tomar a posicao e crescer

    # Matando a cobra

    # Checando se a cobra chega nos limites da janela
    # Pega a cabeça da cobra (posicoes 0 e 1) e verifica que a posicao passa do limite da tela
    if cobra[0][0] == largura_tela or cobra[0][1] == altura_tela or cobra[0][0] < 0 or cobra[0][1] < 0:
        mensagem_fim_jogo()
        break

    # Se ela se morde
    # Sendo a cobra uma lista, pegamos o comprimento dela e verificamos se a cobra atacou algum componente da lista
    #for i in range(1, len(cobra) - 1):
        # Cabeça da cobra [0][0], algum componente [i][0]
     #   if cobra[0][0] == cobra[i][0] and cobra[0][1] == cobra[i][1]:
      #      mensagem_fim_jogo()
       #     break

#===============================================================================================================================================================
    pygame.display.update()
