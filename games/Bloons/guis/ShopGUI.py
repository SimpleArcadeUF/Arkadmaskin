import pygame

from libs.SimpleArcade.gui import Button, Label, Frame
from libs.SimpleArcade import Arcade

from games.Bloons.entity import Monkey, Cannon
from games.Bloons.utils import Assets
from games.Bloons.guis import PlaceDefenderGUI

class ShopGUI:

    def __init__(self):
        super().__init__()

        self._width = 0

        self._boughtDefenderCost = 0
        self._boughtDefender = False

        self._buttons = []
        self._defenders = []

        self.addButton(Monkey.Monkey(0,0,use=False), Assets.shopSlots.getImage(0,0), 170)
        self.addButton(Cannon.Cannon(0,0,use=False), Assets.shopSlots.getImage(1,0), 350)
        self.addButton(Monkey.Monkey(0,0,use=False), Assets.shopSlots.getImage(0,0), 190)
        self.addButton(Monkey.Monkey(0,0,use=False), Assets.shopSlots.getImage(0,0), 200)
        self.addButton(Monkey.Monkey(0,0,use=False), Assets.shopSlots.getImage(0,0), 210)
        self.addButton(Monkey.Monkey(0,0,use=False), Assets.shopSlots.getImage(0,0), 210)

        self._selectedButton = self._buttons[0]

        self._frame = Frame.Frame(x=Arcade.SCREEN_WIDTH-self._width, y=0, width=self._width, height=Arcade.SCREEN_HEIGHT, bgColor=(206, 170, 130))
        self._frame.addBorder(2, (0,0,0))

        self._lblSelectedName = Label.Label(y=20)
        self._lblSelectedName.addText(self._defenders[0].getName(), Arcade.FONT, (255,255,255), 30)
        self._lblSelectedName.alignHorizontally(self._frame, Arcade.ALIGN_CENTER)

    def update(self, screen, money):

        self._frame.update(screen)
        self._lblSelectedName.update(screen)

        for i in range(len(self._buttons)):
            btn = self._buttons[i]
            btn.update(screen)

            if(btn.isHovered()):
                self._lblSelectedName.setText(self._defenders[i].getName())

            if(btn.isClicked() and money >= int(btn.getLabel().getText())):
                PlaceDefenderGUI.DEFENDER = self._defenders[i]
                self._boughtDefender = True
                self._boughtDefenderCost = int(btn.getLabel().getText())
                Arcade.setSelectedGUI(None)

    def addButton(self, defender, image, price):
        width = 80
        height = 120
        spacing = 10
        self._width = (width+spacing)*2 + spacing
        
        btnX = (len(self._buttons)) % 2
        btnY = (len(self._buttons)-btnX) / 2

        btn = Button.Button(bgColor=(255,255,255), x=Arcade.SCREEN_WIDTH-self._width+btnX*(width+spacing)+spacing, y=100+btnY*(height+spacing), width=width, height=height)
        btn.addText(str(price), Arcade.FONT, (0,0,0), 25)
        btn.getLabel().alignVertically(btn, Arcade.ALIGN_BOTTOM)
        btn.addImage(image)
        btn.addBorder(2, (0,0,0))
        
        self._buttons.append(btn)
        self._defenders.append(defender)
    
    def boughtDefender(self):
        return self._boughtDefender
    def getBoughtDefenderCost(self):
        return self._boughtDefenderCost
    def setBoughtDefender(self, tof):
        self._boughtDefender = tof

    def show(self):
        Arcade.setSelectedGUI(self._buttons[0])