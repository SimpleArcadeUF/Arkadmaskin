import pygame
from libs.SimpleArcade.gui import GUI, Label
from libs.SimpleArcade import Arcade

class Button(GUI.GUI):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._lblText = Label.Label()
        self._lblText.addHighlightedText(Arcade.GUI_COLOR_ORANGE)
        self._lblText.alignHorizontally(self, Arcade.ALIGN_CENTER)
        self._lblText.alignVertically(self, Arcade.ALIGN_CENTER)
        
        self.addBorder(2, Arcade.GUI_COLOR_RED)
        self.addHighlightedBorder(Arcade.GUI_COLOR_ORANGE)

        self.attachGui(self._lblText)
    
    def update(self, screen):
        super().update(screen)

        self._lblText.update(screen)
        
        if(self._lblText.haveHighlightedText() and self.isHovered()):
            self._lblText.setForceHover(True)
        else:
            self._lblText.setForceHover(False)


    def addText(self, text, fontName, textColor, fontSize):
        self._lblText.addText(text, fontName, textColor, fontSize)

    def setText(self, text):
        self._lblText.setText(text, self._lblText.getTextColor())
    
    def getLabel(self):
        return self._lblText