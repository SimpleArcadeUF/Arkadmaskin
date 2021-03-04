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
    
    def update(self, screen):
        global DEFENDER

        if(self._defender == None and DEFENDER != None):
            self._defender = DEFENDER.create(Arcade.SCREEN_WIDTH/2, Arcade.SCREEN_HEIGHT/2)
            print("cretae")
            DEFENDER = None
        
        if(self._defender == None): return

        self._defender.update(screen)
        keys = pygame.key.get_pressed()

        if(keys[pygame.K_UP] or Arcade._JOYSTICK_UP):
            if(self._ySpeed < self._maxSpeed):
                self._ySpeed += self._accSpeed * Handler.GAME_SPEED
            self._defender.setY(self._defender.getY()-self._ySpeed)
        elif(keys[pygame.K_DOWN] or Arcade._JOYSTICK_DOWN):
            if(self._ySpeed < self._maxSpeed):
                self._ySpeed += self._accSpeed * Handler.GAME_SPEED
            self._defender.setY(self._defender.getY()+self._ySpeed)
        else:
            self._ySpeed = self._baseSpeed

        if(keys[pygame.K_LEFT] or Arcade._JOYSTICK_LEFT):
            if(self._xSpeed < self._maxSpeed):
                self._xSpeed += self._accSpeed * Handler.GAME_SPEED
            self._defender.setX(self._defender.getX()-self._xSpeed)

        elif(keys[pygame.K_RIGHT] or Arcade._JOYSTICK_RIGHT):
            if(self._xSpeed < self._maxSpeed):
                self._xSpeed += self._accSpeed * Handler.GAME_SPEED
            self._defender.setX(self._defender.getX()+self._xSpeed)
        else:
            self._xSpeed = self._baseSpeed
    
    def updatePlace(self, screen, defenders):
        global DEFENDER
        if(self._defender == None): return

        keys = pygame.key.get_pressed()

        if(keys[pygame.K_SPACE]):
            defenders.append(self._defender)
            print("he")
            self._defender = None
            DEFENDER = None