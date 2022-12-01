import pygame
pygame.init()

##Global Vars
COLOR = (255, 100, 98)
SURFACE_COLOR = (100, 255, 150)
WIDTH = 500
HEIGHT = 500

##Sample Object Class for Making Sprite
class Sprite(pygame.sprite.Sprite):
  def __init__(self, color, height, width):
    super().__init__()
    self.image = pygame.Surface([width, height])
    self.image.fill(SURFACE_COLOR)
    self.image.set_colorkey(COLOR)

    pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
    self.rect = self.image.get_rect()


red = (255, 0, 0)
screen_size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(screen_size) ## 500 x 500 screen
list_of_sprites = pygame.sprite.Group()
obj = Sprite(red, 30, 30) ## red cube Sprite
obj.rect.x = 240 ## x pos of sprite
obj.rect.y = 240 ## y pos of sprite
list_of_sprites.add(obj)

exit = True
clock = pygame.time.Clock()

while exit:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit = False
  list_of_sprites.update() ##updates all sprites in list_of_sprites
  screen.fill(SURFACE_COLOR)
  list_of_sprites.draw(screen)
  pygame.display.flip()
  clock.tick(60)

pygame.quit()



class Menu:
  res = (500, 500) ## screen size
  screen = pygame.display.set_mode(res)
  color = (0, 0, 0) ## color of text
  button_base_color = (235, 225, 255) 
  button_base_shade = (165, 145, 200) ##shade button
  screen_width = screen.get_width()
  screen_height = screen.get_height()

  font = pygame.font.SysFont("Arial", 30)
  text = font.render("quit", True, color)

  while True:
    for the_event in pygame.event.get():
      if the_event.type == pygame.MOUSEBUTTONDOWN:
        if screen_width / 2 <= mouse[0] <= screen_width / 2 + 140 and height/2 <= mouse[1] <= height/2 + 40:
          pygame.quit()

  mouse = pygame.mouse.get_pos()
  screen.blit(text, (screen_width/2 + 50, height/2))
  pygame.display.update()