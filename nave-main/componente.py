import pygame

class Componente:
  def __init__(self, x, y, largura, altura, cor):
    self.x = x
    self.y = y
    self.largura = largura
    self.altura = altura
    self.cor = cor
    self.vivo = True
    self.deve_remover = False
    self.jogador = False
    self.tiro = False

    self.x_inicial = x
    self.y_inicial = y

  def atualizar(self, estado):
    pass

  def desenhar(self, estado):
    pygame.draw.rect(estado.tela, self.cor, (self.x, self.y, self.largura, self.altura))

  def fora_da_tela(self, estado):
    if self.x < 0:
      return True
    if self.y < 0:
      return True
    if self.x + self.largura >= estado.largura:
      return True
    if self.y + self.altura >= estado.altura:
      return True
    return False

  def morreu(self, estado):
    self.vivo = False
    self.deve_remover = True
    estado.componentes.remove(self)

  def reset(self):
    self.x = self.x_inicial
    self.y = self.y_inicial
