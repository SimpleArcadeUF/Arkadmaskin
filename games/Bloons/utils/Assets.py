import pygame

from libs.SimpleArcade import SpriteSheet
from games.Bloons.utils import Handler

balloonSheet = None
monkeySheet = None
cannonSheet = None
map1 = None
dart = cannonBall = None
shopSlots = None
cannonBallExplosionSpriteSheet = None
menuButtons = None
monkeyUpgrades = None

def init():
    global balloonSheet, map1, monkeySheet, dart, shopSlots, cannonSheet, cannonBall, cannonBallExplosionSpriteSheet, menuButtons, monkeyUpgrades

    balloonSheet = SpriteSheet.SpriteSheet("games/Bloons/res/images/Balloons.png", 16)
    balloonSheet.scaleImages(Handler.BALLOON_SIZE)

    monkeySheet = SpriteSheet.SpriteSheet("games/Bloons/res/images/Monkey.png", 20)
    monkeySheet.scaleImages(monkeySheet.getImage(0,0).get_width() * Handler.IMAGE_SCALE)
    
    cannonSheet = SpriteSheet.SpriteSheet("games/Bloons/res/images/Cannon.png", 42)
    cannonSheet.scaleImages(cannonSheet.getImage(0,0).get_width() * Handler.IMAGE_SCALE)

    shopSlots = SpriteSheet.SpriteSheet("games/Bloons/res/images/ShopSlots.png", width=40, height=60)
    shopSlots.scaleImages(width=40*Handler.IMAGE_SCALE, height=60*Handler.IMAGE_SCALE)

    cannonBallExplosionSpriteSheet = SpriteSheet.SpriteSheet("games/Bloons/res/images/CannonExplosion.png", 30)
    cannonBallExplosionSpriteSheet.scaleImages(width=30*Handler.IMAGE_SCALE, height=30*Handler.IMAGE_SCALE)

    menuButtons = SpriteSheet.SpriteSheet("games/Bloons/res/images/MenuButtons.png", width=50, height=75)
    menuButtons.scaleImages(width=50*Handler.IMAGE_SCALE, height=75*Handler.IMAGE_SCALE)

    monkeyUpgrades = SpriteSheet.SpriteSheet("games/Bloons/res/images/MonkeyUpgrades.png", 27)
    monkeyUpgrades.scaleImages(27*Handler.IMAGE_SCALE)

    dart = loadImage("Dart")
    cannonBall = loadImage("CannonBall")

    map1 = loadImage("map")

def loadImage(name):
    image = pygame.image.load("games/Bloons/res/images/"+name+".png")
    return pygame.transform.scale(image, (int(image.get_width()*Handler.IMAGE_SCALE), int(image.get_height()*Handler.IMAGE_SCALE)))