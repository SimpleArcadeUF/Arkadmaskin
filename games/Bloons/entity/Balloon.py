import pygame

from games.Bloons.entity import Entity
from games.Bloons.utils import Handler

class Balloon(Entity.Entity):

    def __init__(self, x, y, speed, color, balloon, rbe, template=False):
        super().__init__(x, y, 15, draw=False, color=color)

        self._speed = speed
        self._template = template
        self._type = balloon
        self._rbe = rbe
        self._currentNodeIndex = 1

    def update(self, screen):
        if(self._template == True):
            return

        super().update(screen)

        pygame.draw.circle(screen, self._color, (self._x, self._y), self._size)

    def move(self, path):
        node = path[self._currentNodeIndex]

        dx = self._x - node.getX()
        dy = self._y - node.getY()            

        if(dx < 0):
            self._x += self._speed * Handler.GAME_SPEED
        if(dx > 0):
            self._x -= self._speed * Handler.GAME_SPEED
        if(dy < 0):
            self._y += self._speed * Handler.GAME_SPEED
        if(dy > 0):
            self._y -= self._speed * Handler.GAME_SPEED
        
        if(abs(dx) <= self._speed * Handler.GAME_SPEED and abs(dy) <= self._speed * Handler.GAME_SPEED):
            self._x = node.getX()
            self._y = node.getY()
            self._currentNodeIndex += 1

    def getCurrentNodeIndex(self):
        return self._currentNodeIndex
    def getRBE(self):
        return self._rbe
    def setColor(self, color):
        self._color = color

    def create(self, x, y):
        return Balloon(x,y, self._speed, self._color, self._type, self._rbe)