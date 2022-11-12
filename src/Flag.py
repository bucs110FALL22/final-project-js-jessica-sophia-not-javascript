import pygame
import random

class Flag(pygame.sprite.Sprite):

  def __init__(self):
    self.image = pygame.image.load()
    self.rect = self.image.get_rect()

  def change_players(self):
    self.player = random.randrange(0,2)
    if self.player == 0:
      return "PlayerOne has the flag"
    if self.player == 1:
      return "PlayerTwo has the flag"

  def change_color(self):
    self.image = pygame.image.load()

