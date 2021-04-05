import pygame, random

from libs.SimpleArcade import Arcade, Timer, Animation
from libs.SimpleArcade.gui import Label

from games.Titanic import State, Assets, Handler

class GameState:

    def __init__(self):
        super().__init__()

        self._lblPlay = Label.Label()
        self._lblPlay.addText("Spela", Arcade.FONT, (255,255,255), 70)
        self._lblPlay.alignHorizontally(None, Arcade.ALIGN_CENTER)
        self._lblPlay.alignVertically(None, Arcade.ALIGN_CENTER, -220)

        self._lblStart = Label.Label()
        self._lblStart.addText("Starta - (knapp 1)", Arcade.FONT, (255,255,255), 40)
        self._lblStart.alignHorizontally(None, Arcade.ALIGN_CENTER)
        self._lblStart.alignVertically(None, Arcade.ALIGN_CENTER, -50)

        self._lblBack = Label.Label()
        self._lblBack.addText("Avsluta - (knapp 2)", Arcade.FONT, (255,255,255), 40)
        self._lblBack.alignHorizontally(None, Arcade.ALIGN_CENTER)
        self._lblBack.alignVertically(None, Arcade.ALIGN_CENTER, 20)

        self._lblScore = Label.Label(y=10)
        self._lblScore.addText("Score: ", Arcade.FONT, (255,255,255), 50)
        self._lblScore.alignHorizontally(None, Arcade.ALIGN_CENTER)

        self._lblFinalScore = Label.Label(y=130)
        self._lblFinalScore.addText("Score: 0", Arcade.FONT, (255,255,255), 35)
        self._lblFinalScore.alignHorizontally(None, Arcade.ALIGN_CENTER)

        self._iceBergs = []
        self._started = False
        self._score = 0
        self._origIceBergSpawn = 3000
        self._origBoatSpeed = 2
        self._boatSpeed = self._origBoatSpeed
        self._lines = [27*4,93*4,159*4]
        self._currentLine = 1
        self._boat = [self._lines[self._currentLine], Arcade.SCREEN_HEIGHT-220, Assets.boat.get_width(), Assets.boat.get_height()]

        self._wavesAnim = Animation.Animation(Assets.wavesSheet.getImagesByRow(0), 800, continuous=True)
        self._wavesAnim.start()

        self._iceBergsLines = [-2*4, 65*4, 132*4]
        self._iceBergTimer = Timer.Timer(self._origIceBergSpawn)

    def update(self, screen):
        screen.blit(Assets.water, (0,0))

        if(self._started == False):
            self._lblPlay.update(screen)
            self._lblStart.update(screen)
            self._lblBack.update(screen)
            self._lblFinalScore.update(screen)

            self._wavesAnim.update()
            screen.blit(self._wavesAnim.getCurrentFrame(), (self._boat[0]-6*4, self._boat[1]+44*4))
            screen.blit(Assets.boat, (self._boat[0], self._boat[1]))

            if(Arcade.BUTTON_PRESSED_1):
                self._started = True
                self._iceBergTimer.start()
                self._iceBergTimer.done = True
            elif(Arcade.BUTTON_PRESSED_2):
                Handler.quit = True
                return
            else:
                return

        self._lblScore.update(screen)

        self._iceBergTimer.update()

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
            self.addScore(1)

        for iceBerg in self._iceBergs:
            iceBerg[1] += self._boatSpeed * Arcade.DELTA_TIME
            
            screen.blit(iceBerg[4], (iceBerg[0], iceBerg[1]))

        self._wavesAnim.update()
        screen.blit(self._wavesAnim.getCurrentFrame(), (self._boat[0]-6*4, self._boat[1]+44*4))
        screen.blit(Assets.boat, (self._boat[0], self._boat[1]))

        for iceBerg in self._iceBergs:
            if(iceBerg[1] > Arcade.SCREEN_HEIGHT):
                self._iceBergs.remove(iceBerg)
            
            if(iceBerg[5] == self._currentLine):
                if(iceBerg[1]+iceBerg[3]-80 > self._boat[1] and iceBerg[1]+80 < self._boat[1]+self._boat[3]):
                    self.reset()

    def addIceBerg(self, quantity):
        lines = self._iceBergsLines.copy()

        for i in range(quantity):
            line = random.randint(0, len(lines)-1)
            img = random.randint(0,1)
            actualLine = self._iceBergsLines.index(lines[line])
            iceBerg = [lines[line], -200, 70*4, 70*4, Assets.iceSheet.getImage(img, 0), actualLine]
            lines.remove(lines[line])
            self._iceBergs.append(iceBerg)

    def reset(self):
        self._currentLine = 1
        self._boat[0] = self._lines[self._currentLine]
        self._started = False
        self._iceBergTimer.start()
        self._iceBergTimer.done = True
        self._boatDistance = 0
        self._iceBergs.clear()
        self._lblFinalScore.setText("Score: " + str(self._score))
        self._score = 0
        self.addScore(0)

    def addScore(self, score):
        self._score += score
        self._lblScore.setText("Score: " + str(self._score))

        self._boatSpeed = self._origBoatSpeed + self._score/4
        self._iceBergTimer.speed = self._origIceBergSpawn - (self._score*40)

    def onShow(self):
        pass