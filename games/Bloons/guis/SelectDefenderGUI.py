import pygame, math

from libs.SimpleArcade import Arcade

from games.Bloons.utils import Handler

SELECT = False

class SelectDefenderGUI:

    def __init__(self):
        self._defender = None
        self._baseSpeed = 0.5
        self._xSpeed = self._baseSpeed
        self._ySpeed = self._baseSpeed
        self._maxSpeed = 7
        self._accSpeed = 0.1
        self._cursorX = Arcade.SCREEN_WIDTH/2
        self._cursorY = Arcade.SCREEN_HEIGHT/2
        self._cursorSize = 10
        self._selected = False
        self._cancel = False

        self._upPressed = False
        self._downPressed = False
        self._leftPressed = False
        self._rightPressed = False
    
    def update(self, screen):
        if(SELECT == False): return

        keys = pygame.key.get_pressed()

        #--------UP---------
        if(Arcade._JOYSTICK_UP):
            self._upPressed = True
            if(self._ySpeed < self._maxSpeed):
                self._ySpeed += self._accSpeed * Handler.GAME_SPEED
            self._cursorY -= self._ySpeed
        else:
            if(self._upPressed == True):
                self._upPressed = False
                self._ySpeed = self._baseSpeed

        #--------DOWN--------
        if(Arcade._JOYSTICK_DOWN):
            self._downPressed = True
            if(self._ySpeed < self._maxSpeed):
                self._ySpeed += self._accSpeed * Handler.GAME_SPEED
            self._cursorY += self._ySpeed
        else:
            if(self._downPressed == True):
                self._downPressed = False
                self._ySpeed = self._baseSpeed

        #--------LEFT--------
        if(Arcade._JOYSTICK_LEFT):
            self._leftPressed = True
            if(self._xSpeed < self._maxSpeed):
                self._xSpeed += self._accSpeed * Handler.GAME_SPEED
            self._cursorX -= self._xSpeed
        else:
            if(self._leftPressed == True):
                self._leftPressed = False
                self._xSpeed = self._baseSpeed

        #--------RIGHT--------
        if(Arcade._JOYSTICK_RIGHT):
            self._rightPressed = True
            if(self._xSpeed < self._maxSpeed):
                self._xSpeed += self._accSpeed * Handler.GAME_SPEED
            self._cursorX += self._xSpeed
        else:
            if(self._rightPressed == True):
                self._rightPressed = False
                self._xSpeed = self._baseSpeed

        pygame.draw.rect(screen, (20,20,20), (self._cursorX-self._cursorSize/2, self._cursorY-self._cursorSize/2, self._cursorSize, self._cursorSize))
    
    def updateSelect(self, defenders):
        global SELECT
        if(SELECT == False): return

        keys = pygame.key.get_pressed()

        if(Arcade.BUTTON_PRESSED_1):
            Arcade.BUTTON_PRESSED_1 = False

            minDist = 0
            closestDefender = None

            for defender in defenders:
                dist = math.dist((defender.getX()+defender.getSize()/2, defender.getY()+defender.getSize()/2), (self._cursorX+self._cursorSize/2, self._cursorY+self._cursorSize/2))
                if(dist < minDist or closestDefender == None):
                    minDist = dist
                    closestDefender = defender

            self._defender = closestDefender
            self._selected = True
            SELECT = False

        if(Arcade.BUTTON_PRESSED_2 or Arcade.BUTTON_PRESSED_3 or Arcade.BUTTON_PRESSED_4):
            SELECT = False
            self._cancel = True

    def onSelect(self):
        return self._selected
    def onCancel(self):
        return self._cancel
    def getSelectedDefender(self):
        return self._defender
    def resetSelect(self):
        self._selected = False
        self._defender = None
        self._cancel = False
    