import pygame
from .base_scene import BaseScene
from .dining_customer_scene import DiningCustomerScene
from ..components import Textbox, Button, Image

class ResultsScene(BaseScene):
  def __init__(self, context):
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
      (150, 208),
      lambda img : pygame.transform.scale(img, (140, 280))
    )

    font = pygame.font.SysFont("Helvetica", 24)
    self.tips_text = Textbox("Tips", (17, 15), font = font)

    self.takeAnOrderButton = Button(
      (214, 46),
      (318, 444),
      (293, 433),
      text="Take an Order",
      font = font,
      onClick=self.onTakeOrder
    )
    self.goToKitchenButton = Button(
      (214, 46),
      (543, 444),
      (518, 433),
      text="Go To Kitchen",
      font = font,
      onClick = self.goToKitchen
    )

  def handleEvents(self, events, keys):
    for event in events:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pressed()[0]:
          self.takeAnOrderButton.handleClick()
          self.goToKitchenButton.handleClick()
          
  def render(self, screen):
    self.order_image.render(screen)
    self.player.render(screen)
    self.customer.render(screen)
    
    pygame.draw.rect(screen, "white", [345, 72, 350, 394])
    # pygame.draw.rect(screen, [0, 255, 0], [293, 433, 214, 46])
    
    self.tips_text.render(screen)

    self.goToKitchenButton.render(screen)
    self.takeAnOrderButton.render(screen)

  def onTakeOrder(self):
    self.sceneService.switchToScene("dining_customer_scene", DiningCustomerScene , self.context)
  def goToKitchen(self):
    self.sceneService.switchToScene("kitchen_scene", KitchenScene, self.context)
    
