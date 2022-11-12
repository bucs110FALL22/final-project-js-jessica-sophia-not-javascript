import pygame
import random
from PlayerOne import PlayerOne
from PlayerTwo import PlayerTwo

class Projectile(pygame.sprite.Sprite):
  def __init__(self, x, y):
    self.location = (x,y)
    self.time = random.randrange()
    self.image = pygame.image.load()
    self.rect = self.image.get_rect()
  
  def change_speed(self):
    self.speed = random.randrange(0, 11)

  def slow_player_on_hit(self):
    if self.location == playerOne.location:
      PlayerOne.location = (0,0)
      return "hit"
    if self.location == playerTwo.location:
      PlayerTwo.location = (0,0)
      return "hit"
    
  def change_size(self):
    self.size = 2