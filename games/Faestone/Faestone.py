from libs.SimpleArcade import Game
import pygame

class Faestone(Game.Game):

    def __init__(self):
        super().__init__("Faestone", (pygame.image.load("res/images/logo.png")))

    def onPlay(self):
        pass #när spel klickas

    def update(self, screen):
        pass #