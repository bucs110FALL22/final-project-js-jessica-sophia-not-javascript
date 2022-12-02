class BaseScene:
  def __init__(self, context):
    """
    context => force subclasses to take in a context
    context will allow the class have access to globals
    """
    pass

  def handleEvents(self, events, keys):
    """
    Anything defined inside this method will handle events
    events => list of pygame events
    keys => list of keys pressed
    """
    pass

  def updateStates(self):
    """
    This method will look at whatever state variables it has
    and compute the next iteration values
    """
    pass

  def render(self, screen):
    """
    This method takes in a screen from pygame
    and does whatever to rend the scene onto the screen
    """
    pass
