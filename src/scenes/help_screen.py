import pygame
from .base_scene import BaseScene
from .welcome_scene import WelcomeScene
from ..components import Textbox, Button, InvisibleButton, Image

class HelpScene(BaseScene):
  def __init__(self, context):
    BaseScene.__init__(self, BaseScene)  
    self.context = context
    self.sceneService = context["scene"]
    
    font = pygame.font.SysFont("Helvetica", 24)
    
    self.closeButton = Image(
      r"./assets/closeButton.png",
      (675, 30),
      lambda img : pygame.transform.scale(img, (50, 50))
    )
    
    self.exitButton = InvisibleButton(
      (50, 50),
      (675, 30),
      onClick = self.onExitButtonClick
    )
    def onExitClick(self):
    self.sceneService.switchToScene("welcome_scene", WelcomeScene, self.context)
  
    
  def handleEvents(self, events, keys):
    for event in events:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pressed()[0]:
          self.exitButton.handleClick()
          break     
    
  def render(self, screen):
    screen.fill((194, 226, 247))
    pygame.draw.rect(screen, (255, 255, 255), [200, 72, 350, 394])
    pygame.draw.rect(screen, (0, 255, 0), [506, 433, 228, 46])
    self.exitButton.render(screen)
    self.closeButton.render(screen)
    for orderLine in self.orderLines:
      orderLine.render(screen)
    self.orderTitle.render(screen)
    

  def onExitButtonClick(self):
    self.sceneService.switchToScene("welcome_scene")