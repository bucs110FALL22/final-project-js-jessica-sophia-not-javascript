import pygame

class PlayerOne:
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.x = x
    self.y = y
    x = 0
    y = 0
    self.location = (x,y)
    self.image = pygame.image.load()
    self.rect = self.image.get_rect()

  def move(self, x, y):
    for event in pygame.event.get():
      #player jumps
      if event.type == pygame.K_w:
        self.y = 1
        pygame.time.wait(10)
        self.y = 0
      #player move left and right
      if event.type == pygame.K_a:
        self.x -= 1
      elif event.type == pygame.K_d:
        self.x += 1