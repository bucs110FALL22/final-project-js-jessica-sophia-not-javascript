class ScoreService:
  """
  This will be a singleton that controls
  the amount of tips you get and the highscore
  """

  def __init__(self):
    self.currentTip = 0
    self.maxTip = 0

  def getTips(self):
    return self.currentTip

  def getHighScore(self):
    return self.maxTip
    
  def reset(self):
    self.currentTip = 0

  def hardReset(self):
    self.currentTip = 0
    self.maxTip = 0

  def addTip(self, amount):
    self.currentTip+= amount

  def updateMax(self):
    """
    updates the max amount of tips ever recieved
    will return true if a new max is reached
    """
    if self.currentTip > self.maxTip:
      self.maxTip = self.currentTip
      return True
    return False
