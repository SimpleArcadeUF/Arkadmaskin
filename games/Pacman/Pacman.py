import pygame, os
from libs.SimpleArcade import Game
from libs.SimpleArcade import Arcade
from libs.SimpleArcade import Timer
from libs.SimpleArcade import SpriteSheet
from libs.SimpleArcade import Animation

class Packman(Game.Game):
        
    def __init__(self):
        super().__init__("Pacman", pygame.image.load("games/Pacman/img/logo.jpg"))

    def onPlay(self):
        super().onPlay()

        self.screen = Arcade.screen
        self.timer = Timer.Timer(1)
        self.timer.start()
        
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

        self.pos = [6, 11]
        self.dir = "none"
        self.nextMove = "none"

        self.xOffset = 0
        self.yOffset = 0

        self.DisplayXOffset = Arcade.SCREEN_WIDTH / 2 - (self.tileSize * len(self.gameLevel[1])) / 2
        self.DisplayYOffset = Arcade.SCREEN_HEIGHT / 2 - (self.tileSize * len(self.gameLevel)) / 2

        self.movementSpeed = 3

        entitySpriteSheet = SpriteSheet.SpriteSheet("games/Pacman/img/entites2.png", 16)
        entitySpriteSheet.scaleImages(32)
        self.AnimPlayerUp = Animation.Animation(entitySpriteSheet.getImagesByRow(2, 2), 400, continuous=True)
        self.AnimPlayerUp.start()
        self.AnimPlayerRight = Animation.Animation(entitySpriteSheet.getImagesByRow(0, 2), 400, continuous=True)
        self.AnimPlayerRight.start()
        self.AnimPlayerDown = Animation.Animation(entitySpriteSheet.getImagesByRow(3, 2), 400, continuous=True)
        self.AnimPlayerDown.start()
        self.AnimPlayerLeft = Animation.Animation(entitySpriteSheet.getImagesByRow(1, 2), 400, continuous=True)
        self.AnimPlayerLeft.start()

        self.CurrentAnim = self.AnimPlayerUp

    def update(self, screen):
        super().update(screen)
        self.renderGame()
        self.inputs()
        self.movement()
        self.timer.update()
        self.CurrentAnim.update()

    def renderGame(self):
        self.screen.fill((0, 0, 0)) # Fill the screen black

        for i in range(len(self.gameLevel)):
            for j in range(len(self.gameLevel[0])):
                if (self.gameLevel[i][j] == 0): # Draw the wall tile
                    pygame.draw.rect(self.screen, (0, 0, 255), (j * self.tileSize + self.DisplayXOffset, i * self.tileSize + self.DisplayYOffset, self.tileSize, self.tileSize))
                elif (self.gameLevel[i][j] == 1): # Draw the small balls
                    pygame.draw.circle(self.screen, (255, 255, 255), (j * self.tileSize + self.tileSize//2 + self.DisplayXOffset, i * self.tileSize + self.tileSize//2 + self.DisplayYOffset), self.tileSize//8)
                elif (self.gameLevel[i][j] == 2): # Draw the bigger balls
                    pygame.draw.circle(self.screen, (255, 255, 255), (j * self.tileSize + self.tileSize//2 + self.DisplayXOffset, i * self.tileSize + self.tileSize//2 + self.DisplayYOffset), self.tileSize//5)
          
    def inputs(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                exit()

        if (Arcade.JOYSTICK_PRESSED_UP):
            if (self.xOffset == 0 and self.yOffset == 0):
                self.dir = "up"
                self.nextMove = "none"
            else:
                self.nextMove = "up"

        elif (Arcade.JOYSTICK_PRESSED_DOWN):
            if (self.xOffset == 0 and self.yOffset == 0):
                self.dir = "down"
                self.nextMove = "none"
            else:
                self.nextMove = "down"

        elif (Arcade.JOYSTICK_PRESSED_LEFT):
            if (self.xOffset == 0 and self.yOffset == 0):
                self.dir = "left"
                self.nextMove = "none"
            else:
                self.nextMove = "left"

        elif (Arcade.JOYSTICK_PRESSED_RIGHT):
            if (self.xOffset == 0 and self.yOffset == 0):
                self.dir = "right"
                self.nextMove = "none"
            else:
                self.nextMove = "right"

    def movement(self):
        print("Dir =", str(self.dir), ", NextDir =", str(self.nextMove))
        self.screen.blit(self.CurrentAnim.getCurrentFrame(), (self.pos[0] * self.tileSize + self.xOffset + self.DisplayXOffset + 1, self.pos[1] * self.tileSize + self.yOffset + self.DisplayYOffset + 3))
        # pygame.draw.circle(self.screen, (255, 255, 0), (self.pos[0] * self.tileSize + self.tileSize//2 + self.xOffset + self.DisplayXOffset, self.pos[1] * self.tileSize + self.tileSize//2 + self.yOffset + self.DisplayYOffset), self.tileSize//3)
        if (self.gameLevel[self.pos[1]][self.pos[0]] == 1 or self.gameLevel[self.pos[1]][self.pos[0]] == 2):
            self.gameLevel[self.pos[1]][self.pos[0]] = 10
        
        if (self.timer.isDone()):

            if (self.dir == "up"):
                self.CurrentAnim = self.AnimPlayerUp
                if (self.gameLevel[self.pos[1] -1][self.pos[0]] != 0):
                    self.yOffset -= self.movementSpeed
                    if (abs(self.yOffset) >= self.tileSize):
                        self.yOffset = 0
                        self.pos[1] -= 1
                        if (self.nextMove != "none"):
                            self.dir = self.nextMove

            elif (self.dir == "down"):
                self.CurrentAnim = self.AnimPlayerDown
                if (self.gameLevel[self.pos[1] + 1][self.pos[0]] != 0):
                    self.yOffset += self.movementSpeed
                    if (abs(self.yOffset) >= self.tileSize):
                        self.yOffset = 0
                        self.pos[1] += 1
                        if (self.nextMove != "none"):
                            self.dir = self.nextMove

            elif (self.dir == "left"):
                self.CurrentAnim = self.AnimPlayerLeft
                if (self.gameLevel[self.pos[1]][self.pos[0] - 1] != 0):
                    self.xOffset -= self.movementSpeed
                    if (abs(self.xOffset) >= self.tileSize):
                        self.xOffset = 0
                        self.pos[0] -= 1
                        if (self.nextMove != "none"):
                            self.dir = self.nextMove

            elif (self.dir == "right"):
                self.CurrentAnim = self.AnimPlayerRight
                if (self.gameLevel[self.pos[1]][self.pos[0] + 1] != 0):  
                    self.xOffset += self.movementSpeed
                    if (abs(self.xOffset) >= self.tileSize):
                        self.xOffset = 0
                        self.pos[0] += 1
                        if (self.nextMove != "none"):
                            self.dir = self.nextMove
              
            self.timer.start()





        
        
        


