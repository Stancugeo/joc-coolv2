import pygame
import random
class Asteroid():
    Asteroids = []
    nr_asteroids = 0

    def __init__(self,PosX , PosY , sizeX , sizeY ):
        self.x = sizeX
        self.y = sizeY
        self.image = pygame.image.load("Asteroid (1).png")
        self.image = pygame.transform.scale(self.image, (self.x, self.y))

        self.PosX = PosX
        self.PosY = PosY

        self.angle = 0

        self.px = PosX + sizeX
        self.py = PosY + sizeY
        self.radius = sizeX/2

        
        self.speed = random.uniform(1,3)

    def __del__(self):
        del self.image













