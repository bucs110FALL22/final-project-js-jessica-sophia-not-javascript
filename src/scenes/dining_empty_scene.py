import pygame
from .base_scene import BaseScene
from .dining_customer_scene import DiningCustomerScene
from .ending_scene import EndingScene
from .kitchen_scene import KitchenScene
from ..components import Button, Image, Textbox

class DiningEmptyScene(BaseScene):
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
      (20, 94),
      lambda img : pygame.transform.flip(img, True, False),
      lambda img : pygame.transform.scale(img, (200, 400))
    )

    self.title = Textbox("Dining Room", (17, 15))
    
    font = pygame.font.SysFont("Helvetica", 24)
    self.closeShopButton = Button(
      (214, 36),
      (304.39, 444),
      (279, 433),
      text="Close Shop",
      font=font,
      onClick=self.onCloseShopClick
    )
    
    self.takeOrderButton = Button(
      (214, 36),
      (540.39, 380),
      (515, 369),
      text="Take Order",
      font=font,
      onClick=self.onTakeOrderClick
    )
    self.goToKitchenButton = Button(
      (214, 36),
      (540.39, 444),
      (515, 433),
      text="Go to Kitchen",
      font=font,
      onClick=self.onGoToKitchenClick
    )

  def handleEvents(self, events, keys):
    for event in events:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pressed()[0]:
          self.closeShopButton.handleClick()
          self.takeOrderButton.handleClick()
          self.goToKitchenButton.handleClick()
          break

  def render(self, screen):
    screen.fill((255 , 255, 255))
    self.order_image.render(screen)
    self.title.render(screen)
    self.closeShopButton.render(screen)
    self.takeOrderButton.render(screen)
    self.goToKitchenButton.render(screen)
    self.player.render(screen)

  def onTakeOrderClick(self):
    self.sceneService.switchToScene("dining_customer_scene", DiningCustomerScene, self.context)

  def onCloseShopClick(self):
    self.sceneService.switchToScene("ending_scene", EndingScene , self.context)

  def onGoToKitchenClick(self):
    try:
      self.sceneService.switchToScene("kitchen_scene")
    except:
      self.sceneService.switchToScene("kitchen_scene", KitchenScene, self.context)