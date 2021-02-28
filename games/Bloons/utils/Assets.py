import pygame

from games.Bloons.utils import Handler

def init():
    pass

def loadImage(name):
    image = pygame.image.load("games/Escape/res/images/"+name+".png")
    return pygame.transform.scale(image, (int(image.get_width()*Handler.IMAGE_SCALE), int(image.get_height()*Handler.IMAGE_SCALE)))