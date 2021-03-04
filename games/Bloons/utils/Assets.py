import pygame

from libs.SimpleArcade import SpriteSheet
from games.Bloons.utils import Handler

balloonSheet = None
map1 = None
monkeySheet = None
dart = None
shopSlots = None

def init():
    global balloonSheet, map1, monkeySheet, dart, shopSlots

    balloonSheet = SpriteSheet.SpriteSheet("games/Bloons/res/images/Balloons.png", 16)
    balloonSheet.scaleImages(Handler.BALLOON_SIZE)

    monkeySheet = SpriteSheet.SpriteSheet("games/Bloons/res/images/Monkey.png", 20)
    monkeySheet.scaleImages(monkeySheet.getImage(0,0).get_width() * Handler.IMAGE_SCALE)
    
    shopSlots = SpriteSheet.SpriteSheet("games/Bloons/res/images/ShopSlots.png", width=40, height=60)
    shopSlots.scaleImages(width=40*Handler.IMAGE_SCALE, height=60*Handler.IMAGE_SCALE)

    dart = loadImage("Dart")

    map1 = loadImage("map")

def loadImage(name):
    image = pygame.image.load("games/Bloons/res/images/"+name+".png")
    return pygame.transform.scale(image, (int(image.get_width()*Handler.IMAGE_SCALE), int(image.get_height()*Handler.IMAGE_SCALE)))