import pygame
class Enemy():
    def __init__(self,sizeX,sizeY,posX,posY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.posX = posX
        self.posY = posY
        self.posX_init = posX

        self.Exist = True
        self.image = pygame.image.load("mob1.png")
        self.image = pygame.transform.scale(self.image,(sizeX,sizeY))
        self.clock = 0
        self.Step = True
        self.get_hits = 0




    def draw(self, screen):
        screen.blit(self.image,(self.posX,self.posY))

    def update(self):
        if self.get_hits < 3:
            return True
        else:
            return False




    def dead(self):
        self.Exist = False
    def __del__(self):
        self.Exist = False
        del self.image




