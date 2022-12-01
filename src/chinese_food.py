import pygame

class Food(pygame.sprite.Sprite):
  def __init__(self):
  # makes the setup for screen where the building food is
    pygame.init()
    self.screen = pygame.display.set_mode() #keep same size all throughout game
    self.background.fill((246, 86, 77))
  # puts image of the bases, proteins, and veggies on certain locations of the screen
    self.noods = pygame.image.load("assets/noodles.png")
    self.noods_rect = self.noods.get_rect()
    self.noods_rect.x = 10
    self.noods_rect.y = 10
    self.rice = pygame.image.load("assets/rice.png")
    self.rice_rect = self.rice.get_rect()
    self.rice_rect.x = 20
    self.rice_rect.y = 10
    
    
  def base(self, x, y):
  # when user selects image, image goes to the position of the final food
    self.x = x
    self.y = y
    self.base_images = [
      "assets/rice.png",
      "assets/noodles.png"
    ]

  def protein(self, x, y):
  # when user selects image, image goes to the position of the final food
    self.x = x
    self.y = y
    self.protein_images = [
      "assets/chicken.png"
      "assets/beef.png"
      "assets/pork.png"
    ]
    
  def veggies(self, x, y):
  # when user selects image, image goes to the position of the final food
    self.x = x
    self.y = y
    self.veggies_images = [
      "assets/broccoli.png",
      "assets/pepper.png",
      "assets/carrots.png"
    ]