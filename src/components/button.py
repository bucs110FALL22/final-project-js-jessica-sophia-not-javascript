import pygame
from .base_component import BaseComponent
from ..util import getOrElse

class Button(BaseComponent):
  def __init__(self, size, textPosition, backgroundPosition, **kwargs):
    """
	general function description
	size: (integer) the size of the button
  textPosition: ()
    """
    BaseComponent.__init__(self)
    self.size = size
    self.font = getOrElse(kwargs, "font", pygame.font.SysFont("Helvetica", 35))
    self.color = getOrElse(kwargs, "color", (0, 0, 0))
    self.backgroundColor = getOrElse(kwargs, "backgroundColor", (235, 225, 255))

    textContent = getOrElse(kwargs, "text", "Untitled")
    self.text = self.font.render(textContent, True, self.color)
    if len(self.color) > 3:
      self.text.set_alpha(self.color[3])
    
    self.textPosition = textPosition
    self.backgroundPosition = backgroundPosition

    bx, by = backgroundPosition
    bw, bh = size
    self.boundaries = pygame.Rect(bx, by, bw, bh)

    self.onClick = getOrElse(kwargs, "onClick", lambda : True)

  def handleClick(self):
    """
	general function description
	args: (type) description
	return: (type) description
    """
    mx, my = pygame.mouse.get_pos()
    if self.boundaries.collidepoint(mx, my):
      self.onClick()

  def render(self, screen):
    """
	general function description
	args: (type) description
	return: (type) description
    """
    w, h = self.size
    bx, by = self.backgroundPosition
    pygame.draw.rect(screen, self.backgroundColor, [bx, by, w, h])

    tx, ty = self.textPosition
    screen.blit(self.text, (tx, ty)) 
    