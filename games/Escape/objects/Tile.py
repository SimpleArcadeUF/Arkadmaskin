import pygame

from games.Escape.objects import GameObject
from games.Escape.utils import Handler

class Tile(GameObject.GameObject):

    def __init__(self, order, tileType, tileX, tileY):
        super().__init__(GameObject.TAG_TILE, order, Handler.TILE_SIZE, Handler.TILE_SIZE)

        self._tileType = tileType
        self._tileX = tileX
        self._tileY = tileY
        self._static = True

    def update(self, screen):
        super().update(screen)

        self._x = self._tileX * Handler.TILE_SIZE
        self._y = self._tileY * Handler.TILE_SIZE

        if(self._onScreen):
            screen.blit(self._tileType.getImage(), (self._x - Handler.gameCamera.getXOffset(), self._y - Handler.gameCamera.getYOffset()))

    def show(self, tof):
        super().show(tof)

    def getTileType(self):
        return self._tileType