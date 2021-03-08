import pygame

from libs.SimpleArcade import Arcade

from games.Bloons.utils import Handler

DEFENDER = None

class PlaceDefenderGUI:

    def __init__(self):
        self._defender = None
        self._baseSpeed = 0.5
        self._xSpeed = self._baseSpeed
        self._ySpeed = self._baseSpeed
        self._maxSpeed = 7
        self._accSpeed = 0.1

        self._upPressed = False
        self._downPressed = False
        self._leftPressed = False
        self._rightPressed = False
    
    def update(self, screen):
        global DEFENDER

        if(self._defender == None and DEFENDER != None):
            self._defender = DEFENDER.create(Arcade.SCREEN_WIDTH/2, Arcade.SCREEN_HEIGHT/2)
            DEFENDER = None
        
        if(self._defender == None): return

        self._defender.update(screen)
        keys = pygame.key.get_pressed()

        #--------UP---------
        if(keys[pygame.K_UP] or Arcade._JOYSTICK_UP):
            self._upPressed = True
            if(self._ySpeed < self._maxSpeed):
                self._ySpeed += self._accSpeed * Handler.GAME_SPEED
            self._defender.setY(self._defender.getY()-self._ySpeed)
        else:
            if(self._upPressed == True):
                self._upPressed = False
                self._ySpeed = self._baseSpeed

        #--------DOWN--------
        if(keys[pygame.K_DOWN] or Arcade._JOYSTICK_DOWN):
            self._downPressed = True
            if(self._ySpeed < self._maxSpeed):
                self._ySpeed += self._accSpeed * Handler.GAME_SPEED
            self._defender.setY(self._defender.getY()+self._ySpeed)
        else:
            if(self._downPressed == True):
                self._downPressed = False
                self._ySpeed = self._baseSpeed

        #--------LEFT--------
        if(keys[pygame.K_LEFT] or Arcade._JOYSTICK_LEFT):
            self._leftPressed = True
            if(self._xSpeed < self._maxSpeed):
                self._xSpeed += self._accSpeed * Handler.GAME_SPEED
            self._defender.setX(self._defender.getX()-self._xSpeed)
        else:
            if(self._leftPressed == True):
                self._leftPressed = False
                self._xSpeed = self._baseSpeed

        #--------RIGHT--------
        if(keys[pygame.K_RIGHT] or Arcade._JOYSTICK_RIGHT):
            self._rightPressed = True
            if(self._xSpeed < self._maxSpeed):
                self._xSpeed += self._accSpeed * Handler.GAME_SPEED
            self._defender.setX(self._defender.getX()+self._xSpeed)
        else:
            if(self._rightPressed == True):
                self._rightPressed = False
                self._xSpeed = self._baseSpeed
    
    def updatePlace(self, screen, defenders):
        global DEFENDER
        if(self._defender == None): return

        keys = pygame.key.get_pressed()

        if(keys[pygame.K_RETURN]):
            defenders.append(self._defender)
            self._defender = None
            DEFENDER = None