import pygame
from .base_scene import BaseScene
from .results_scene import ResultsScene
from ..components import Textbox, Button, InvisibleButton, Image

class KitchenOrderScene(BaseScene):
  def __init__(self, context):
    """
	  Provides context to the scene, creates Buttons and Textboxes
    """
    BaseScene.__init__(self, BaseScene)  
    self.context = context
    self.sceneService = context["scene"]
    self.kitchenService = context["kitchen"]
    self.orderService = context["order"]
    
    font = pygame.font.SysFont("Helvetica", 24)
    
    self.closeButton = Image(
      r"./assets/closeButton.png",
      (675, 30),
      lambda img : pygame.transform.scale(img, (50, 50))
    )
    self.SendOutFoodButton = Button(
      (228, 46),
      (533, 444),
      (506, 433),
      text="Send Out Food",
      font = font,
      onClick = self.onSendOutFoodClick
    )
    
    self.exitButton = InvisibleButton(
      (50, 50),
      (675, 30),
      onClick = self.onExitButtonClick
    )
  
    order, order_index = self.kitchenService.getFocus()
    ORDER_X = 240
    self.orderTitle = Textbox(
      f"ORDER {order['id']}", 
      (ORDER_X, 90), 
      font = font
    )

    self.orderLines = []
    orderSummary = self.orderService.getSummary(order)
    for i, line in enumerate(orderSummary):
      self.orderLines.append(
        Textbox(
          line, 
          (ORDER_X, 140 + 80*i), 
          font = font
        )
      )

  def handleEvents(self, events, keys):
    """
    Anything defined inside this method will handle events
    events => list of pygame events
    keys => list of keys pressed
    """
    for event in events:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pressed()[0]:
          self.SendOutFoodButton.handleClick()
          self.exitButton.handleClick()
          break     
    
  def render(self, screen):
    """
	  Blits texts onto the screen
	  screen: (pygame.Surface) represents image on screen and location of it
    """
    screen.fill((194, 226, 247))
    pygame.draw.rect(screen, (255, 255, 255), [200, 72, 350, 394])
    pygame.draw.rect(screen, (0, 255, 0), [506, 433, 228, 46])
    self.SendOutFoodButton.render(screen)
    self.exitButton.render(screen)
    self.closeButton.render(screen)
    for orderLine in self.orderLines:
      orderLine.render(screen)
    self.orderTitle.render(screen)
    
  def onSendOutFoodClick(self):
    """
	  Switches Scene to resultsScene on click out SendOutFoodButton  
    """
    self.sceneService.switchToScene("results_scene", ResultsScene, self.context)
    
  def onExitButtonClick(self):
    """
	  Switches Scene to kitchenScene on click of exitButton
    """
    self.sceneService.switchToScene("kitchen_scene")
    