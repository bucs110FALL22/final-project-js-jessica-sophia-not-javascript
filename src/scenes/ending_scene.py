import pygame
from .base_scene import BaseScene
from ..components import Textbox, Image, Button

class EndingScene(BaseScene):
  def __init__(self, context):
    BaseScene.__init__(self, BaseScene)
    self.context = context
    self.sceneService = context["scene"]
    
    # WARNING: self.player is not being used
    self.player = Image(
      r"./assets/playerboy.png",
      (20, 208),
      lambda img : pygame.transform.flip(img, True, False),
      lambda img : pygame.transform.scale(img, (140, 280))
    )
    
    font = pygame.font.SysFont("Helvetica", 24)
    self.replayButton = Button(
      (214, 46),
      (365, 333),
      (340, 322),
      text = "Replay",
      font = font,
      onClick = self.onReplayClick
    )
    self.goHomeButton = Button(
      (214, 46),
      (364, 415),
      (340, 404),
      text = "Go Home",
      font = font,
      onClick = self.onGoHomeClick
    )


  def handleEvents(self, events, keys):
    for event in events:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pressed()[0]:
          self.goHomeButton.handleClick()
          self.replayButton.handleClick()
          break
          
  def render(self, screen):
    screen.fill((194, 226, 247))
    self.goHomeButton.render(screen)
    self.player.render(screen)
    self.replayButton.render(screen)

  def onReplayClick(self):
    self.sceneService.switchToScene("dining_no_customer")

  def onGoHomeClick(self):
    self.sceneService.switchToScene("welcome_scene")
