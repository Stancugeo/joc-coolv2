import pygame
class Player():
    def __init__(self,SizeY,SizeX,PosX = 0 ,PosY = 0):
        self.SizeX = SizeX
        self.SizeY = SizeY

        self.Death = False
        self.lives = 3
        self.speed = 0

        self.PosX = PosX
        self.PosY = PosY

        self.movement_mode = ["toleft","stay","toright"]


        self.attack = []
        self.sprites = []

        self.Exist = True



        self.image = pygame.image.load("spaceship.png")

        self.rect = self.image.get_rect()
        self.is_animating = False

        self.px = self.PosX + self.SizeX / 2
        self.py = self.PosY + self.SizeY / 2 + 10
        self.radius = 52

    def move(self,direction):
        lead_x_change = 0
        if direction == "LEFT":
            lead_x_change = -3
        if direction == "RIGHT":
            lead_x_change = 3
        self.PosX = self.PosX + lead_x_change
        self.px = self.PosX + self.SizeX / 2

    def draw(self,screen,PosX = 0 , PosY = 0):
        if PosX == 0 : PosX = self.PosX
        if PosY == 0 : PosY = self.PosY
        screen.blit(self.image,(PosX,PosY,self.SizeX,self.SizeY))




































