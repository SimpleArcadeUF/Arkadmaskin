import pygame

from libs.SimpleArcade.gui import Button, Label, Frame
from libs.SimpleArcade import Arcade

from games.Bloons.entity import Monkey, Cannon
from games.Bloons.utils import Assets, Handler
from games.Bloons.guis import PlaceDefenderGUI

class GeneralGUI:

    def __init__(self):
        super().__init__()

        self._width = 192

        self._frame = Frame.Frame(x=Arcade.SCREEN_WIDTH-self._width, y=0, width=self._width, height=Arcade.SCREEN_HEIGHT, bgColor=(206, 170, 130))
        self._frame.addBorder(2, (0,0,0))

        self._lblSelectedName = Label.Label(y=20)
        self._lblSelectedName.addText("Allmänt", Arcade.FONT, (255,255,255), 30)
        self._lblSelectedName.alignHorizontally(self._frame, Arcade.ALIGN_CENTER)

        self._btnStartOver = Button.Button(y=90, width=170, height=65)
        self._btnStartOver.addText("Börja om", Arcade.FONT, (255,255,255), 30)
        self._btnStartOver.addBorder(2, (0,0,0))
        self._btnStartOver.alignHorizontally(self._frame, Arcade.ALIGN_CENTER)

        self._btnExit = Button.Button(y=190, width=170, height=65)
        self._btnExit.addText("Avsluta", Arcade.FONT, (255,255,255), 30)
        self._btnExit.addBorder(2, (0,0,0))
        self._btnExit.alignHorizontally(self._frame, Arcade.ALIGN_CENTER)

        #Button neighbors
        self._btnStartOver.setNeighbors(None, self._btnExit, None, None)
        self._btnExit.setNeighbors(self._btnStartOver, None, None, None)

        self._selectedButton = None

    def update(self, screen):
        self._frame.update(screen)
        self._lblSelectedName.update(screen)
        self._btnStartOver.update(screen)
        self._btnExit.update(screen)

        if(self._btnExit.isClicked()):
            Handler.EXIT = True
        if(self._btnStartOver.isClicked()):
            Handler.RESTART = True

    def show(self):
        Arcade.setSelectedGUI(self._btnStartOver)
        
    def hide(self):
        pass