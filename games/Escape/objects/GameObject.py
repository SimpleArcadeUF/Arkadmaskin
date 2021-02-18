import math, bisect 

from libs.SimpleArcade import Arcade

from games.Escape.utils import Handler

GAME_OBJECTS = []
TAG_TILE = 0
TAG_CREATURE = 1

""" ORDER
-10 - Air
-2 - Behind tiles
-1 - Rocket etc
 0 - Player
 1 - ...
 2 - Infront tiles
"""

class GameObject():

    def __init__(self, objTag, order, width, height):
        self._objTag = objTag
        self._order = order
        self._width = width
        self._height = height

        self._x = 0
        self._y = 0
        self._show = True
        self._onScreen = True

        #Physics
        self._xVel = 0
        self._yVel = 0
        self._static = False
        self._gravity = 0.2
        self._grounded = False
        self._collisionBox = [0, 0, width, height]

        bisect.insort_left(GAME_OBJECTS, self)

    def __lt__(self, other):
        return self._order < other.getOrder()

    def update(self, screen):
        self._onScreen = False

        if(self._x + self._width - Handler.gameCamera.getXOffset() > 0 and self._x - Handler.gameCamera.getXOffset() < Arcade.SCREEN_WIDTH):
            if(self._y + self._height - Handler.gameCamera.getYOffset() > 0 and self._y - Handler.gameCamera.getYOffset() < Arcade.SCREEN_HEIGHT):
                self._onScreen = True

        if(self._onScreen):
            self._updatePhysics()

    def _updatePhysics(self):
        if(self._static == True): return

        if(self._xVel != 0):
            self._grounded = False

        if(self._grounded == False):
            self._yVel += self._gravity


        self._collision()

        self._x += self._xVel
        self._y += self._yVel

        self._xVel = 0
    
    def _collision(self):
        pass

    def show(self, tof):
        self._show = tof
    def getOrder(self):
        return self._order
    def getObjTag(self):
        return self._objTag
    def getCollisionBox(self):
        return self._collisionBox
    def isOnScreen(self):
        return self._onScreen
    def getX(self):
        return self._x
    def getY(self):
        return self._y
    def getWidth(self):
        return self._width
    def getHeight(self):
        return self._height