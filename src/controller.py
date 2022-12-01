import pygame
from src.menu_screen import Menu
from src.customer import Customer
from src.player import Player
from src.tips import Tips
from src.chinese_food import Food
## state for current gamemode
## conditions to change out of states
## if in game show this screen
class Controller:
  
  def __init__(self):
    self.screen = Menu()
    self.user = Player()
    self.customer = Customer()

  def startloop(self):
    '''
    The user selects the start button from the menu_screen.py and the screen changes to the order station
    '''
    #select state loop
    start = False
    while start:
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
          #if player select start
          self.background = pygame.image.load("assets/orderBackground.png")
          start = True


  def mainloop(self):
    '''
  The user clicks the bases and toppings to create the ordered food to their memory and then presses the finished button and the total tips are returned 
  '''

    #customer moves across the screen and orders
    Bob = Customer()
    Bob.order()
    # order will stay on screen for 10 sec
    print("Reminder: In this game you have 10 seconds to memorize the order. The more accurate the food you make is, the more tips you get.")
    
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        #if player select base
        select = Food()
        select.base(100, 20)
    maingame = False
    while maingame:
      mouse = pygame.mouse.get_pos()
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
          if mouse[0] > 50 and mouse[1] < 50:
            Total_tips = Tips()
            return Total_tips
        
        

        
  ### below are some sample loop states ###
  
    
      #event loop
      #update data
      #redraw
    
  # def gameloop(self):
  #     #event loop
  #     #update date
  #     #redraw
  # def gameoverloop(self):
  #     #event loop
  #     #update data
  #     #redraw
