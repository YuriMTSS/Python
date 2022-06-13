from componente import Componente
from tiro import Tiro
import pygame
from pygame.locals import *
import os

class Jogador(Componente):
  LARGURA = 50
  ALTURA = 80
  COR = (0, 255, 0)
  VELOCIDADE = 15
  TEMPO_RECARGA = 500

  def __init__(self, x, y):
    Componente.__init__(self, x, y, Jogador.LARGURA, Jogador.ALTURA, Jogador.COR)
    self.momento_ultimo_tiro = pygame.time.get_ticks()
    self.jogador = True

  def desenhar(self, estado):
    nave_img = pygame.image.load(f'images{os.path.sep}nave.png')
    nave_img = pygame.transform.scale(nave_img, (self.largura, self.altura))
    estado.tela.blit(nave_img, (self.x, self.y))

  def checar_tiro(self, estado):
    if pygame.time.get_ticks() - self.momento_ultimo_tiro < Jogador.TEMPO_RECARGA:
      return

    teclas_pressionadas = pygame.key.get_pressed()
    if teclas_pressionadas[K_SPACE]:
      self.momento_ultimo_tiro = pygame.time.get_ticks()
      tiro = Tiro(self.x, self.y)
      estado.componentes.append(tiro)

  def checar_reinicio(self, estado):
    if not estado.acabou():
      return

    teclas_pressionadas = pygame.key.get_pressed()
    if teclas_pressionadas[K_RETURN]:
      estado.reset()

  def morreu(self, estado):
    self.vivo = False

  def atualizar(self, estado):
    self.checar_tiro(estado)
    self.checar_reinicio(estado)
    teclas_pressionadas = pygame.key.get_pressed()

    if teclas_pressionadas[K_LEFT]:
      self.x -= Jogador.VELOCIDADE
    if teclas_pressionadas[K_RIGHT]:
      self.x += Jogador.VELOCIDADE

    if teclas_pressionadas[K_UP]:
      self.y -= Jogador.VELOCIDADE
    if teclas_pressionadas[K_DOWN]:
      self.y += Jogador.VELOCIDADE

    if self.x < 0:
      self.x = 0
    if self.x + Jogador.LARGURA > estado.largura:
      self.x = estado.largura - Jogador.LARGURA

    if self.y < 0:
      self.y = 0
    if self.y + Jogador.ALTURA > estado.altura:
      self.y = estado.altura - Jogador.ALTURA
