class KitchenService:
  INGREDIENTS = [
    "noodles", "rice",
    "chicken", "beef", "pork",
    "carrots", "peppers", "broccoli"
  ]

  def __init__(self):
    """
	  creates tally of all ingredients used, and history of undo moves
    self.history[i] == name of item to take back
    self.target is (order, index of order) that will be displayed on the kitchen order scene
    """ 
    self.summary = {}
    for ing in KitchenService.INGREDIENTS:
      self.summary[ing] = 0

    self.history = []
    self.target = (None, -1)

  def addItem(self, itemName):
    """
	  adds item to order summary
    """ 
    if itemName not in self.summary:
      return
    self.summary[itemName]+= 1
    self.history.append(itemName)
  
  def reset(self):
    """
	  resets order summary
    """ 
    self.history = []
    for ing in KitchenService.INGREDIENTS:
      self.summary[ing] = 0

  def computeDifference(self, order):
    """
	  Computes total tips earned according to criteria
    """ 
    total_tips = 0
    lines = []
    for ing in KitchenService.INGREDIENTS:
      if ing not in order:
        # if the ingredient is not in the order
        if ing in self.summary:
          amount = self.summary[ing]
          if amount < 1:
            continue

          # but we still gave some, deduct $0.50 for every item
          deduction = 0.5*amount
          total_tips-= deduction
          lines.append("{}x {} [- ${:.2f}]".format(amount, ing, deduction))
        continue
      
      wanted = order[ing]
      if wanted < 1:
        continue
      # now we know the ingredient is in order
      # we compute the absolute difference and deduct from $2.75
      # based on how off we are
      gave = self.summary[ing]
      diff = min(abs(wanted - gave), wanted)
      tip = max(2.75*(wanted - diff)/wanted, 0)
      total_tips+= tip
      lines.append("{}x {} [+ ${:.2f}]".format(gave, ing, tip))

    total_tips = max(total_tips, 0)
    lines.append("Tips Earned: {:.2f}".format(total_tips))
    # if they get negative tips, they just get 0 tips
    return (total_tips, lines)

  def undo(self):
    """
	  removes ingredient from order 
    """ 
    if len(self.history) < 1:
      return
    item = self.history.pop()
    self.summary[item]-= 1

  def getCurrentSummary(self):
    """
	  gets current list of ingredients added
    """ 
    return self.summary

  def focus(self, target, index):
    self.target = (target, index)
  
  def getFocus(self):
    return self.target
  