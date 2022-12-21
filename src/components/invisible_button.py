from .button import Button
from ..util import getOrElse

class InvisibleButton(Button):
  def __init__(self, size, backgroundPosition, **kwargs):
    """
	Creates invisible button
	size: (float, float) the size of the button
  backgroundPosition: (float, float) the x and y coordinates for the button position
    """
    Button.__init__(
      self, 
      size,
      (0, 0), 
      backgroundPosition, 
      **kwargs,
      text=""
    )
    self.debug = getOrElse(kwargs, "debug", False)

  def render(self, screen):
    """
    If we are not in debug mode, we don't even need to render
    this button because it is "invisible"
	  screen: (pygame.Surface) represents image on screen and location of it
    """
    if not self.debug:
      return
    Button.render(self, screen)