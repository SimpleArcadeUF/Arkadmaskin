import pygame, random

from libs.SimpleArcade import Arcade, Timer
from libs.SimpleArcade.gui import Label

from games.Titanic import State, Assets, Handler

class GameState:

    def __init__(self):
        super().__init__()

        self._lblPlay = Label.Label()
        self._lblPlay.addText("Spela", Arcade.FONT, (255,255,255), 70)
        self._lblPlay.alignHorizontally(None, Arcade.ALIGN_CENTER)
        self._lblPlay.alignVertically(None, Arcade.ALIGN_CENTER, -180)

        self._lblStart = Label.Label()
        self._lblStart.addText("Starta - (knapp 1)", Arcade.FONT, (255,255,255), 40)
        self._lblStart.alignHorizontally(None, Arcade.ALIGN_CENTER)
        self._lblStart.alignVertically(None, Arcade.ALIGN_CENTER, -50)

        self._lblBack = Label.Label()
        self._lblBack.addText("Avsluta - (knapp 2)", Arcade.FONT, (255,255,255), 40)
        self._lblBack.alignHorizontally(None, Arcade.ALIGN_CENTER)
        self._lblBack.alignVertically(None, Arcade.ALIGN_CENTER, 20)

        self._iceBergs = []
        self._started = False
        self._boatDistance = 0
        self._boatSpeed = 5
        self._lines = [27*4,93*4,159*4]
        self._currentLine = 1
        self._boat = [self._lines[self._currentLine], Arcade.SCREEN_HEIGHT-200, Assets.boat.get_width(), Assets.boat.get_height()]

        self._iceBergsLines = [-2*4, 65*4, 132*4]
        self._iceBergTimer = Timer.Timer(2000)

    def update(self, screen):
        screen.blit(Assets.water, (0,0))

        if(self._started == False):
            self._lblPlay.update(screen)
            self._lblStart.update(screen)
            self._lblBack.update(screen)

            if(Arcade.BUTTON_PRESSED_1):
                self._started = True
                self._iceBergTimer.start()
                self._iceBergTimer.done = True
            elif(Arcade.BUTTON_PRESSED_2):
                Handler.setState(Handler.menuState)
                return
            else:
                return

        self._iceBergTimer.update()
        self._boatDistance += self._boatSpeed

        if(Arcade.JOYSTICK_PRESSED_LEFT):
            self._currentLine = max(0, self._currentLine-1)
            self._boat[0] = self._lines[self._currentLine]
        if(Arcade.JOYSTICK_PRESSED_RIGHT):
            self._currentLine = min(2, self._currentLine+1)
            self._boat[0] = self._lines[self._currentLine]
        
        if(self._iceBergTimer.isDone()):
            self._iceBergTimer.start()
            procentage = random.randint(0,100)
            quantity = 1
            if(procentage <= 33):
                quantity = 2
            self.addIceBerg(quantity)

        for iceBerg in self._iceBergs:
            iceBerg[1] += self._boatSpeed
            screen.blit(iceBerg[4], (iceBerg[0], iceBerg[1]))

        screen.blit(Assets.boat, (self._boat[0], self._boat[1]))

        for iceBerg in self._iceBergs:
            if(iceBerg[1] > Arcade.SCREEN_HEIGHT):
                self._iceBergs.remove(iceBerg)
            
            #if(self._boat[5] == self._currentLine)

    def addIceBerg(self, quantity):
        lines = self._iceBergsLines.copy()

        for i in range(quantity):
            line = random.randint(0, len(lines)-1)
            img = random.randint(0,1)
            actualLine = self._iceBergsLines.index(lines[line])
            iceBerg = [lines[line], -200, 70*4, 70*4, Assets.iceSheet.getImage(img, 0), actualLine]
            lines.remove(lines[line])
            self._iceBergs.append(iceBerg)

    def onShow(self):
        pass