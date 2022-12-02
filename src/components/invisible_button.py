from .button import Button
from ..util import getOrElse

class InvisibleButton(Button):
  def __init__(self, size, backgroundPosition, **kwargs):
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
    """
    if not self.debug:
      return
    Button.render(self, screen)