import pygame
from .base_component import BaseComponent
from ..util import getOrElse

class Textbox(BaseComponent):
  def __init__(self, content, textPosition, **kwargs):
    """
	  initializes Textbox
    content: string containing textbox content
    textPosition: position of text
    **kwargs
    """
    BaseComponent.__init__(self)

    self.font = getOrElse(kwargs, "font", pygame.font.SysFont("Helvetica", 35))
    self.color = getOrElse(kwargs, "color", (0, 0, 0))
    
    self.content = self.font.render(content, True, self.color)
    self.textPosition = textPosition

  def render(self, screen):
    """
	  Blits texts onto the screen
	  screen: (pygame.Surface) represents image on screen and location of it
    """
    screen.blit(self.content, self.textPosition)

