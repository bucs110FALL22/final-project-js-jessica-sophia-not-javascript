import pygame
from .base_scene import BaseScene
from .dining_empty_scene import DiningEmptyScene
from .help_scene import HelpScene
from ..components import Button, Textbox, Image

class WelcomeScene(BaseScene):
  def __init__(self, context):
    """
	  Provides context to the scene, creates Buttons and Textboxes
    """
    BaseScene.__init__(self, BaseScene)
    self.context = context
    self.sceneService = context["scene"]

    self.dining_hall_image = Image(
      r"./assets/dining_hall.jpg",
      (0, 0),
      lambda img : pygame.transform.scale(img, (750, 500))
    )
  
    self.startButton = Button(
      (140, 40), 
      (375 - 35, 250 - 20), 
      (375 - 70, 250 - 20),
      text="Start",
      onClick=self.onStartClick
    )
    self.helpButton = Button(
      (140, 40), 
      (375 - 35, 250 + 40), 
      (375 - 70, 250 + 40),
      text="Help",
      onClick=self.onHelpClick
    )
    self.quitButton = Button(
      (140, 40), 
      (375 - 35, 250 + 100), 
      (375 - 70, 250 + 100),
      text="Quit",
      onClick=self.onQuitClick
    )
    self.title = Textbox("JS' Dining Halleria", (375 - 160, 40))

  def onStartClick(self):
    """
	  Switches Scene to diningEmptyScene on click of startButton
    """
    self.sceneService.switchToScene("dining_no_customer", DiningEmptyScene, self.context)

  def onHelpClick(self):
    """
	  Switches Scene to helpScene on click of helpButton
    """
    self.sceneService.switchToScene("help_scene", HelpScene, self.context)
    
  def onQuitClick(self):
    """
	  Clears current Scene on click of quitButton
    """
    self.sceneService.clearCurrentScene()

  def handleEvents(self, events, keys):
    """
    Anything defined inside this method will handle events
    events => list of pygame events
    keys => list of keys pressed
    """
    for event in events:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pressed()[0]:
          self.startButton.handleClick()
          self.helpButton.handleClick()
          self.quitButton.handleClick()
          break

  def render(self, screen):
    """
	  renders buttons and visual elements of screen
    """
    screen.fill((255 , 255, 255))
    self.dining_hall_image.render(screen)

    self.title.render(screen)
    self.startButton.render(screen)
    self.helpButton.render(screen)
    self.quitButton.render(screen)
