from libs.SimpleArcade import Game, Arcade

from libs.SimpleArcade.gui import Label, Button

#from games.GeoDash import GeoPlayer
from games.GeoDash import GeoGame
import pygame


class GeoDash(Game.Game):

    def __init__(self):
        super().__init__("GeoDash", (pygame.image.load("res/images/logo.png")))


    def onPlay(self): #variabler här asså
        self.Label = Label.Label(x=10,y=100)
        self.Label.alignHorizontally(None, Arcade.ALIGN_CENTER)
        self.Label.addText("hej", Arcade.FONT, "white", 100)

    def update(self, screen): #While true loopen 
        self.Label.update(screen)