import pygame, math

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
        self._placed = False
        self._placeNewDefender = False
        self._startX = 0
        self._startY = 0
        self._cancel = False

        self._upPressed = False
        self._downPressed = False
        self._leftPressed = False
        self._rightPressed = False
    
    def update(self, screen):
        global DEFENDER

        if(self._defender == None and DEFENDER != None):
            if(DEFENDER.isUse() == False):
                self._defender = DEFENDER.create(Arcade.SCREEN_WIDTH/2, Arcade.SCREEN_HEIGHT/2)
                self._placeNewDefender = True
            else:
                self._placeNewDefender = False
                self._defender = DEFENDER
                self._defender.setCanAttack(False)
                self._defender.setSelected(False)
                self._startX = self._defender.getX()
                self._startY = self._defender.getY()
            self._defender.showAttackRange(True)
            DEFENDER = None
        
        if(self._defender == None): return

        if(self._placeNewDefender):
            self._defender.update(screen, None)
            
        keys = pygame.key.get_pressed()

        #--------UP---------
        if(Arcade._JOYSTICK_UP):
            self._upPressed = True
            if(self._ySpeed < self._maxSpeed):
                self._ySpeed += self._accSpeed * Handler.GAME_SPEED
            self._defender.setY(self._defender.getY()-self._ySpeed)
        else:
            if(self._upPressed == True):
                self._upPressed = False
                self._ySpeed = self._baseSpeed

        #--------DOWN--------
        if(Arcade._JOYSTICK_DOWN):
            self._downPressed = True
            if(self._ySpeed < self._maxSpeed):
                self._ySpeed += self._accSpeed * Handler.GAME_SPEED
            self._defender.setY(self._defender.getY()+self._ySpeed)
        else:
            if(self._downPressed == True):
                self._downPressed = False
                self._ySpeed = self._baseSpeed

        #--------LEFT--------
        if(Arcade._JOYSTICK_LEFT):
            self._leftPressed = True
            if(self._xSpeed < self._maxSpeed):
                self._xSpeed += self._accSpeed * Handler.GAME_SPEED
            self._defender.setX(self._defender.getX()-self._xSpeed)
        else:
            if(self._leftPressed == True):
                self._leftPressed = False
                self._xSpeed = self._baseSpeed

        #--------RIGHT--------
        if(Arcade._JOYSTICK_RIGHT):
            self._rightPressed = True
            if(self._xSpeed < self._maxSpeed):
                self._xSpeed += self._accSpeed * Handler.GAME_SPEED
            self._defender.setX(self._defender.getX()+self._xSpeed)
        else:
            if(self._rightPressed == True):
                self._rightPressed = False
                self._xSpeed = self._baseSpeed
    
    def updatePlace(self, defenders):
        global DEFENDER
        if(self._defender == None): return

        canPlace = True

        for d in defenders:
            if(d == self._defender): continue
            
            dist = Arcade.getDistance((self._defender.getX()+self._defender.getSize()/2, self._defender.getY()+self._defender.getSize()/2), (d.getX()+d.getSize()/2, d.getY()+d.getSize()/2))

            if(dist < self._defender.getSize()/2 + d.getSize()/2):
                canPlace = False

        #[TODO] Check for roads

        keys = pygame.key.get_pressed()

        if(Arcade.BUTTON_PRESSED_1 and canPlace):
            Arcade.BUTTON_PRESSED_1 = False
            if(self._placeNewDefender == True):
                defenders.append(self._defender)
            else:
                self._defender.setSelected(True)
            self._defender.setCanAttack(True)
            self._defender.showAttackRange(False)
            self._defender = None
            DEFENDER = None
            self._placed = True
        
        if(Arcade.BUTTON_PRESSED_2 or Arcade.BUTTON_PRESSED_3 or Arcade.BUTTON_PRESSED_4):
            if(self._placeNewDefender == False):
                self._defender.showAttackRange(False)
                self._defender.setCanAttack(True)
                self._defender.setSelected(True)
                self._defender.setX(self._startX)
                self._defender.setY(self._startY)
            
            self._defender = None
            DEFENDER = None
            self._cancel = True

    def onPlace(self):
        return self._placed
    def onCancel(self):
        return self._cancel
    
    def reset(self):
        self._placed = False
        self._cancel = False