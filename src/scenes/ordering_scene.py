import pygame
from .base_scene import BaseScene
from .kitchen_scene import KitchenScene
from ..components import Textbox, Image, Button

class OrderingScene(BaseScene):
  def __init__(self, context):
    """
	general function description
	args: (type) description
	return: (type) description
    """
    BaseScene.__init__(self, BaseScene)
    self.context = context
    self.sceneService = context["scene"]
    self.orderService = context["order"]

    self.newOrder = self.orderService.generateNewOrder()
    self.orderService.addOrder(self.newOrder)
    
    self.order_image = Image(
      r"./assets/orderBackground.png",
      (0, 0),
      lambda img : pygame.transform.scale(img, (750, 500)),
      lambda img : pygame.transform.scale(img, (750, 500))
    )
    
    self.player = Image(
      r"assets/playerboy.png",
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
    #self.create_text = Textbox("Create", (630, 444), font = font)

    self.title = Textbox("Ordering...", (17, 15), font = font)
    # 621, 433, 
    self.createButton = Button(
      (150, 46),
      (530, 444),
      (521, 433),
      text="Create",
      font = font,
      onClick=self.onCreateClick
    )

    ORDER_X = 360
    self.orderTitle = Textbox(
      f"ORDER {self.newOrder['id']}", 
      (ORDER_X, 90), 
      font = font
    )

    self.orderLines = []
    orderSummary = self.orderService.getSummary(self.newOrder)
    for i, line in enumerate(orderSummary):
      self.orderLines.append(
        Textbox(
          line, 
          (ORDER_X, 140 + 60*i), 
          font = font
        )
      )
    

  def handleEvents(self, events, keys):
    """
	general function description
	args: (type) description
	return: (type) description
    """
    for event in events:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pressed()[0]:
          self.createButton.handleClick()
          break
  
  def render(self, screen):
    """
	general function description
	args: (type) description
	return: (type) description
    """
    self.order_image.render(screen)
    self.player.render(screen)
    self.customer.render(screen)
    
    self.title.render(screen)
    
    pygame.draw.rect(screen, "white", [345, 72, 350, 394])
    self.orderTitle.render(screen)

    for orderLine in self.orderLines:
      orderLine.render(screen)
    
    self.createButton.render(screen)

  def onCreateClick(self):
    """
	general function description
	args: (type) description
	return: (type) description
    """
    self.sceneService.switchToScene("kitchen_scene", KitchenScene, self.context)