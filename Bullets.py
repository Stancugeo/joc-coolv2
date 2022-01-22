from cmath import sqrt
from math import sqrt
import pygame
import random
class Bullet():
    Bullet_list = []
    Bullet_sprites = [pygame.image.load("Bullet1form-1.2.png.png"),pygame.image.load("Bullet1form-1.2.png.png"),pygame.image.load("Bullet1form-1.2.png.png")]
    def __init__(self,posX,posY):
        self.sizeX = 9
        self.sizeY = 18
        self.posX = posX
        self.posY = posY
        self.Exist = True
        self.image = Bullet.Bullet_sprites[random.randint(0,2)]
        self.image = pygame.transform.scale(self.image, (self.sizeX, self.sizeY))


    def draw(self,screen):
        screen.blit(self.image, (self.posX, self.posY))
        #pygame.draw.rect(screen,(210, 43, 43),(self.posX,self.posY,self.sizeX,self.sizeY),2)
    def update(self):
        self.posY = self.posY - 3
    def check(self):
        if self.posY < 0 - self.sizeY:
            return True
        return False

    def collision (self,x,y,radius):
        x = x - 5
        y = y - 5
        radius = radius - 8
        distanceX = abs(x - self.posX)
        distanceY = abs(y - self.posY)
        if distanceX > (self.sizeX/2 + radius): return False
        if distanceY > (self.sizeY/2 + radius): return False
        if distanceX <= (self.sizeX/2): return True
        if distanceY <= (self.sizeY/2): return True
        cDist = (distanceX - self.sizeX/2)*(distanceX - self.sizeX/2) + (distanceY - self.sizeY/2)*(distanceY - self.sizeY/2)
        if cDist <= radius*radius:
            return True
        else : return False


    def check2(self,enemy):
        if self.posY < enemy.posY:
            if self.posX >= enemy.posX and self.posX <= enemy.posX + enemy.sizeX:
                return True
        return False



    def __del__(self):
        self.Exist = False
        del self.image



