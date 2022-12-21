import pygame
from .base_scene import BaseScene
from .ordering_scene import OrderingScene
from ..components import Textbox, Image

class DiningCustomerScene(BaseScene):
  def __init__(self, context):
    """
	  Provides context to the scene
    """
    BaseScene.__init__(self, BaseScene)
    self.context = context
    self.sceneService = context["scene"]

    self.order_image = Image(
      r"./assets/orderBackground.png",
      (0, 0),
      lambda img : pygame.transform.scale(img, (750, 500))
    )
    self.player = Image(
      r"./assets/playerboy.png",
      (20, 208),
      lambda img : pygame.transform.flip(img, True, False),
      lambda img : pygame.transform.scale(img, (140, 280))
    )
    
    self.customer = Image(
      r"./assets/customer.png",
      (550, 208),
      lambda img : pygame.transform.scale(img, (140, 280))
    )
    self.customerXCoordinate = 550
    
    font = pygame.font.SysFont("Helvetica", 24)
    self.title = Textbox("Dining Room", (17, 15), font=font)

  def updateStates(self):
    """
	  Updates scene state to OrderingScene after customer walks to the player
    """
    newX = self.customerXCoordinate - 10
    self.customerXCoordinate = max(150, newX)

    if self.customerXCoordinate == 150:
      self.sceneService.switchToScene("order_scene", OrderingScene, self.context)
  
  def render(self, screen):
    """
	  Blits texts onto the screen
	  screen: (pygame.Surface) represents image on screen and location of it
    """
    self.title.render(screen)
    self.order_image.render(screen)
    self.player.render(screen)
    self.customer.render(screen, (self.customerXCoordinate, 208))
    