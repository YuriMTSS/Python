import pygame
from pygame.locals import *
from componente import Componente
from estado import Estado
from jogador import Jogador
from inimigo import Inimigo
from pontuacao import Pontuacao
from tempo import Tempo
import sys

LARGURA_TELA = 800
ALTURA_TELA = 600
FPS = 30

pygame.init()
relogio = pygame.time.Clock()
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
estado = Estado(tela, LARGURA_TELA, ALTURA_TELA, FPS)

jogador = Jogador(LARGURA_TELA / 2, ALTURA_TELA - 100)

estado.componentes.append(jogador)

estado.componentes.append(Inimigo(50, 50))
estado.componentes.append(Inimigo(250, 50))
estado.componentes.append(Inimigo(99, 50))

pontuacao = Pontuacao(estado)
estado.componentes.append(pontuacao)

estado.componentes.append(Tempo())

fonte_fim_jogo = pygame.font.Font(pygame.font.get_default_font(), 36)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)

    tela.fill((0, 0, 0))

    for componente in estado.componentes:
      componente.atualizar(estado)

    if estado.acabou():
      superficie_texto = fonte_fim_jogo.render(f'Pontuacao Final: {estado.pontuacao}', True, (0, 255, 0))
      estado.tela.blit(superficie_texto, dest=(LARGURA_TELA / 2 - 100, ALTURA_TELA / 2))
    else:
      for componente in estado.componentes:
        componente.desenhar(estado)

    pygame.display.update()
    relogio.tick(FPS)


