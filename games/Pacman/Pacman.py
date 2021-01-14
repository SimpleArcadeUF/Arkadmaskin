import pygame, os
from libs.SimpleArcade import Game
from libs.SimpleArcade import Arcade

class Packman(Game.Game):
        
    def __init__(self):
        super().__init__("Pacman", pygame.image.load("games/FlappyBird/images/logo.png"))
        self.screen = Arcade.screen
        
        self.tileSize = 20 # Size of each tile
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
        ]  
    
    
    def onPlay(self):
        super().onPlay()

    def update(self, screen):
        super().update(screen)
        self.renderGame(self)

    def renderGame(self):
        self.screen.fill((0, 0, 0)) # Fill the screen black

        for i in range(len(self.gameLevel)):
            for j in range(len(self.gameLevel[0])):
                if (self.gameLevel[i][j] == 0): # Draw the wall tile
                    pygame.draw.rect(self.screen, (0, 0, 255), (j * self.tileSize, i * self.tileSize, self.tileSize, self.tileSize))
                elif (self.gameLevel[i][j] == 1): # Draw the small balls
                    pygame.draw.circle(self.screen, (255, 255, 255), (j * self.tileSize + self.tileSize//2, i * self.tileSize + self.tileSize//2), self.tileSize//8)
                elif (self.gameLevel[i][j] == 1): # Draw the bigger balls
                    pygame.draw.circle(self.screen, (211, 211, 211), (j * self.tileSize + self.tileSize//2, i * self.tileSize + self.tileSize//2), self.tileSize//5)

    
        
