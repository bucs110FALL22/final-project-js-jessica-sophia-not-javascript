import random

class OrderService:
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
    self.id = 1
    self.orders = []

  def reset(self):
    self.id = 1
    self.orders = []

  def generateNewOrder(self):
    """
    Picks a random base, protein, and a set of toppings
    Picks a random # of protein and toppings
    Returns an order with those new ingredients
    """
    
    base = random.choice(OrderService.INGREDIENTS[:2])
    protein = random.choice(OrderService.INGREDIENTS[2:5])
    toppings = list(set(random.choices(OrderService.INGREDIENTS[5:], k=2)))

    order = {}
    order[base] = 1
    order[protein] = random.randint(1, 3)

    for top in toppings:
      order[top] = random.randint(2, 5)

    order["id"] = self.id
    self.id+= 1

    return order

  def getOrders(self):
    return self.orders

  def addOrder(self, order):
    self.orders.append(order)

  def getOrder(self, index):
    return self.orders[index]

  def removeOrder(self, order):
    id = order["id"]
    self.orders = list(filter(lambda o : o["id"] != id, self.orders))

  def size(self):
    return len(self.orders)

  def getSummary(self, order):
    lines = []
    for ing in OrderService.INGREDIENTS:
      if ing not in order:
        continue
      amount = order[ing]
      if amount < 1:
        continue
      lines.append(f"{amount}x {ing}")
    return lines
  