import pygame
import mainmenu as mm


pygame.init()
menu = mm.MainMenu()


screen = pygame.display.set_mode([900,900])
clock = pygame.time.Clock()



while menu.Running:
    menu.MainMenu_state(screen)
    pygame.display.update()



pygame.quit()




