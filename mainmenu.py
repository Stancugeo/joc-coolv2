import pygame
import game2 as gg

class MainMenu():
    def __init__(self):

        self.game = gg.Game()
        self.contor = 0
        self.Display_x = 900
        self.Display_y = 900
        self.movement = 0
        self.Background = pygame.Rect(0,0,self.Display_x,self.Display_y)
        self.Running = True



        self.enter = False


    def MainMenu_state(self,screen):

        self.font = pygame.font.SysFont(None, 100)
        self.enterX = pygame.font.SysFont(None, 75)
        self.StartButton = self.font.render('START', True, (255, 255, 255))
        self.Options = self.font.render('EXIT', True, (255, 255, 255))
        self.EXIT = self.font.render('CREDITS', True, (255, 255, 255))
        self.MainMenu = pygame.Rect(0, 0, self.Display_x, self.Display_y)

        self.X = self.enterX.render('->', True, (255, 255, 255))

        self.stats = [(self.StartButton.get_rect().centerx, -100),
                      (self.Options.get_rect().centerx, 0),
                      (self.EXIT.get_rect().centerx, 100)]

        pygame.draw.rect(screen,(0,0,0),self.MainMenu)
        screen.blit(self.StartButton ,[ self.Display_x / 2 - self.StartButton.get_rect().centerx , self.Display_y / 2 - 100 ])
        screen.blit(self.Options, [self.Display_x / 2 - self.Options.get_rect().centerx  , self.Display_y / 2  ])
        screen.blit(self.EXIT, [self.Display_x / 2 - self.EXIT.get_rect().centerx  , self.Display_y / 2 + 100 ])
        self.keyfunctionality()

        screen.blit(self.X, (self.Display_x / 2 - self.stats[self.contor][0] - self.X.get_rect().right,
                                 self.Display_y / 2 + self.stats[self.contor][1]))


        self.exit_mm()
        self.start_game(screen)

        self.enter = False



    def keyfunctionality(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.Running = False
            userInput = pygame.key.get_pressed()
            if userInput[pygame.K_DOWN]:
                self.contor = self.contor + 1
            if userInput[pygame.K_UP]:
                self.contor = self.contor - 1
            if userInput[pygame.K_LEFT]:
                self.enter = True

            if self.contor >= 3: self.contor = 0
            if self.contor < 0: self.contor = 2


    def exit_mm(self):
        if self.contor == 1 and self.enter:
            self.Running = False

    def start_game(self,screen):
        if self.contor == 0 and self.enter:
            self.game.Running = True
        while self.game.Running:
            self.game.Game_state(screen)
            pygame.display.update()






























