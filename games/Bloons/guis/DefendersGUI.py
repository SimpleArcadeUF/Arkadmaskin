import pygame

from libs.SimpleArcade.gui import Button, Label, Frame
from libs.SimpleArcade import Arcade

from games.Bloons.entity import Monkey, Cannon
from games.Bloons.utils import Assets, Handler
from games.Bloons.guis import PlaceDefenderGUI

class DefendersGUI:

    def __init__(self):
        super().__init__()

        self._width = 192

        self._frame = Frame.Frame(x=Arcade.SCREEN_WIDTH-self._width, y=0, width=self._width, height=Arcade.SCREEN_HEIGHT, bgColor=(206, 170, 130))
        self._frame.addBorder(2, (0,0,0))

        self._lblSelectedName = Label.Label(y=20)
        self._lblSelectedName.addText("Försvarare", Arcade.FONT, (255,255,255), 27)
        self._lblSelectedName.alignHorizontally(self._frame, Arcade.ALIGN_CENTER)

        self._selectedButton = None

    def update(self, screen):
        self._frame.update(screen)
        self._lblSelectedName.update(screen)

    def show(self):
        pass