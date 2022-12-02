import pygame
from .base_scene import BaseScene
from ..components import Textbox, Button, Image

class ResultsScene(BaseScene):
  def __init__(self, context):
    BaseScene.__init__(self, BaseScene)
    
    self.context = context
    self.sceneService = context["scene"]
    self.orderService = context["order"]
    self.kitchenService = context["kitchen"]
    self.scoreService = context["score"]
    
    self.order_image = Image(
      r"./assets/orderBackground.png",
      (0, 0),
      lambda img : pygame.transform.scale(img, (750, 500))
    )
    self.player = Image(
      r"./assets/playerboy.png",
      (20, 208),
      lambda img : pygame.transform.flip(img, True, False),
      lambda img : pygame.transform.scale(img, (140, 280))
    )
    self.customer = Image(
      r"./assets/customer.png",
      (150, 208),
      lambda img : pygame.transform.scale(img, (140, 280))
    )

    font = pygame.font.SysFont("Helvetica", 24)
    
    self.takeAnOrderButton = Button(
      (214, 46),
      (318, 444),
      (293, 433),
      text="Take an Order",
      font = font,
      onClick=self.onTakeOrder
    )
    self.goToKitchenButton = Button(
      (214, 46),
      (543, 444),
      (518, 433),
      text="Go To Kitchen",
      font = font,
      onClick = self.goToKitchen
    )
    
    order, index = self.kitchenService.getFocus()
    self.summaryTitle = Textbox(
      f"ORDER {order['id']}",
      (370, 42)
    )

    summary_font = pygame.font.SysFont("Helvetica", 20)
    tips, computedLines = self.kitchenService.computeDifference(order)
    self.kitchenService.reset()
    self.orderService.removeOrder(order)
    self.scoreService.addTip(tips)
    self.summaryLines = []
    for i, line in enumerate(computedLines):
      self.summaryLines.append(
        Textbox(
          line,
          (370, 90 + 40*i),
          font= summary_font
        )
      )

    self.tips_text = Textbox(
      "Tips: ${:.2f}".format(self.scoreService.getTips()), 
      (17, 15), 
      font = font
    )

  def handleEvents(self, events, keys):
    for event in events:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pressed()[0]:
          self.takeAnOrderButton.handleClick()
          self.goToKitchenButton.handleClick()

  def renderSummary(self, screen):
    pygame.draw.rect(screen, "white", [345, 32, 350, 394])
    self.summaryTitle.render(screen)
    for line in self.summaryLines:
      line.render(screen)
          
  def render(self, screen):
    self.order_image.render(screen)
    self.player.render(screen)
    self.customer.render(screen)
    
    self.renderSummary(screen)
    
    self.tips_text.render(screen)

    self.goToKitchenButton.render(screen)
    self.takeAnOrderButton.render(screen)

  def onTakeOrder(self):
    self.sceneService.switchToScene("dining_no_customer")
  
  def goToKitchen(self):
    self.sceneService.switchToScene("kitchen_scene", context=self.context, reset=True)
    
