import pygame
import random
from libs.SimpleArcade.gui import Label
from libs.SimpleArcade import Game
from libs.SimpleArcade import Arcade


class Snake(Game.Game):

    def __init__(self):
        super().__init__("Snake", (pygame.image.load("games/Snake/snake_SimpleArcade.jpg")))

    def rutnat(self, lx, ly, screen):
    #Funktion som ritar ut rutnätet
        pygame.draw.line(screen, self.vitisch, (self.gridx, self.gridy),(self.gridx, self.gridy+500), 1)
        pygame.draw.line(screen, self.vitisch, (self.gridx, self.gridy),(self.gridx+500, self.gridy), 1)
        for i in range(25):
            lx += 20
            ly += 20
            pygame.draw.line(screen, self.vitisch, (self.gridx+lx, self.gridy),(self.gridx+lx, self.gridy+500), 1)
            pygame.draw.line(screen, self.vitisch, (self.gridx, self.gridy+ly),(self.gridx+500, self.gridy+ly), 1)

    def ormRit(self, screen):
        #Funktion som ritar ormen
        self.snakeHuvud = pygame.draw.rect(screen, (0, max(255-self.langdLi*3, 100), 0), (self.x, self.y, self.width, self.height))

        self.svansLi.clear()
        for q in range(self.langdLi):
            snakeSvans = pygame.draw.rect(screen, (0, max(255-q*3, 100), 0), (self.xLista[q], self.yLista[q], self.width, self.height))
            self.svansLi.append(snakeSvans)

        self.xLista.append(self.x)
        self.yLista.append(self.y)
        self.xLista.pop(0)
        self.yLista.pop(0)

    def onPlay(self):
        self.gridx = Arcade.SCREEN_WIDTH/2-(20*24)/2
        self.gridy = Arcade.SCREEN_HEIGHT/2-(20*24)/2

        #Färger
        self.vitisch = (225, 225, 225)
        self.svart = (0, 0, 0)
        self.rod = (255, 0, 0)
        self.gron = (0, 255, 0)

        #Ormen:
        self.x = self.gridx+200
        self.y = self.gridy+200
        self.width = 20
        self.height = 20
        self.langdLi = 0
        self.xLista = []
        self.yLista = []
        self.svansLi = []

        #Äpplet:
        self.width2 = 10
        self.height2 = 10
        self.apple = pygame.Rect(0, 0, self.width2, self.height2)

        #Hastighet
        self.xVel = 0
        self.yVel = 0
        self.speed = 20

        self.appletfinns = False
        self.gameOver = False
        self.ifMoving = False

        self.snakeHuvud = pygame.Rect(self.gridx, self.gridy, self.width, self.height)

        self.label = Label.Label(x=self.gridx, y=self.gridy)
        self.label.addText('Game Over', Arcade.FONT, (139, 0, 0), 200)
        self.label.alignHorizontally(None, Arcade.ALIGN_CENTER)
        self.label.alignVertically(None, Arcade.ALIGN_CENTER)

        self.label2 = Label.Label(x=self.gridx, y=self.gridy-60)
        self.label2.addText('Använd joysticken för att starta', Arcade.FONT, (139, 0, 0), 50)

 
    def update(self, screen):
        #Gör ormens förflself.yttning hackigare
        pygame.time.delay(100)
        #Gör skärmen svart igen efter varje förflyttning
        screen.fill(self.svart)

        #Rutnät
        lx = 0
        ly = 0
        self.rutnat(lx, ly, screen)

        if self.gameOver == False:
            if self.ifMoving == False:
                self.label2.update(screen)#GTGDFVTHGRFGFEFSDFTRGHTTHYGH


            #Förflyttning
            keys = pygame.key.get_pressed()

            if keys [pygame.K_LEFT] and self.xVel == 0:
                self.xVel = -self.speed
                self.yVel = 0
                self.ifMoving = True
            
            elif keys [pygame.K_RIGHT] and self.xVel == 0:
                self.xVel = self.speed
                self.yVel = 0
                self.ifMoving = True

            elif keys [pygame.K_UP] and self.yVel == 0:
                self.yVel = -self.speed
                self.xVel = 0
                self.ifMoving = True

            elif keys [pygame.K_DOWN] and self.yVel == 0:
                self.yVel = self.speed
                self.xVel = 0
                self.ifMoving = True

            self.x+=self.xVel
            self.y+=self.yVel

            #Ritar ormen
            self.snakeHuvud = pygame.draw.rect(screen, self.gron, (self.x, self.y, self.width, self.height))
            self.ormRit(screen)

            #Äpplet
            if self.appletfinns == False:
                self.apple.x = random.randrange(5+self.gridx, 500-self.width2+self.gridx, 20)
                self.apple.y = random.randrange(5+self.gridy, 500-self.width2+self.gridy, 20)
                if self.apple.x in self.xLista and self.apple.y in self.yLista:
                    self.appletfinns = False
                else:
                    self.appletfinns = True
            
            pygame.draw.rect(screen, self.rod, self.apple)

            #Ormens position
            snake = pygame.Rect(self.x, self.y, self.width, self.height)

            #Kontrollerar om ormen äter ett äpple, gör den det så förlänger den ormen
            if self.apple.colliderect(snake) == True:
                self.appletfinns = False

                #Förlänger ormen
                self.langdLi += 1
                self.xLista.append(self.x)
                self.yLista.append(self.y)
                print(self.langdLi)

        
        if self.gameOver == True:
            self.label.update(screen)
            
            

        keys = pygame.key.get_pressed()
        if keys [pygame.K_SPACE]:
            self.gameOver = False

            self.x = self.gridx+200
            self.y = self.gridy+200
            self.xVel = 0
            self.yVel = 0
            self.svansLi = []
            self.langdLi = 0
            self.xLista = []
            self.yLista = []

        #Kontrollerar om ormen är utanför skärmen
        if self.x > self.gridx+480 or self.x < self.gridx or self.y > self.gridy+480 or self.y < self.gridy:
            self.gameOver = True

        #Kontrollerar så att ormen inte kör in i sig själv
        if self.langdLi > 4:
            for svans in self.svansLi:
                if svans.colliderect(self.snakeHuvud) == True:
                    self.gameOver = True
