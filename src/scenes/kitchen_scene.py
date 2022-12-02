import pygame
from .base_scene import BaseScene
from .kitchen_order_scene import KitchenOrderScene
from ..components import Textbox, Image, Button, InvisibleButton

class KitchenScene(BaseScene):
  def __init__(self, context):
    BaseScene.__init__(self, BaseScene)
    self.context = context
    self.sceneService = context["scene"]
    
    self.noodles_image = Image(
      r"./assets/noodles.png",
      (0, 80)
    )
    self.rice_image = Image(
      r"./assets/rice.png",
      (0, 200)
    )
    self.chicken_image = Image(
      r"./assets/chicken.png",
      (160, 100)
    )
    self.beef_image = Image(
      r"./assets/beef.png",
      (160, 175)
    )
    self.pork_image = Image(
      r"./assets/pork.png",
      (160, 250)
    )
    self.broccoli_image = Image(
      r"./assets/broccoli.png",
      (300, 100)
    )
    self.carrots_image = Image(
      r"./assets/carrots.png",
      (300, 175)
    )
    self.pepper_image = Image(
      r"assets/pepper.png",
      (300, 250)
    )
    self.squiggles_image = Image(
      r"./assets/squiggles.png",
      (524, 22)
    )
    self.rice_button = InvisibleButton(
      (140, 100),
      (40, 100)
    )
    self.noodles_button = InvisibleButton(
      (140, 100),
      (40, 200)
    )
    self.chicken_button = InvisibleButton(
      (130, 50),
      (200, 110)
    )
    self.pork_button = InvisibleButton(
      (140, 50),
      (200, 270)
    )
    self.beef_button = InvisibleButton(
      (130, 50),
      (200, 180)
    )
    self.broccoli_button = InvisibleButton(
      (130, 50),
      (340, 110)
    )
    self.carrots_button = InvisibleButton(
      (130, 50),
      (340, 180)
    )
    self.pepper_button = InvisibleButton(
      (130, 50),
      (340, 270)
    )
    self.orderTick_button = InvisibleButton(
      (50, 65),
      (675, 30),
      onClick = self.ViewOrder
    )
    
    font = pygame.font.SysFont("Helvetica", 24)
    self.title = Textbox("The Kitchen", (17, 15), font = font)
    
    self.startAnOrderButton = Button(
      (214, 46), 
      (42, 444),
      (17, 433),
      text="Take an Order",
      font=font,
      onClick=self.onTakeAnOrderClick
    )
    self.undoButton = Button(
      (107, 46),
      (639, 444),
      (621, 433),
      text = "Undo",
      font = font,
      onClick=self.onUndoClick
    )

  def onTakeAnOrderClick(self):
    self.sceneService.switchToScene("dining_no_customer")

  def onUndoClick(self):
    pass
  
  def renderIngredientImages(self, screen):
    self.noodles_image.render(screen)
    self.rice_image.render(screen)
    self.chicken_image.render(screen)
    self.beef_image.render(screen)
    self.pork_image.render(screen)
    self.carrots_image.render(screen)
    self.pepper_image.render(screen)
    self.broccoli_image.render(screen)

  def renderIngredientButtons(self, screen):
    self.rice_button.render(screen)
    self.noodles_button.render(screen)
    self.chicken_button.render(screen)
    self.pork_button.render(screen)
    self.beef_button.render(screen)
    self.carrots_button.render(screen)
    self.broccoli_button.render(screen)
    self.pepper_button.render(screen)

  def renderOrdersList(self, screen):
    self.squiggles_image.render(screen)
    self.squiggles_image.render(screen, (598, 22))
    self.squiggles_image.render(screen, (672, 22))
    self.orderTick_button.render(screen)

  def handleEvents(self, events, keys):
      for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
          if pygame.mouse.get_pressed()[0]:
            self.Tick_button.handleClick()
  def ViewOrder(self):
    self.sceneService.switchToScene("kitchen_order_scene", KitchenOrderScene, self.context)
            
  def render(self, screen):
    screen.fill((194, 226, 247))
    self.title.render(screen)

    self.renderIngredientImages(screen)
    self.renderIngredientButtons(screen)

    pygame.draw.rect(screen, "white", [524, 22, 56, 73])
    pygame.draw.rect(screen,"white", [598, 22, 56, 73])
    pygame.draw.rect(screen,"white", [672, 22, 56, 73])
    pygame.draw.rect(screen, "white",[498, 124, 230, 341])

    self.renderOrdersList(screen)

    self.undoButton.render(screen)
    self.startAnOrderButton.render(screen)

    
