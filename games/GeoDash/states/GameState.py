from games.GeoDash.states import State 
from games.GeoDash.utils import Handler
from games.GeoDash.tileSystem import TileType
from libs.SimpleArcade.gui import Label, Button, Frame
from libs.SimpleArcade import Game, Arcade

import pygame

class GameState():

    def __init__(self):

        TileType.init()
        self.mapWidth = 76
        self.mapHeight = 10

        self.tiles = [] 
        self.loadMap("games/GeoDash/res/maps/level1")

    def update(self, screen):
        for tile in self.tiles:
            tile.update(screen)
    
    def loadMap(self, path):
        f = open(path + '.txt','r')
        data = f.read()
        f.close()
        data = data.split('\n')
        for y in range(self.mapHeight):
            for x in range(self.mapWidth):
                ID = int(data[y][x])
                self.tiles.append(Tile(TileType.getTileTypeByID(ID), x, y))



class Tile: 

    def __init__(self, tileType, x, y):
        self.tileType = tileType
        self.x = x
        self.y = y
        self.size = 64
        

    def update(self, screen):
        screen.blit(self.tileType.image, (self.x * self.size, self.y * self.size))


