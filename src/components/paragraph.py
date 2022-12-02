from .base_component import BaseComponent
from .textbox import Textbox

class Paragraph(BaseComponent):
  def __init__(self, lines, textPosition, gap=30, **kwargs):
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
    for text in self.textboxes:
      text.render(screen)
