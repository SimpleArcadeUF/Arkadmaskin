import pygame
from games.Titanic import Handler
from libs.SimpleArcade import SpriteSheet

water = None
iceSheet = None
boat = None
wavesSheet = None

def init():
    global water, iceSheet, boat, wavesSheet

    water = pygame.image.load("games/Titanic/res/Water.png")
    water = pygame.transform.scale(water, (water.get_width()*Handler.SCALE, water.get_height()*Handler.SCALE))

    boat = pygame.image.load("games/Titanic/res/Boat.png")
    boat = pygame.transform.scale(boat, (boat.get_width()*Handler.SCALE, boat.get_height()*Handler.SCALE))

    iceSheet = SpriteSheet.SpriteSheet("games/Titanic/res/IceSheet.png", 70)
    iceSheet.scaleImages(70*4)

    wavesSheet = SpriteSheet.SpriteSheet("games/Titanic/res/BoatWaves.png", width=26, height=14)
    wavesSheet.scaleImages(width=26*Handler.SCALE, height=14*Handler.SCALE)
