from libs.SimpleArcade.gui import Button, Label
from libs.SimpleArcade import Arcade

from games.Escape.states import State
from games.Escape.utils import Handler

class SelectSaveState(State.State):

    def __init__(self):
        super().__init__()

        self._btnSave1 = Button.Button(width=200, height=200)
        self._btnSave1.alignHorizontally(None, Arcade.ALIGN_CENTER)
        self._btnSave1.alignVertically(None, Arcade.ALIGN_CENTER)
        self._btnSave1.addText("Save 1", Arcade.FONT, Arcade.GUI_COLOR_BLUE, 70)

        self._lblTitle = Label.Label(y=20)
        self._lblTitle.addText("Escape", Arcade.FONT, (255,255,255), 90)
        self._lblTitle.alignHorizontally(None, Arcade.ALIGN_CENTER)

    def update(self, screen):
        super().update(screen)

        screen.fill((25,20,20))

        self._btnSave1.update(screen)
        self._lblTitle.update(screen)

        if(self._btnSave1.isClicked(stopClick=True)):
            Handler.setCurrentState(Handler.gameState)

    def show(self, tof):
        super().show(tof)

        self._btnSave1.show(tof)
        self._lblTitle.show(tof)

        Arcade.setSelectedGUI(self._btnSave1)