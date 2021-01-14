import pygame
from libs.SimpleArcade import Game

class Minecraft(Game.Game):

    def __init__(self):
        super().__init__("Minecraft", (pygame.image.load("res/images/logo.png")))

    def onPlay(self):
        pass

    def update(self, screen):
        pass