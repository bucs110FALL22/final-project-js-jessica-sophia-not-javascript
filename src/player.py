import pygame

class Player(pygame.sprite.Sprite):
  def __init__(self, x, y):
    #library for player options
    self.player_images = [
      "assets/playergirl.png",
      "assets/playerboy.png",
      "assets/playergen.png"
    ]
    #asks user what player they want to be
    player = None
    player = input("What gender would you like your player to be? Your options are: female, male, gender neutral")
    if player == "female":
      self.player = pygame.image.load(self.player_images[0])
    elif player == "male":
      self.player == pygame.image.load(self.player_images[1])
    elif player == "gender neutral":
      self.player == pygame.image.load(self.player_image[2])
    else:
      while player != "female" or "male" or "gender neutral":
        print("Sorry. That is not one of the options.")
    #self.player = pygame.transform.scale(self.player, size)
    self.rect = self.player.get_rect()
    
    self.x = x
    self.y = y
    x = 0
    y = 0