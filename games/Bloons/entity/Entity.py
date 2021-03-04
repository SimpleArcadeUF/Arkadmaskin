import pygame

class Entity():

    def __init__(self, x, y, size, draw=False, color=(20,20,20)):
        self._x = x
        self._y = y
        self._size = size
        self._draw = draw
        self._color = color
    
    def update(self, screen):
        if(self._draw == True):
            pygame.draw.circle(screen, self._color, (self._x, self._y), self._size)

    def setDraw(self, tof):
        self._draw = tof

    def getX(self):
        return self._x
    def getY(self):
        return self._y
    def getSize(self):
        return self._size