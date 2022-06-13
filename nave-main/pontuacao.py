from componente import Componente
import pygame

class Pontuacao(Componente):
  def __init__(self, estado):
    Componente.__init__(self, estado.largura / 2, estado.altura / 2, 100, 50, (255, 255, 255))
    self.fonte = pygame.font.Font(pygame.font.get_default_font(), 36)
    self.vivo = False

  def desenhar(self, estado):
    superficie_texto = self.fonte.render(f'{estado.pontuacao}', True, (0, 255, 0))
    estado.tela.blit(superficie_texto, dest=(self.x, self.y))
