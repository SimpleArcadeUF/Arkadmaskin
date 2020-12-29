import os

from states import State
from libs.SimpleArcade.gui import Label
from libs.SimpleArcade import Arcade

class GamesState(State.State):

    def __init__(self):
        super().__init__()

        self._lblTitle = Label.Label(y=20)
        self._lblTitle.addText("SPEL", "roboto", Arcade.GUI_COLOR_BLUE, 80)
        self._lblTitle.addUnderline(2, Arcade.GUI_COLOR_BLUE)
        self._lblTitle.alignHorizontally(None, Arcade.ALIGN_CENTER)

    def update(self, screen):
        super().update(screen)

        self._lblTitle.update(screen)
        