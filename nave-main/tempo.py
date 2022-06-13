from componente import Componente
import pygame

class Tempo(Componente):
  def __init__(self):
    Componente.__init__(self, 0, 0, 15, 0, (0, 255, 0))
    self.vivo = False

  def atualizar(self, estado):
    passou = (pygame.time.get_ticks() - estado.inicio) / 1000.0
    fracao = passou / estado.duracao
    self.altura = estado.altura * fracao
