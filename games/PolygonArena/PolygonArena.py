from libs.SimpleArcade import Game, Arcade
from libs.SimpleArcade.gui import Label, Button, Frame
from games.PolygonArena.states import GameState, MenuState
from games.PolygonArena.utils import Handler


import random, time, sqlite3, math
import pygame, pygame.freetype 
from pygame.math import Vector2



class PolygyonArena(Game.Game):

    def __init__(self):

        super().__init__("Polygonz", (pygame.image.load("res/images/logo.png")))


    def onPlay(self): #variabler här asså'

        Handler.MenuState = MenuState.MenuState()
        Handler.GameState = GameState.GameState()

        #Starting frame
        Handler.currentState = Handler.MenuState


    def update(self, screen): #While true loopen 
        
        Handler.currentState.update(screen)
        
        if Handler.quit == True:
            self.quit()
            Handler.quit = False