import pygame

class Estado:
  def __init__(self, tela, largura, altura, fps, duracao=20):
    self.tela = tela
    self.largura = largura
    self.altura = altura
    self.fps = fps
    self.duracao = duracao
    self.componentes = []
    self.pontuacao = 0
    self.inicio = pygame.time.get_ticks()

  def pegar_jogador(self):
    for componente in self.componentes:
      if componente.jogador:
        return componente
    return None

  def acabou(self):
    if ((pygame.time.get_ticks() - self.inicio) / 1000.0) > self.duracao:
      return True
    if not self.pegar_jogador().vivo:
      return True
    return False

  def reset(self):
    self.inicio = pygame.time.get_ticks()
    self.pontuacao = 0
    self.pegar_jogador().vivo = True
    for componente in self.componentes:
      if componente.tiro:
        self.componentes.remove(componente)
      else:
        componente.reset()
