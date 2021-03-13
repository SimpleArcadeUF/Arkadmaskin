import pygame

from libs.SimpleArcade.gui import Button, Label, Frame
from libs.SimpleArcade import Arcade

from games.Bloons.entity import Monkey, Cannon
from games.Bloons.utils import Assets, Handler
from games.Bloons.guis import PlaceDefenderGUI, SelectDefenderGUI

class DefendersGUI:

    def __init__(self):
        super().__init__()

        self._width = 192

        self._frame = Frame.Frame(x=Arcade.SCREEN_WIDTH-self._width, y=0, width=self._width, height=Arcade.SCREEN_HEIGHT, bgColor=(206, 170, 130))
        self._frame.addBorder(2, (0,0,0))

        self._lblTitle = Label.Label(y=20)
        self._lblTitle.addText("Försvarare", Arcade.FONT, (255,255,255), 27)
        self._lblTitle.alignHorizontally(self._frame, Arcade.ALIGN_CENTER)

        self._lblNoDefender = Label.Label(y=80)
        self._lblNoDefender.addText("Du har inga", Arcade.FONT, (255,255,255), 24)
        self._lblNoDefender.alignHorizontally(self._frame, Arcade.ALIGN_CENTER)
        self._lblNoDefender2 = Label.Label(y=110)
        self._lblNoDefender2.addText("försvarare!", Arcade.FONT, (255,255,255), 24)
        self._lblNoDefender2.alignHorizontally(self._frame, Arcade.ALIGN_CENTER)

        self._btnSelect = Button.Button(y=80, width=150, height=50)
        self._btnSelect.addText("Välj", Arcade.FONT, (255,255,255), 30)
        self._btnSelect.alignHorizontally(self._frame, Arcade.ALIGN_CENTER)
        self._btnSelect.addBorder(2, (0,0,0))

        self._btnMove = Button.Button(y=150, width=150, height=50)
        self._btnMove.addText("Flytta", Arcade.FONT, (255,255,255), 30)
        self._btnMove.alignHorizontally(self._frame, Arcade.ALIGN_CENTER)
        self._btnMove.addBorder(2, (0,0,0))

        self._lblUpgrades = Label.Label(y=225)
        self._lblUpgrades.addText("Uppgraderingar", Arcade.FONT, (255,255,255), 20)
        self._lblUpgrades.alignHorizontally(self._frame, Arcade.ALIGN_CENTER)

        self._btnSelect.setNeighbors(None, self._btnMove, None, None)
        self._btnMove.setNeighbors(self._btnSelect, None, None, None)

        self._selectedDefender = None

    def update(self, screen):
        self._frame.update(screen)
        self._lblTitle.update(screen)
        self._lblNoDefender.update(screen)
        self._lblNoDefender2.update(screen)

        if(self._selectedDefender == None): return

        self._btnSelect.update(screen)
        self._btnMove.update(screen)
        self._lblUpgrades.update(screen)

        if(self._btnMove.isClicked(True)):
            PlaceDefenderGUI.DEFENDER = self._selectedDefender
            Arcade.setSelectedGUI(None)
        
        if(self._btnSelect.isClicked(True)):
            SelectDefenderGUI.SELECT = True
            Arcade.setSelectedGUI(None)

    def setSelectedDefender(self, defender):
        if(self._selectedDefender != None):
            self._selectedDefender.setSelected(False)

        self._selectedDefender = defender
        self._selectedDefender.setSelected(True)

    def show(self, defenders):
        if(len(defenders) > 0):
            self.setSelectedDefender(defenders[0])
            self._lblNoDefender.show(False)
            self._lblNoDefender2.show(False)

            Arcade.setSelectedGUI(self._btnSelect)
        else:
            self._lblNoDefender.show(True)
            self._lblNoDefender2.show(True)
    
    def hide(self):
        if(self._selectedDefender != None):
            self._selectedDefender.setSelected(False)
