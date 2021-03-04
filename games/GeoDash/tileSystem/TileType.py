import pygame

TILE_TYPES = []
air = brick = None

def init():
    global air, brick

    air = TileType(0, loadImage("air_sprite"), False, -10)
    brick = TileType(1, loadImage("ground_sprite"), True, -2)

def getTileTypeByID(ID):
    for tileType in TILE_TYPES:
        if(tileType.id == ID):
            return tileType


def loadImage(name):
    image = pygame.image.load("games/GeoDash/images/"+name+".png")
    image = pygame.transform.scale(image, (64,64))
    return image


class TileType:

    def __init__(self, ID, image, solid, order):
        self.id = ID
        self.image = image
        self.solid = solid
        self.order = order

        TILE_TYPES.append(self)