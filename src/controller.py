from sys import exit
import pygame
from .scenes import *
from .services import *

class Controller:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((750, 500))
    self.clock = pygame.time.Clock()
    
    self.sceneSvc = SceneService()
    
    self.context = {
      "scene": self.sceneSvc,
      "score": ScoreService(),
      "kitchen": KitchenService(),
      "order": OrderService()
    }

  def run(self):
    self.sceneSvc.switchToScene(
      "welcome",
      WelcomeScene,
      self.context
    )

    while True:
      activeScene = self.sceneSvc.getCurrentScene()
      
      # if we don't have any more scenes
      # then the program has ended
      if activeScene == None:
        return
      
      # grab all events at this frame
      pressedKeys = pygame.key.get_pressed()
      events = pygame.event.get()
      activeScene.handleEvents(events, pressedKeys)
      
      # update any states in the scene
      activeScene.updateStates()
      
      # render new scene
      activeScene.render(self.screen)
      pygame.display.flip()
      
      # delay a bit until next frame
      self.clock.tick(60)

    # we don't have any more active scenes, so we quit
    pygame.display.quit()
    pygame.quit()
    exit()