import pygame
import random

class Customer(pygame.sprite.Sprite):
  ## loading sprite image
  
  def __init__(self, pos_x, pos_y):
    super().__init__()
    self.image = pygame.image.load("../assets/customer.png")
    self.rect = self.image.get_rect()
    
  def move_start(self):
    '''
    After the user starts the game, the customer walks to the player to order food.
    parameters: self
    return: (type)
    '''
    pass

  def order(self):
  # order is randomized each game
    self.base_order = ["rice", "noodles"]
    self.protein_order = ["chicken", "beef", "pork"]
    self.veggies_order = ["broccoli", "peppers", "carrots"]
    print(random.choice(self.base_order))
  # will make it so that the number of protein and veggies they order is random tmr
    print(random.choice(self.protein_order))
    print(random.choice(self.veggies_order))
    
## customer object
customer = Customer(50, 50)
customer_group = pygame.sprite.Group()
customer_group.add(customer)
pygame.sprite.Group.draw()




    

    # if player clicks start, screen changes to a different background and the customer walks from the right to the left, where the player is 
    
  