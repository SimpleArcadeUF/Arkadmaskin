import pygame

from libs.SimpleArcade.gui import Button, Label, Frame
from libs.SimpleArcade import Arcade

from games.Bloons.utils import Assets

class MenuGUI:

    def __init__(self):
        super().__init__()

        self._width = 192
        self._buttons = []

        self.addButton("Försvarare", Assets.menuButtons.getImage(0,0))
        self.addButton("Affär", Assets.menuButtons.getImage(1,0))
        self.addButton("Allmänt", Assets.menuButtons.getImage(2,0))

        #Button neighbors
        self._buttons[0].setNeighbors(None, self._buttons[1], None, None)
        self._buttons[1].setNeighbors(self._buttons[0], self._buttons[2], None, None)
        self._buttons[2].setNeighbors(self._buttons[1], None, None, None)
        
        self._frame = Frame.Frame(x=Arcade.SCREEN_WIDTH-self._width, y=0, width=self._width, height=Arcade.SCREEN_HEIGHT, bgColor=(206, 170, 130))
        self._frame.addBorder(2, (0,0,0))

        self._lblSelectedName = Label.Label(y=20)
        self._lblSelectedName.addText(self._buttons[0].getLabel().getText(), Arcade.FONT, (255,255,255), 25)
        self._lblSelectedName.alignHorizontally(self._frame, Arcade.ALIGN_CENTER)

        self._newOpenMenuID = -1

    def update(self, screen):
        self._frame.update(screen)
        self._lblSelectedName.update(screen)

        for i in range(len(self._buttons)):
            btn = self._buttons[i]
            btn.update(screen)

            if(btn.isHovered()):
                self._lblSelectedName.setText(self._buttons[i].getLabel().getText())
        
        if(self._buttons[0].isClicked()): #Defenders
            self._newOpenMenuID = 0
        if(self._buttons[1].isClicked()): #Shop
            self._newOpenMenuID = 1
        if(self._buttons[2].isClicked()): #General
            self._newOpenMenuID = 2

    def addButton(self, name, image):
        spacing = 40
        width = 80
        height = 120

        btn = Button.Button(bgColor=(255,255,255), x=Arcade.SCREEN_WIDTH-(self._width/2+width/2), y = 90 + len(self._buttons)*(height+spacing), width=width, height=height)
        btn.addText(name, Arcade.FONT, (0,0,0), 25)
        btn.getLabel().alignVertically(btn, Arcade.ALIGN_BOTTOM)
        btn.addImage(image)
        btn.addBorder(2, (0,0,0))
        btn.getLabel().show(False)

        self._buttons.append(btn)

    def returnNewOpenMenu(self):
        return self._newOpenMenuID
    def resetNewOpenMenu(self):
        self._newOpenMenuID = -1

    def show(self):
        Arcade.setSelectedGUI(self._buttons[0])
        self.resetNewOpenMenu()

    def hide(self):
        pass