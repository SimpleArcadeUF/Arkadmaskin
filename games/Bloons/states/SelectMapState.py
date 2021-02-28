from libs.SimpleArcade.gui import Button, Label
from libs.SimpleArcade import Arcade

from games.Bloons.states import State
from games.Bloons.utils import Handler
from games.Bloons.map import Maps

class SelectMapState(State.State):

    def __init__(self):
        super().__init__()

        self._btnMap1 = Button.Button(width=250, height=200)
        self._btnMap1.alignHorizontally(None, Arcade.ALIGN_CENTER)
        self._btnMap1.alignVertically(None, Arcade.ALIGN_CENTER)
        self._btnMap1.addText("Vanilla", Arcade.FONT, Arcade.GUI_COLOR_BLUE, 60)

        self._lblTitle = Label.Label(y=20)
        self._lblTitle.addText("Bloons", Arcade.FONT, (255,255,255), 90)
        self._lblTitle.alignHorizontally(None, Arcade.ALIGN_CENTER)

    def update(self, screen):
        super().update(screen)

        screen.fill((25,20,20))

        self._btnMap1.update(screen)
        self._lblTitle.update(screen)

        if(self._btnMap1.isClicked(stopClick=True)):
            Handler.setCurrentState(Handler.gameState)
            Handler.currentMap = Maps.MAPS[0]
            Handler.gameState.startWave()

    def show(self, tof):
        super().show(tof)

        self._btnMap1.show(tof)
        self._lblTitle.show(tof)

        Arcade.setSelectedGUI(self._btnMap1)