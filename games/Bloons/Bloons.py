import pygame
from libs.SimpleArcade import Game, Arcade

from games.Bloons.utils import Handler, Assets
from games.Bloons.states import SelectMapState, GameState
from games.Bloons.map import Maps
from games.Bloons.entity import Balloons

class Bloons(Game.Game):

    def __init__(self):
        super().__init__("Bloons", (pygame.image.load("res/images/logo.png")))

    def onPlay(self):
        Handler.init()
        Assets.init()

        Balloons.init()
        Balloons.initWaves()
        Maps.init()

        #Init states
        Handler.selectMapState = SelectMapState.SelectMapState()
        Handler.gameState = GameState.GameState()
        
        Handler.setCurrentState(Handler.selectMapState)

    def update(self, screen):
        Handler.currentState.update(screen)

        if(Handler.EXIT):
            self.quit()
        elif(Handler.RESTART):
            self.onPlay()
            Handler.setCurrentState(Handler.gameState)
            Handler.currentMap = Maps.MAPS[0]
            Handler.gameState.startWave()