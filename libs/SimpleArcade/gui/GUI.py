import pygame
from libs.SimpleArcade import Arcade

class GUI:

    def __init__(self, x=0, y=0, width=100, height=100, bgColor=None):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._bgColor = bgColor
        
        self._horizontalAlignment = -1
        self._verticalAlignment = -1
        self._horizontalAlignmentGui = None
        self._verticalAlignmentGui = None
        self._horizontalAlignmentOffset = 0
        self._verticalAlignmentOffset = 0

        self._haveBorder = False
        self._borderColor = None
        self._borderSize = 0
        self._haveHighligtedBorder = False
        self._highlightedBorderColor = None

        self._hovered = False
        self._clicked = False
        self._show = True
        self._attachedGuis = []
        self._updateAttachedGuis = False
        self._image = None

        self._neighborTop = None
        self._neighborBottom = None
        self._neighborLeft = None
        self._neighborRight = None
    
    def update(self, screen):
        if(self._show == False): return

        self._setHovered()
        self._setIsClicked()

        self._updateGuiHovered()

        if(self._bgColor != None):
            pygame.draw.rect(screen, self._bgColor, (self._x, self._y, self._width, self._height))

        if(self._image != None):
            screen.blit(self._image, (self._x, self._y))

        if(self._haveBorder):
            color = self._borderColor
            if(self._haveHighligtedBorder and self.isHovered()):
                color = self._highlightedBorderColor

            pygame.draw.rect(screen, color, (self._x, self._y, self._width, self._borderSize)) #Top
            pygame.draw.rect(screen, color, (self._x, self._y+self._height-self._borderSize, self._width, self._borderSize)) #Bottom
            pygame.draw.rect(screen, color, (self._x, self._y, self._borderSize, self._height)) #Left
            pygame.draw.rect(screen, color, (self._x+self._width-self._borderSize, self._y, self._borderSize, self._height)) #Right

        if(self._updateAttachedGuis):
            for gui in self._attachedGuis:
                gui.update(screen)

    def _updateGuiHovered(self):
        if(Arcade.PLATFORM == Arcade.PLATFORM_ARCADE and Arcade.SELECTED_GUI == self):
            if(Arcade.BUTTON_PRESSED_1): #Left
                if(self._neighborLeft != None):
                    Arcade.setSelectedGUI(self._neighborLeft)
                    Arcade.BUTTON_PRESSED_1 = False
            elif(Arcade.JOYSTICK_PRESSED_UP): #Top
                if(self._neighborTop != None):
                    Arcade.setSelectedGUI(self._neighborTop)
                    Arcade.JOYSTICK_PRESSED_UP = False
            elif(Arcade.JOYSTICK_PRESSED_DOWN): #Bottom
                if(self._neighborBottom != None):
                    Arcade.setSelectedGUI(self._neighborBottom)
                    Arcade.JOYSTICK_PRESSED_DOWN = False
            elif(Arcade.BUTTON_PRESSED_4): #Right
                if(self._neighborRight != None):
                    Arcade.setSelectedGUI(self._neighborRight)
                    Arcade.BUTTON_PRESSED_4 = False
    
    def addImage(self, image):
        self._image = image
        self._image = pygame.transform.scale(self._image, (self._width, self._height))

    def addBorder(self, size, color):
        self._haveBorder = True
        self._borderSize = size
        self._borderColor = color

    def addHighlightedBorder(self, color):
        self._haveHighligtedBorder = True
        self._highlightedBorderColor = color

    def removeHighlightedBorder(self):
        self._haveHighligtedBorder = False

    def alignHorizontally(self, gui, alignment, offset=0):
        self._horizontalAlignmentOffset = offset
        self._horizontalAlignment = alignment
        self._horizontalAlignmentGui = gui

        if(alignment == Arcade.ALIGN_CENTER):
            if(gui == None):
                w, h = pygame.display.get_surface().get_size()
                self.setX(w / 2 - self._width/2 + offset)
            else:
                self.setX(gui.getX() + (gui.getWidth() - self._width) / 2 + offset)
        
        elif(alignment == Arcade.ALIGN_LEFT):
            if(gui == None):
                self.setX(0 + offset)
            else:
                self.setX(gui.getX() + offset)
        
        elif(alignment == Arcade.ALIGN_RIGHT):
            if(gui == None):
                w, h = pygame.display.get_surface().get_size()
                self.setX(w - self._width + offset)
            else:
                self.setX(gui.getX()+gui.getWidth() - self._width + offset)
            
    def alignVertically(self, gui, alignment, offset=0):
        self._verticalAlignmentOffset = offset
        self._verticalAlignmentGui = gui
        self._verticalAlignment = alignment

        if(alignment == Arcade.ALIGN_CENTER):
            if(gui == None):
                w, h = pygame.display.get_surface().get_size()
                self.setY(h / 2 - self._height/2 + offset)
            else:
                
                self.setY(gui.getY() + (gui.getHeight() - self._height) / 2 + offset)
        
        elif(alignment == Arcade.ALIGN_TOP):
            if(gui == None):
                self.setY(0 + offset)
            else:
                self.setY(gui.getY() + offset)
        
        elif(alignment == Arcade.ALIGN_BOTTOM):
            if(gui == None):
                w, h = pygame.display.get_surface().get_size()
                self.setY(h - self._height + offset)
            else:
                self.setY(gui.getY() + gui.getHeight() - self._height + offset)

    def updateAttachedGuis(self, tof):
        self._updateAttachedGuis = tof

    def attachGui(self, gui):
        self._attachedGuis.append(gui)

    def setX(self, x):
        for gui in self._attachedGuis:
            dx = x - self._x
            gui.setX(gui.getX() + dx)
        self._x = x

    def setY(self, y):
        for gui in self._attachedGuis:
            dy = y - self._y
            gui.setY(gui.getY() + dy)
        self._y = y

    def setWidth(self, width):
        self._width = width
        self.alignHorizontally(self._horizontalAlignmentGui, self._horizontalAlignment, self._horizontalAlignmentOffset)
    def setHeight(self, height):
        self._height = height
        self.alignVertically(self._verticalAlignmentGui, self._verticalAlignment, self._verticalAlignmentOffset)

    def _setHovered(self):
        if(Arcade.PLATFORM == Arcade.PLATFORM_DESKTOP):
            self._hovered = False
            pos = pygame.mouse.get_pos()
            if(pos[0] > self._x and pos[0] < self._x + self._width):
                if(pos[1] > self._y and pos[1] < self._y + self._height):
                    self._hovered = True
    
    def _setIsClicked(self):
        self._clicked = False
        if(Arcade.PLATFORM == Arcade.PLATFORM_DESKTOP):
            if(self._hovered and pygame.mouse.get_pressed()[0] and Arcade.GUI_IS_CLICKED == False):
                self._clicked = True
        elif(Arcade.PLATFORM == Arcade.PLATFORM_ARCADE):
            if(self._hovered and Arcade.BUTTON_PRESSED_1):
                self._clicked = True
    
    def setNeighbors(self, top, bottom, left, right):
        self._neighborTop = top
        self._neighborBottom = bottom
        self._neighborLeft = left
        self._neighborRight = right

    def setHovered(self, tof):
        self._hovered = tof

    def isHovered(self):
        return self._hovered
    def isClicked(self):
        return self._clicked
    def getX(self):
        return self._x
    def getY(self):
        return self._y
    def getWidth(self):
        return self._width
    def getHeight(self):
        return self._height
    def isShown(self):
        return self._show
    def show(self, tof):
        self._show = tof