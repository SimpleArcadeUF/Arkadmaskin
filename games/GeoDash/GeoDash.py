from libs.SimpleArcade import Game, Arcade
from libs.SimpleArcade.gui import Label, Button, Frame
from games.GeoDash import GameState, LevelState, MenuState, Handler


import pygame


class GeoDash(Game.Game):

    def __init__(self):

        super().__init__("GeoRush", (pygame.image.load("res/images/logo.png")))


    def onPlay(self): #variabler här asså'

        Handler.MenuState = MenuState.MenuState()
        Handler.LevelState = LevelState.LevelState()

        #Starting frame
        Handler.currentState = Handler.MenuState


    def update(self, screen): #While true loopen 
        
        Handler.currentState.update(screen)
        
        if Handler.quit == True:
            self.quit()