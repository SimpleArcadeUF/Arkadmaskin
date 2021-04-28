class Game:

    def __init__(self, title, logo):
        super().__init__()

        self._title = title
        self._logo = logo
        self._quit = False

    def onPlay(self):
        pass

    def update(self, screen):
        pass
    def quit(self):
        self._quit = True
    def getTitle(self):
        return self._title
    def getLogo(self):
        return self._logo
    def isQuit(self):
        return self._quit
    def setQuit(self, tof):
        self._quit = tof
"""
import pygame
from libs.SimpleArcade import Game

class Pong(Game.Game):

    def __init__(self):
        super().__init__("Pong", (pygame.image.load("res/images/logo.png")))

    def onPlay(self):
        pass

    def update(self, screen):
        pass
"""