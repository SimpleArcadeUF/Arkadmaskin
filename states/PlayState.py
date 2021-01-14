from states import State

class PlayState(State.State):

    def __init__(self):
        super().__init__()

        self._game = None

    def update(self, screen):
        super().update(screen)

        self._game.update(screen)

    def onShow(self):
        super().onShow()

    def playGame(self, game):
        self._game = game

        game.onPlay()