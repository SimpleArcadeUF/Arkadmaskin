import pygame

from games.Bloons.entity import Balloons

class Map():

    def __init__(self, name, path):
        self._name = name
        self._path = path
        self._showPath = False

    def update(self, screen):
        for i in range(len(self._path)):
            node = self._path[i]
            if(i < len(self._path)-1):
                nextNode = self._path[i+1]
                pygame.draw.line(screen, (100,130,150), (node.getX(), node.getY()), (nextNode.getX(), nextNode.getY()), 50)
            node.update(screen)

    def showPath(self, tof):
        self._showPath = tof
        for node in self._path:
            node.setDraw(tof)
        
    def getPath(self):
        return self._path
