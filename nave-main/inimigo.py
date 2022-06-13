from componente import Componente
import random
import pygame
import math

def colidiu(componente1, componente2):
  x1, y1 = componente1.x, componente1.y
  x2, y2 = componente2.x, componente2.y

  r1 = componente1.largura / 2
  r2 = componente2.largura / 2

  d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

  if d > (r1 + r2):
    return False
  return True

def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)

  return (r, g, b)

class Inimigo(Componente):
  LARGURA = 40
  ALTURA = 60
  CORES = [random_color() for _ in range(100)]
  VELOCIDADE = 2

  def __init__(self, x, y):
    Componente.__init__(self, x, y, Inimigo.LARGURA, Inimigo.ALTURA, random.choice(Inimigo.CORES))

  def desenhar(self, estado):
    if not self.vivo:
      tempo_animacao = 1000.0
      tempo_passou = pygame.time.get_ticks() - self.momento_morte
      fracao = 1 - (tempo_passou / tempo_animacao)

      self.largura = Inimigo.LARGURA * fracao
      self.altura = Inimigo.ALTURA * fracao
      self.x = self.x + Inimigo.LARGURA * (1 - fracao) * 0.5
      self.y = self.y + Inimigo.ALTURA * (1 - fracao) * 0.5
      self.cor = (0, 0, max(0, min(255, 255 * fracao)))

      if tempo_passou > tempo_animacao:
        Componente.morreu(self, estado)
        estado.componentes.append(Inimigo(random.randint(0, estado.largura-Inimigo.LARGURA), 50))

    Componente.desenhar(self, estado)

  def morreu(self, estado):
    self.vivo = False
    self.momento_morte = pygame.time.get_ticks()

  def atualizar(self, estado):
    if not self.vivo:
      return

    self.y += Inimigo.VELOCIDADE
    if self.fora_da_tela(estado):
      self.morreu(estado)
      
    for componente in estado.componentes:
      if componente.jogador and colidiu(self, componente):
        self.morreu(estado)
        componente.morreu(estado)
