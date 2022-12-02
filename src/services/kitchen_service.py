class KitchenService:
  """
  This will be a singleton that controls
  what scene to play on the screen
  """
  INGREDIENTS = [
    "noodles", "rice",
    "chicken", "beef", "pork",
    "carrots", "peppers", "broccoli"
  ]

  def __init__(self):
    # self.summary will be a tally of all the ind used
    self.summary = {}
    for ing in KitchenService.INGREDIENTS:
      self.summary[ing] = 0

    # self.history will be a stack containing all the undo moves
    # self.history[i] == name of item to take back
    self.history = []

    # self.target is (order, index of order) that will be displayed on the kitchen order scene
    self.target = (None, -1)

  def reset(self):
    for ing in KitchenService.INGREDIENTS:
      self.summary[ing] = 0

  def undo(self):
    if len(self.history) < 1:
      return
    item = self.history.pop()
    self.summary[item]-= 1

  def getCurrentSummary(self):
    return self.summary

  def focus(self, target, index):
    self.target = (target, index)

  def getFocus(self):
    return self.target
  