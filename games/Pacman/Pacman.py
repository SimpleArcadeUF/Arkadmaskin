import pygame, os
from libs.SimpleArcade import Game
from libs.SimpleArcade import Arcade

class Packman(Game.Game):
        
    def __init__(self):
        super().__init__("Pacman", pygame.image.load("games/FlappyBird/images/logo.png"))
        self.screen = Arcade.screen
        self.clock = Arcade.clock
        
        self.tileSize = 40 # Size of each tile
        self.gameLevel = [ # 0 = Wall, 1 = Smallball, 2 = Bigball
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
            [0, 2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 2, 0],
            [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0], 
            [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0], # Halfway
            [0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 2, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]  # Total size is 13x13
    
        self.pos = [11, 6]
        self.dir = "none"
    
    def onPlay(self):
        super().onPlay()

    def update(self, screen):
        super().update(screen)
        self.renderGame()
        self.inputs()
        self.movement()

    def renderGame(self):
        self.screen.fill((0, 0, 0)) # Fill the screen black

        for i in range(len(self.gameLevel)):
            for j in range(len(self.gameLevel[0])):
                if (self.gameLevel[i][j] == 0): # Draw the wall tile
                    pygame.draw.rect(self.screen, (0, 0, 255), (j * self.tileSize, i * self.tileSize, self.tileSize, self.tileSize))
                elif (self.gameLevel[i][j] == 1): # Draw the small balls
                    pygame.draw.circle(self.screen, (255, 255, 255), (j * self.tileSize + self.tileSize//2, i * self.tileSize + self.tileSize//2), self.tileSize//8)
                elif (self.gameLevel[i][j] == 2): # Draw the bigger balls
                    pygame.draw.circle(self.screen, (255, 255, 255), (j * self.tileSize + self.tileSize//2, i * self.tileSize + self.tileSize//2), self.tileSize//5)
          
                if (self.pos[0] == i and self.pos[1] == j):
                    pygame.draw.circle(self.screen, (255, 255, 0), (j * self.tileSize + self.tileSize//2, i * self.tileSize + self.tileSize//2), self.tileSize//3)
                    if (self.gameLevel[i][j] == 1):
                        self.gameLevel[i][j] = 3
                    elif (self.gameLevel[i][j] == 2):
                        self.gameLevel[i][j] = 3

    def inputs(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                exit()

        if (Arcade.JOYSTICK_PRESSED_UP):
            self.dir = "up"
        elif (Arcade.JOYSTICK_PRESSED_DOWN):
            self.dir = "down"
        elif (Arcade.JOYSTICK_PRESSED_LEFT):
            self.dir = "left"
        elif (Arcade.JOYSTICK_PRESSED_RIGHT):
            self.dir = "right"

    def movement(self):
        if (self.dir == "up"):
            if (self.gameLevel[self.pos[0] - 1][self.pos[1]] != 0):
                self.pos[0] -= 1
            else:
                self.dir = "none"
        elif (self.dir == "down"):
            if (self.gameLevel[self.pos[0] + 1][self.pos[1]] != 0):
                self.pos[0] += 1
            else:
                self.dir = "none"
        elif (self.dir == "left"):
            if (self.gameLevel[self.pos[0]][self.pos[1] - 1] != 0):
                self.pos[1] -= 1
            else:
                self.dir = "none"
        elif (self.dir == "right"):
            if (self.gameLevel[self.pos[0]][self.pos[1] + 1] != 0):  
                self.pos[1] += 1
            else:
                self.dir = "none"
        
        
        


