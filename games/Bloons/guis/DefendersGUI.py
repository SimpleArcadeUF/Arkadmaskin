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

        self._upgradeButtons = []

        btn1 = UpgradeButton(y=280)
        btn1.alignHorizontally(self._frame, Arcade.ALIGN_CENTER)
        self._upgradeButtons.append(btn1)

        btn2 = UpgradeButton(y=370)
        btn2.alignHorizontally(self._frame, Arcade.ALIGN_CENTER)
        self._upgradeButtons.append(btn2)

        btn3 = UpgradeButton(y=460)
        btn3.alignHorizontally(self._frame, Arcade.ALIGN_CENTER)
        self._upgradeButtons.append(btn3)

        self._btnSelect.setNeighbors(None, self._btnMove, None, None)
        self._btnMove.setNeighbors(self._btnSelect, btn1, None, None)
        btn1.setNeighbors(self._btnMove, btn2, None, None)
        btn2.setNeighbors(btn1, btn3, None, None)
        btn3.setNeighbors(btn2, None, None, None)

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

        for btn in self._upgradeButtons:
            btn.update(screen)

        if(self._btnMove.isClicked()):
            PlaceDefenderGUI.DEFENDER = self._selectedDefender
            Arcade.setSelectedGUI(None)
        
        if(self._btnSelect.isClicked()):
            SelectDefenderGUI.SELECT = True
            Arcade.setSelectedGUI(None)

    def setSelectedDefender(self, defender):
        if(self._selectedDefender != None):
            self._selectedDefender.setSelected(False)

        self._selectedDefender = defender
        self._selectedDefender.setSelected(True)

        if(len(defender.getUpgrades()) > 0):
            self._upgradeButtons[0].setUpgrade(defender.getUpgrades()[0])
        if(len(defender.getUpgrades()) > 1):
            self._upgradeButtons[1].setUpgrade(defender.getUpgrades()[1])
        if(len(defender.getUpgrades()) > 2):
            self._upgradeButtons[2].setUpgrade(defender.getUpgrades()[2])

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


class UpgradeButton(Button.Button):

    def __init__(self, *args, **kwargs):
        super().__init__(width=160, height=70,*args, **kwargs)
        
        self.addBorder(2, (0,0,0))
        self._upgrade = None
        self._unlockedTierColor = (200, 200, 5)
        self._tierColor = (198,198,198)

        self._imageFrame = Frame.Frame(width=27*2, height=27*2)
        self._imageFrame.alignHorizontally(self, Arcade.ALIGN_LEFT)
        self._imageFrame.alignVertically(self, Arcade.ALIGN_TOP)
        self._imageFrame.addBorder(2, (0,0,0))
        self.attachGui(self._imageFrame)

        self._tierFrame = Frame.Frame(width=37*2, height=9*2)
        self._tierFrame.alignHorizontally(self, Arcade.ALIGN_LEFT)
        self._tierFrame.alignVertically(self, Arcade.ALIGN_BOTTOM)
        self.attachGui(self._tierFrame)

        self._tier1 = Frame.Frame(width=13*2, height=9*2, bgColor=self._tierColor)
        self._tier1.addBorder(2, (0,0,0))
        self._tier1.alignHorizontally(self._tierFrame, Arcade.ALIGN_LEFT)
        self._tier1.alignVertically(self._tierFrame, Arcade.ALIGN_CENTER)
        self.attachGui(self._tier1)

        self._tier2 = Frame.Frame(width=13*2, height=9*2, bgColor=self._tierColor)
        self._tier2.addBorder(2, (0,0,0))
        self._tier2.alignHorizontally(self._tierFrame, Arcade.ALIGN_CENTER)
        self._tier2.alignVertically(self._tierFrame, Arcade.ALIGN_CENTER)
        self.attachGui(self._tier2)

        self._tier3 = Frame.Frame(width=13*2, height=9*2, bgColor=self._tierColor)
        self._tier3.addBorder(2, (0,0,0))
        self._tier3.alignHorizontally(self._tierFrame, Arcade.ALIGN_RIGHT)
        self._tier3.alignVertically(self._tierFrame, Arcade.ALIGN_CENTER)
        self.attachGui(self._tier3)

        self._lblName = Label.Label()
        self._lblName.addText("", Arcade.FONT, (0,0,0), 18)
        self._lblName.alignHorizontally(self, Arcade.ALIGN_CENTER, 27)
        self._lblName.alignVertically(self, Arcade.ALIGN_TOP, 3)

    def update(self, screen):
        self._imageFrame.update(screen)
        self._tier1.update(screen)
        self._tier2.update(screen)
        self._tier3.update(screen)
        self._lblName.update(screen)

        super().update(screen)

        #if(self._)
    
    def show(self, tof):
        super().show(tof)
    
    def setUpgrade(self, upgrade):
        self._upgrade = upgrade

        self._lblName.setText(upgrade.getName())
        self._imageFrame.addImage(self._upgrade.getImage())

        self._tier1.setBgColor(self._tierColor)
        self._tier2.setBgColor(self._tierColor)
        self._tier3.setBgColor(self._tierColor)

        if(self._upgrade.getTier() == 1):
            self._tier1.setBgColor(self._unlockedTierColor)
        if(self._upgrade.getTier() == 2):
            self._tier2.setBgColor(self._unlockedTierColor)
        if(self._upgrade.getTier() == 3):
            self._tier3.setBgColor(self._unlockedTierColor)