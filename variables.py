import pygame
class Player:
    x = 98
    y = 84
class Asteroid:
    x = 40
    y = 40

class Heart:
    x = 20
    y = 20
    image = pygame.image.load("Heart.png")
    pygame.transform.scale(image,(20,20))



