import pygame

from games.Escape.utils import SpriteSheet, Handler

tileSheet = None
playerSheet = None
rocket = None
rocketBroken = None

def init():
    global tileSheet, playerSheet, rocket, rocketBroken

    tileSheet = SpriteSheet.SpriteSheet("games/Escape/res/images/TileSheet.png", 16)
    tileSheet.scaleImages(Handler.TILE_SIZE)

    playerSheet = SpriteSheet.SpriteSheet("games/Escape/res/images/PlayerSheet.png", 24)
    playerSheet.scaleImages(Handler.IMAGE_SCALE*24)
    rocket = loadImage("Rocket")
    rocketBroken = loadImage("BrokenRocket")

def loadImage(name):
    image = pygame.image.load("games/Escape/res/images/"+name+".png")
    return pygame.transform.scale(image, (int(image.get_width()*Handler.IMAGE_SCALE), int(image.get_height()*Handler.IMAGE_SCALE)))