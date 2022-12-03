import pygame
from .base_scene import BaseScene
from ..components import InvisibleButton, Image, Paragraph

class HelpScene(BaseScene):
  def __init__(self, context):
    """
	general function description
	args: (type) description
	return: (type) description
    """
    BaseScene.__init__(self, BaseScene)  
    self.context = context
    self.sceneService = context["scene"]
    
    font = pygame.font.SysFont("Helvetica", 20)
    self.instructions = Paragraph(
      [
        "Help",
        "To play the game, click start and",
        "take order. Afterwards, click",
        "create and match the order by",
        "clicking on the images of the",
        "food. You can then take another",
        "order or click on the order on the",
        "upper right hand corner to serve",
        "the food. The goal is to receive",
        "as many tips as possible."
      ],
      (210, 80),
      gap=38,
      font=font
    )
    
    self.exitImage = Image(
      r"./assets/closeButton.png",
      (675, 30),
      lambda img : pygame.transform.scale(img, (50, 50))
    )
    
    self.exitButton = InvisibleButton(
      (50, 50),
      (675, 30),
      onClick = self.onExitButtonClick
    )
    
  def onExitButtonClick(self):
    """
	general function description
	args: (type) description
	return: (type) description
    """
    self.sceneService.switchToScene("welcome")
  
    
  def handleEvents(self, events, keys):
    """
	general function description
	args: (type) description
	return: (type) description
    """
    for event in events:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pressed()[0]:
          self.exitButton.handleClick()
          break     
    
  def render(self, screen):
    """
	general function description
	args: (type) description
	return: (type) description
    """
    screen.fill((194, 226, 247))
    
    self.exitImage.render(screen)
    self.exitButton.render(screen)
    
    pygame.draw.rect(screen, (255, 255, 255), [200, 72, 350, 394])
    #pygame.draw.rect(screen, (0, 255, 0), [506, 433, 228, 46])
    self.instructions.render(screen)
    
  