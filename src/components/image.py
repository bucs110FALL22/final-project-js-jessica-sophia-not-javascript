import pygame
from .base_component import BaseComponent

class Image(BaseComponent):
  def __init__(self, path, position, *mappings):
    """
	general function description
	path: ()
  position: ()
    """
    BaseComponent.__init__(self)

    self.position = position
    
    base = pygame.image.load(path)
    for m in mappings:
      base = m(base)
    self.content = base

  def render(self, screen, newPosition=None):
    """
	Blits images onto the screen
	screen: (pygame.Surface) description
	newPosition:()
    """
    pos = self.position if newPosition == None else newPosition
    screen.blit(self.content, pos)
