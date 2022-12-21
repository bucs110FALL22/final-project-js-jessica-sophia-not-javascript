import pygame
from .base_scene import BaseScene
from ..components import Textbox, Image, Button

class EndingScene(BaseScene):
  def __init__(self, context):
    """
	  Provides context to the scene, creates Buttons and Textboxes
    """
    BaseScene.__init__(self, BaseScene)
    self.context = context
    self.sceneService = context["scene"]
    self.orderService = context["order"]
    self.scoreService = context["score"]
    
    # WARNING: self.player is not being used
    self.player = Image(
      r"./assets/playerboy.png",
      (20, 208),
      lambda img : pygame.transform.flip(img, True, False),
      lambda img : pygame.transform.scale(img, (140, 280))
    )

    self.scoreService.updateMax()
    self.total_tips = Textbox(
      "You have earned a total of: ${:.2f}".format(self.scoreService.getTips()), 
      (100, 100)
    )
    self.highScore = Textbox(
      "High Score: ${:.2f}".format(self.scoreService.getHighScore()), 
      (280, 200)
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
    """
    Anything defined inside this method will handle events
    events => list of pygame events
    keys => list of keys pressed
    """
    for event in events:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pressed()[0]:
          self.goHomeButton.handleClick()
          self.replayButton.handleClick()
          break
          
  def render(self, screen):
    """
	  Blits texts onto the screen
	  screen: (pygame.Surface) represents image on screen and location of it
    """
    screen.fill((194, 226, 247))
    self.goHomeButton.render(screen)
    self.player.render(screen)
    self.replayButton.render(screen)
    self.total_tips.render(screen)
    self.highScore.render(screen)

  def reset(self):
    """
	  resets the score and orders list
    """
    self.scoreService.reset()
    self.orderService.reset()

  def onReplayClick(self):
    """
	  Switches scene to diningNoCustomer on click ofreplayButton
    """
    self.reset()
    self.sceneService.switchToScene("dining_no_customer")

  def onGoHomeClick(self):
    """
	  Switches scene to welcomeScene on click of goHomeButton
    """
    self.reset()
    self.sceneService.switchToScene("welcome")
