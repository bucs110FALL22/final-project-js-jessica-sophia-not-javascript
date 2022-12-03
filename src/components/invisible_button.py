from .button import Button
from ..util import getOrElse

class InvisibleButton(Button):
  def __init__(self, size, backgroundPosition, **kwargs):
    """
	general function description
	args: (type) description
	return: (type) description
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
	  args: (type) description
  	return: (type) description
    """
    if not self.debug:
      return
    Button.render(self, screen)