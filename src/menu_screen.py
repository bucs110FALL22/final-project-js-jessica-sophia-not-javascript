import pygame
pygame.init()


class Menu: 
  res = (500, 500) ## screen size
  screen = pygame.display.set_mode(res) ## open window
  dining_hall_image = pygame.image.load(("../assets/dining_hall.jpg"))
  
  ## colors go here
  color_of_buttons_text = (0, 0, 0) ## color of quit text
  color_of_title_text = (255, 255, 255) ## color of text
  button_base_color = (235, 225, 255) 
  button_base_shade = (165, 145, 200) ## shade button
  
  screen_width = screen.get_width() ## store screen width
  screen_height = screen.get_height() ## store screen height
  
  ## texts go here
  font = pygame.font.SysFont("Helvetica", 35)
  quit_text = font.render("Quit", True, color_of_buttons_text)
  title_text = font.render("JS' Dining Halleria", True, color_of_title_text)
  help_text = font.render("Help", True, color_of_buttons_text)
  start_text = font.render("Start", True, color_of_buttons_text)

  ## functionality (only quit button currently functions)
  ## might be easier to make button objects
  ## should this move to somewhere else? said models should not contain events
  while True:
    mouse = pygame.mouse.get_pos()
    for the_event in pygame.event.get():
      if the_event.type == pygame.QUIT:
        pygame.quit()
      if the_event.type == pygame.MOUSEBUTTONDOWN:
        if screen_width/2 - 70 <= mouse[0] <= screen_width/2+ 70 and screen_height/2 - 20 <= mouse[1] <= screen_height/2+ 20:
          pygame.quit()  
        

  ## visuals
    screen.fill((255 , 255, 255))
    screen.blit(dining_hall_image, (0, 0)) 
    pygame.draw.rect(screen, button_base_color,[screen_width/2 - 70, screen_height/2 - 20, 140, 40]) ## visual for quit button (middle)
    pygame.draw.rect(screen, button_base_color,[screen_width/2 - 70, screen_height/2 + 40, 140, 40]) ## visual for help button (bottom)
    pygame.draw.rect(screen, button_base_color,[screen_width/2 - 70, screen_height/2 - 80, 140, 40]) ## visual for start button (top)
    screen.blit(quit_text, (screen_width/2 - 35, screen_height/2 - 20))
    screen.blit(help_text, (screen_width/2 - 35, screen_height/2 + 40)) 
    screen.blit(start_text, (screen_width/2 - 35, screen_height/2 - 80)) 
    screen.blit(title_text, (screen_width/2 - 160, 40)) 
    
    pygame.display.update()

    
