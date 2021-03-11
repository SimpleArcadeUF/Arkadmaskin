import pygame
from libs.SimpleArcade.gui import GUI
from libs.SimpleArcade import Arcade

class Label(GUI.GUI):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._textSurface = None
        self._font = None
        self._text = None
        self._haveUnderline = False
        self._underlineSize = 0
        self._underlineColor = None
        self._underlineOffset = 0
        self._haveHighlightedText = False
        self._textSurfaceHighlighted = None
        self._textSurfaceHighlightedColor = None
        self._forceHover = False

    def update(self, screen):
        super().update(screen)

        if(self._show == False): return

        if(self._haveUnderline):
            pygame.draw.rect(screen, self._underlineColor, (self._x, self._y+self._height+self._underlineOffset, self._width, self._underlineSize))

        if(self._textSurface != None):
            textSurface = self._textSurface

            if(self._haveHighlightedText and (self.isHovered() or self._forceHover)):
                textSurface = self._textSurfaceHighlighted

            screen.blit(textSurface, (self._x, self._y))

    def addUnderline(self, size, color, offset=0):
        self._haveUnderline = True
        self._underlineSize = size
        self._underlineColor = color
        self._underlineOffset = offset

    def addHighlightedText(self, color):
        self._haveHighlightedText = True
        self._textSurfaceHighlightedColor = color

        if(self._font != None and self._text != None):
            self._textSurfaceHighlighted = self._font.render(self._text, color)

    def addText(self, text, fontName, textColor, fontSize):
        self._textColor = textColor
        self._text = text
        
        self._font = pygame.font.Font(fontName, fontSize)
        self.setText(text, textColor)

    def setText(self, text, textColor=None):
        if(textColor == None):
            textColor = self._textColor

        self._textColor = textColor
        self._text = text

        self._textSurface = self._font.render(text, False, textColor)
        self.setWidth(self._textSurface.get_width())
        self.setHeight(self._textSurface.get_height())

        if(self._haveHighlightedText):
            self._textSurfaceHighlighted = self._font.render(self._text, False, self._textSurfaceHighlightedColor)

    def setForceHover(self, tof):
        self._forceHover = tof
    def getTextColor(self):
        return self._textColor
    def getText(self):
        return self._text
    def haveHighlightedText(self):
        return self._haveHighlightedText