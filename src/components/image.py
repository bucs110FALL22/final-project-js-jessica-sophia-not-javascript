import pygame
from .base_component import BaseComponent

class Image(BaseComponent):
  def __init__(self, path, position, *mappings):
    """
	general function description
	args: (type) description
	return: (type) description
    """
    BaseComponent.__init__(self)

    self.position = position
    
    base = pygame.image.load(path)
    for m in mappings:
      base = m(base)
    self.content = base

  def render(self, screen, newPosition=None):
    """
	general function description
	args: (type) description
	return: (type) description
    """
    pos = self.position if newPosition == None else newPosition
    screen.blit(self.content, pos)
