from games.Bloons.states import State
from games.Bloons.utils import Handler

class GameState(State.State):

    def __init__(self):
        super().__init__()

    def update(self, screen):
        super().update(screen)

        screen.fill((40, 60, 255))

    def show(self, tof):
        super().show(tof)