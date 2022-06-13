from componente import Componente
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


class Tiro(Componente):
  LARGURA = 30
  ALTURA = 60
  COR = (255, 0, 0)
  VELOCIDADE = 30

  def desenhar(self, estado):
    p1 = (self.x, self.y + self.altura)
    p2 = (self.x + self.largura // 2, self.y)
    p3 = (self.x + self.largura, self.y + self.altura)
    p4 = (self.x + self.largura // 2, self.y + self.altura // 2)
    pygame.draw.polygon(estado.tela, self.cor, [p1, p2, p3, p4])
    pygame.draw.rect(estado.tela, self.cor, (self.x + self.largura * 0.3, self.y + self.altura * 0.3, self.largura * 0.4, self.altura))

  def __init__(self, x, y):
    Componente.__init__(self, x, y, Tiro.LARGURA, Tiro.ALTURA, Tiro.COR)
    self.tiro = True

  def atualizar(self, estado):
    self.y -= Tiro.VELOCIDADE

    for componente in estado.componentes:
      if componente != self and componente.vivo and not componente.jogador:
        if colidiu(self, componente):
          self.morreu(estado)
          componente.morreu(estado)
          estado.pontuacao += 10
          return
