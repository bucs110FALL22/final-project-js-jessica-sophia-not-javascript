import pygame
from .base_scene import BaseScene
from .results_scene import ResultsScene
from .kitchen_scene import KitchenScene
from ..components import Textbox, Button, InvisibleButton

class KitchenOrderScene(BaseScene):
  def __init__(self, context):
    BaseScene.__init__(self, BaseScene)  
    self.context = context
    self.sceneService = context["scene"]
    
    font = pygame.font.SysFont("Helvetica", 24)
    #self.send_out_food_text = Textbox("Send Out Food", (533, 444), font = font)
    
    self.SendOutFoodButton = Button(
      (228, 46),
      (533, 444),
      (506, 433),
      text="Send Out Food",
      font = font,
      onClick = self.onSendOutFoodClick
    )
    
    self.exitButton = InvisibleButton(
      (50, 65),
      (675, 30),
      onClick = self.onExitButtonClick
    )
    
  def handleEvents(self, events, keys):
    for event in events:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pressed()[0]:
          self.SendOutFoodButton.handleClick()
          self.exitButton.handleClick()
          break
            
  def render(self, screen):
    screen.fill((194, 226, 247))
    pygame.draw.rect(screen, (255, 255, 255), [200, 72, 350, 394])
    pygame.draw.rect(screen, (0, 255, 0), [506, 433, 228, 46])
    self.SendOutFoodButton.render(screen)
    self.exitButton.render(screen)
    
  def onSendOutFoodClick(self):
      self.sceneService.switchToScene("results_scene", ResultsScene, self.context)
  def onExitButtonClick(self):
    self.sceneService.switchToScene("kitchen_scene", KitchenScene , self.context)
    