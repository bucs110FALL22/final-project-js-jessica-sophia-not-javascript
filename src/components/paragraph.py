from .base_component import BaseComponent
from .textbox import Textbox

class Paragraph(BaseComponent):
  def __init__(self, lines, textPosition, gap=30, **kwargs):
    """
	Creates textbox for multiple lines of text
	lines: (string)
  textPosition: (float, float)
  gap: (integer)
    """
    BaseComponent.__init__(self)

    x, y = textPosition
    self.textboxes = []
    for i, line in enumerate(lines):
      self.textboxes.append(
        Textbox(
          line,
          (x, y + i*gap),
          **kwargs
        )
      )

  def render(self, screen):
    """
	Blits texts onto the screen
	screen: (pygame.Surface) represents image on screen and location of it
    """
    for text in self.textboxes:
      text.render(screen)
