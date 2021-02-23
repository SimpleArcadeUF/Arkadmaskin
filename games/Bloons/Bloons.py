import pygame
from libs.SimpleArcade import Game, Arcade

from games.Bloons.utils import Handler, Assets
from games.Bloons.states import SelectSaveState, GameState

class Bloons(Game.Game):

    def __init__(self):
        super().__init__("Bloons", (pygame.image.load("res/images/logo.png")))

    def onPlay(self):
        Assets.init()

        #Init states
        Handler.selectSaveState = SelectSaveState.SelectSaveState()
        Handler.gameState = GameState.GameState()
        
        Handler.setCurrentState(Handler.selectSaveState)


    def update(self, screen):
        Handler.currentState.update(screen)