import pygame
from .base_component import BaseComponent
from ..util import getOrElse

class Button(BaseComponent):
  def __init__(self, size, textPosition, backgroundPosition, **kwargs):
    """
	initialize button class
	size: (float, float) the size of the button
  textPosition: (float, float) the position for the text
  backgroundPosition: (float, float) the x and y for the button position
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
	To identify the area with the event of mouse click. onClick function runs if mouse is on certain area
    """
    mx, my = pygame.mouse.get_pos()
    if self.boundaries.collidepoint(mx, my):
      self.onClick()

  def render(self, screen):
    """
	Draws and blits images/texts onto the screen
	screen: (pygame.Surface) represents image on screen and location of it
    """
    w, h = self.size
    bx, by = self.backgroundPosition
    pygame.draw.rect(screen, self.backgroundColor, [bx, by, w, h])

    tx, ty = self.textPosition
    screen.blit(self.text, (tx, ty)) 
    