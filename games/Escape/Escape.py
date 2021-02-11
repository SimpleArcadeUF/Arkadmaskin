import pygame

from libs.SimpleArcade import Game, Arcade

from games.Escape.utils import Handler, Assets
from games.Escape.states import SelectSaveState, GameState
from games.Escape.objects import TileType

class Escape(Game.Game):
    """Spela som en robot och överlev samt leta upp delar för att reparera raketen som man krashade på planeten med."""

    def __init__(self):
        super().__init__("Escape", (pygame.image.load("games/Escape/res/images/Logo.png")))

    def onPlay(self):
        Assets.init()
        TileType.init()

        #Init states
        Handler.selectSaveState = SelectSaveState.SelectSaveState()
        Handler.gameState = GameState.GameState()
        
        Handler.setCurrentState(Handler.selectSaveState)

    def update(self, screen):
        Handler.currentState.update(screen)