import pygame
from .base_scene import BaseScene
from .kitchen_order_scene import KitchenOrderScene
from ..components import Textbox, Image, Button, InvisibleButton

class KitchenScene(BaseScene):
  def __init__(self, context):
    BaseScene.__init__(self, BaseScene)
    self.context = context
    self.sceneService = context["scene"]
    self.orderService = context["order"]
    self.kitchenService = context["kitchen"]
    
    self.noodles_image = Image(
      r"./assets/noodles.png",
      (0, 80)
    )
    self.rice_image = Image(
      r"./assets/rice.png",
      (0, 200)
    )
    self.chicken_image = Image(
      r"./assets/chicken.png",
      (160, 100)
    )
    self.beef_image = Image(
      r"./assets/beef.png",
      (160, 175)
    )
    self.pork_image = Image(
      r"./assets/pork.png",
      (160, 250)
    )
    self.broccoli_image = Image(
      r"./assets/broccoli.png",
      (300, 100)
    )
    self.carrots_image = Image(
      r"./assets/carrots.png",
      (300, 175)
    )
    self.pepper_image = Image(
      r"assets/pepper.png",
      (300, 250)
    )
    
    self.noodles_button = InvisibleButton(
      (140, 100),
      (40, 100),
      onClick=self.generateIngredientFunction("noodles")
    )
    self.rice_button = InvisibleButton(
      (140, 100),
      (40, 200),
      onClick=self.generateIngredientFunction("rice")
    )
    self.chicken_button = InvisibleButton(
      (130, 50),
      (200, 110),
      onClick=self.generateIngredientFunction("chicken")
    )
    self.pork_button = InvisibleButton(
      (140, 50),
      (200, 270),
      onClick=self.generateIngredientFunction("pork")
    )
    self.beef_button = InvisibleButton(
      (130, 50),
      (200, 180),
      onClick=self.generateIngredientFunction("beef")
    )
    self.broccoli_button = InvisibleButton(
      (130, 50),
      (340, 110),
      onClick=self.generateIngredientFunction("broccoli")
    )
    self.carrots_button = InvisibleButton(
      (130, 50),
      (340, 180),
      onClick=self.generateIngredientFunction("carrots")
    )
    self.pepper_button = InvisibleButton(
      (130, 50),
      (340, 270),
      onClick=self.generateIngredientFunction("peppers")
    )
    
    font = pygame.font.SysFont("Helvetica", 24)
    self.title = Textbox("The Kitchen", (17, 15), font = font)
    self.summaryTitle = Textbox("Summary:", (510, 134), font = font)
    
    self.startAnOrderButton = Button(
      (214, 46), 
      (42, 444),
      (17, 433),
      text="Take an Order",
      font=font,
      onClick=self.onTakeAnOrderClick
    )
    self.undoButton = Button(
      (107, 46),
      (639, 444),
      (621, 433),
      text = "Undo",
      font = font,
      onClick=self.onUndoClick
    )

    self.orderViewButtons = []
    self.orderImagePositions = []
    self.squiggles_image = Image(
      r"./assets/squiggles.png",
      (524, 22),
      lambda img : pygame.transform.scale(img, (50, 65))
    )

    orders = self.orderService.getOrders()
    for i, order in enumerate(orders):
      self.orderImagePositions.append(
        (675 - 60*i, 30)
      )
      self.orderViewButtons.append(
        InvisibleButton(
          (50, 65),
          (675 - 60*i, 30),
          onClick = self.generateOrderViewFunction(i, order)
        )
      )

    self.summaryLines = []
    self.updateSummaryLines()

  def updateSummaryLines(self):
    self.summaryLines = []
    
    summary_font = pygame.font.SysFont("Helvetica", 20)
    newSummaryDetails = self.kitchenService.getCurrentSummary()
    newSummaryLines = self.orderService.getSummary(newSummaryDetails)
    for i, line in enumerate(newSummaryLines):
      self.summaryLines.append(
        Textbox(
          line,
          (510, 180 + 25*i),
          font= summary_font
        )
      )

  def generateIngredientFunction(self, itemName):
    def addItem():
      self.kitchenService.addItem(itemName)
      self.updateSummaryLines()
    return addItem

  def generateOrderViewFunction(self, index, order):
    def viewSpecificOrder():
      self.kitchenService.focus(order, index)
      self.sceneService.switchToScene("kitchen_order_scene", KitchenOrderScene, self.context)
    return viewSpecificOrder
      
  def onTakeAnOrderClick(self):
    self.sceneService.switchToScene("dining_no_customer")

  def onUndoClick(self):
    self.kitchenService.undo()
    self.updateSummaryLines()
  
  def renderIngredientImages(self, screen):
    self.noodles_image.render(screen)
    self.rice_image.render(screen)
    self.chicken_image.render(screen)
    self.beef_image.render(screen)
    self.pork_image.render(screen)
    self.carrots_image.render(screen)
    self.pepper_image.render(screen)
    self.broccoli_image.render(screen)

  def renderIngredientButtons(self, screen):
    self.rice_button.render(screen)
    self.noodles_button.render(screen)
    self.chicken_button.render(screen)
    self.pork_button.render(screen)
    self.beef_button.render(screen)
    self.carrots_button.render(screen)
    self.broccoli_button.render(screen)
    self.pepper_button.render(screen)

  def renderOrdersList(self, screen):
    for pos in self.orderImagePositions:
      self.squiggles_image.render(screen, pos)

    for button in self.orderViewButtons:
      button.render(screen)

  def handleEvents(self, events, keys):
    for event in events:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pressed()[0]:
          self.rice_button.handleClick()
          self.noodles_button.handleClick()
          self.chicken_button.handleClick()
          self.pork_button.handleClick()
          self.beef_button.handleClick()
          self.broccoli_button.handleClick()
          self.carrots_button.handleClick()
          self.pepper_button.handleClick()

          for button in self.orderViewButtons:
            button.handleClick()
          
          self.startAnOrderButton.handleClick()
          self.undoButton.handleClick()
          break

  def renderSummary(self, screen):
    pygame.draw.rect(screen, "white",[498, 124, 230, 341])
    self.summaryTitle.render(screen)
    for line in self.summaryLines:
      line.render(screen)
  
  def render(self, screen):
    screen.fill((194, 226, 247))
    self.title.render(screen)

    self.renderIngredientImages(screen)
    self.renderIngredientButtons(screen)
    
    self.renderSummary(screen)

    self.renderOrdersList(screen)

    self.undoButton.render(screen)
    self.startAnOrderButton.render(screen)