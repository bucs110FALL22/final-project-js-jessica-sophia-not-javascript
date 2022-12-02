import pygame
from .base_scene import BaseScene
from ..components import Textbox, Image

class DiningCustomerScene(BaseScene):
  def __init__(self, context):
    BaseScene.__init__(self, BaseScene)

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
    
    font = pygame.font.SysFont("Helvetica", 24)
    self.title = Textbox("Dining Room", (17, 15), font=font)

  def render(self, screen):
    self.title.render(screen)
    self.order_image.render(screen)
    self.player.render(screen)
    self.customer.render(screen)
    