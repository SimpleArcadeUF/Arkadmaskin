from states import State
from libs.SimpleArcade import Arcade

class PlayState(State.State):

    def __init__(self):
        super().__init__()

        self._game = None

    def update(self, screen):
        super().update(screen)

        self._game.update(screen)

        if(self._game.isQuit()):
            Arcade.setCurrentState(Arcade.gamesState)
            self._game = None
            
    def onShow(self):
        super().onShow()

    def playGame(self, game):
        self._game = game

        game.onPlay()
        game.setQuit(False)