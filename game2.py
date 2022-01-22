from math import  sqrt

import pygame
import player as p
import Bullets as b
import variables as v
import Asteroid as ast
import random


class Game():
    def __init__(self):
        self.bkg = pygame.image.load("space.png")
        self.y = 0
        self.Player1 = p.Player(v.Player.y, v.Player.x, 900 / 2 - v.Player.x / 2, 1000 - v.Player.y - 100, )

        self.SCORE = '0'
        self.font = pygame.font.SysFont(None, 40)
        self.Score = self.font.render('SCORE: ' + self.SCORE, True, (255, 255, 255))

        self.Running = False
        self.pause = False
        self.Enemies = []
        self.enemies = 0
        self.time = 0
        self.upgrade = pygame.image.load("Wrench key.png")
        pygame.transform.scale(self.upgrade,(18,18))
        self.upgrade_stage = 1
        self.bullet_stages = [(self.Player1.PosX + self.Player1.SizeX / 2 + 9 / 2, self.Player1.PosY + 18 / 2),
                              ((self.Player1.PosX + 3 * self.Player1.SizeX / 7 + 9 / 2 , self.Player1.PosY + 18/2),(self.Player1.PosX + 5 * self.Player1.SizeX / 7 + 9 / 2 , self.Player1.PosY + 18/2))]

        self.cnt = random.randint(150,200)

    def Game_state(self,screen):
        self.background(screen)

        self.bullet_update(screen)
        if self.Player1.Exist == True:
            #pygame.draw.rect(screen,(210, 43, 43),(self.Player1.PosX,self.Player1.PosY + 5/6 * self.Player1.SizeY - 5 ,self.Player1.SizeX,1))
            #pygame.draw.circle(screen, (210, 43, 43), (self.Player1.PosX + self.Player1.SizeX / 2  ,self.Player1.PosY + self.Player1.SizeY / 2 + 10 ), 52 , 2)
            #pygame.draw.rect(screen,(210, 43, 43),(self.Player1.px,self.Player1.py,1,1),1)
            #pygame.draw.rect(screen, (210, 43, 43), (self.Player1.px, self.Player1.py -  2 * self.Player1.SizeY / 3 , 3, 3), 1)
            self.keyfunctionality()
            self.Player1.draw(screen)
            if self.Player1.lives > 0:
                h = v.Heart()
                for i in range(self.Player1.lives):
                    screen.blit(h.image,( h.x + 2 *i*h.x,900 - h.y - h.y/2 ))

        self.print_score(screen)



        if self.enemies <= 0 or self.time == 0:
            self.create_enemies()
            self.cnt = random.randint(50,100)


        self.check()
        self.draw(screen)
        self.update()



        self.clock()



    def background(self,screen):
        screen.fill((0, 0, 0))
        self.rel_y = self.y % self.bkg.get_rect().height
        screen.blit(self.bkg, (0, self.rel_y - self.bkg.get_rect().height))

        if self.rel_y < self.bkg.get_rect().height:
            screen.blit(self.bkg, (0, self.rel_y))
        self.y += 1



    def keyfunctionality(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.Bullet = b.Bullet(self.Player1.PosX + self.Player1.SizeX / 2 + 9 / 2, self.Player1.PosY + 18 / 2)
                    self.Player1.attack.append(self.Bullet)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.Player1.move("LEFT")
        if keys[pygame.K_RIGHT]:
            self.Player1.move("RIGHT")

    def bullet_update(self,screen):

        for each_bullet in self.Player1.attack:
            each_bullet.update()
            each_bullet.draw(screen)
            if each_bullet.check():
                self.Player1.attack.remove(each_bullet)


    def create_enemies(self):
        list = []
        size = random.randint(40,50)
        col = 9
        for i in range(col):
            ok = True
            my_enemy = ast.Asteroid(random.randint(0, 1000 - int(size * 4)), - size * 3/2, size, size)
            for each_enemy in list:
                dx = ( my_enemy.px - each_enemy.px ) * ( my_enemy.px - each_enemy.px )
                dy = ( my_enemy.py - each_enemy.py ) * ( my_enemy.py - each_enemy.py )
                distance = int(sqrt(dx + dy))
                if distance <= my_enemy.radius + each_enemy.radius :
                    ok = False
                    break

            if ok :
                list.append(my_enemy)

        for my_enemy in list:
            ok = True
            for each_enemy in self.Enemies:
                if my_enemy.speed > each_enemy.speed :
                    if my_enemy.px - my_enemy.x/2 >= each_enemy.px - each_enemy.x/2 and my_enemy.px - my_enemy.x/2 <= each_enemy.px + each_enemy.x/2:
                        ok = False
                        break
                    elif my_enemy.px + my_enemy.x/2 <= each_enemy.px + each_enemy.x/2 and my_enemy.px + my_enemy.x/2 >= each_enemy.px - each_enemy.x/2:
                        ok = False
                        break
            if ok:
                self.Enemies.append(my_enemy)
                self.enemies = self.enemies + 1


    def draw(self,screen):
            for each_enemy in self.Enemies:
                rotated_image = pygame.transform.rotate(each_enemy.image,each_enemy.angle)
                each_enemy.angle = each_enemy.angle - float(each_enemy.speed/3)
                new_rect = rotated_image.get_rect( center=( each_enemy.image.get_rect(center = (each_enemy.x , each_enemy.y )).center ) )
                screen.blit(rotated_image,(new_rect.x + each_enemy.PosX , new_rect.y + each_enemy.PosY ))
                #pygame.draw.circle(screen, (210, 43, 43),
                #                (each_enemy.px , each_enemy.py ),
                #                each_enemy.x/2 , 2)
                #pygame.draw.rect(screen,(0, 9, 255),(each_enemy.px - each_enemy.x/2 ,each_enemy.py ,3,3))
                #pygame.draw.rect(screen, (0, 9, 255), (each_enemy.px + each_enemy.x / 2, each_enemy.py, 3, 3))

                #pygame.draw.rect(screen, (0, 9, 255), (each_enemy.px , each_enemy.py - each_enemy.y / 2 , 3, 3))

    def check(self):
        for each_enemy in self.Enemies:
            if each_enemy.py + each_enemy.y/2 >= 1000:
                self.Enemies.remove(each_enemy)
                self.enemies = self.enemies - 1
                del each_enemy
            else:
                for each_bullet in self.Player1.attack:
                    if each_bullet.collision(each_enemy.px, each_enemy.py, each_enemy.radius):
                        self.Enemies.remove(each_enemy)
                        self.enemies = self.enemies - 1
                        self.Player1.attack.remove(each_bullet)
                        self.add_score()

                        del each_enemy
                        del each_bullet
                        break
                for each_enemy in self.Enemies:
                    dx = (self.Player1.px - each_enemy.px) * (self.Player1.px - each_enemy.px)
                    dy = (self.Player1.py - each_enemy.py) * (self.Player1.py - each_enemy.py)
                    distance = int(sqrt(dx + dy))
                    if each_enemy.py - each_enemy.y / 2 <=  self.Player1.PosY + self.Player1.SizeY / 2 + 10 + 5 :
                        if distance <= self.Player1.radius + each_enemy.radius - 10 :
                            self.Enemies.remove(each_enemy)
                            self.enemies = self.enemies - 1
                            self.Player1.lives = self.Player1.lives - 1
                            del each_enemy
                            break



    def update(self):

        for each_enemy in self.Enemies:
            each_enemy.PosY = each_enemy.PosY + each_enemy.speed
            each_enemy.py = each_enemy.PosY + each_enemy.y

    def clock(self):
        self.time = (self.time + 1) % self.cnt

    def print_score(self,screen):
        screen.blit(self.Score,(900 - self.Score.get_rect().bottomright[0] - 10 ,900 - self.Score.get_rect().bottomright[1] - 10 ))

    def add_score(self):
        self.SCORE = str(int(self.SCORE) + random.randint(1,4))
        self.Score = self.font.render('SCORE: ' + self.SCORE, True, (255, 255, 255))




