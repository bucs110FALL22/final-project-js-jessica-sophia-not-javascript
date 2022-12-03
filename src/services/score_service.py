class ScoreService:
  """
  This will be a singleton that controls
  the amount of tips you get and the highscore
  """

  def __init__(self):
    """
  	initializes tip values
    """
    self.currentTip = 0
    self.maxTip = 0
  def getTips(self):
    """
  	returns current tips value
    """
    return self.currentTip
    
  def getHighScore(self):
    """
    returns high score of tips
    """
    return self.maxTip
    
  def reset(self):
    """
  	resets tips value
    """
    self.currentTip = 0

  def hardReset(self):
    """
  	Resets both the highscore maxtip and the tips value    
    """
    self.currentTip = 0
    self.maxTip = 0

  def addTip(self, amount):
    """
  	Adds to previously earned tips
    """
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
