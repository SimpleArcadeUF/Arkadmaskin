from libs.SimpleArcade.gui import Label
from libs.SimpleArcade import Arcade

class GameplayGUI():

    def __init__(self):
        
        self._lblWave = Label.Label(x=10, y=10)
        self._lblWave.addText("", Arcade.FONT, (50,50,70), 60)
        self._lblWave.addUnderline(4, (50,50,70), offset=-8)

        self._lblHealth = Label.Label(x=10, y=90)
        self._lblHealth.addText("Liv: ", Arcade.FONT, (50,50,70), 30)

        self._lblMoney = Label.Label(x=10, y=125)
        self._lblMoney.addText("Pengar: ", Arcade.FONT, (50,50,70), 30)

        self._startWaveMessage = False
        self._newWaveMessage = False
        self._lblNewWaveNumber = Label.Label(y=180)
        self._lblNewWaveNumber.alignHorizontally(None, Arcade.ALIGN_CENTER, -100)
        self._lblNewWaveNumber.addText("0", Arcade.FONT, (30,130,130), 70)
        self._lblNewWaveNumber.addUnderline(4, (30,130,130), offset=-10)

        self._lblNewWave = Label.Label(y=270)
        self._lblNewWave.alignHorizontally(None, Arcade.ALIGN_CENTER, -100)
        self._lblNewWave.addText("Grattis! Du har klarat en ny nivå.", Arcade.FONT, (30,30,30), 32)
        
        self._lblNewWaveInfo = Label.Label(y=325)
        self._lblNewWaveInfo.alignHorizontally(None, Arcade.ALIGN_CENTER, -100)
        self._lblNewWaveInfo.addText("Tryck (knapp 3) för att börja nästa.", Arcade.FONT, (50,50,50), 28)

    def update(self, screen):
        self._lblWave.update(screen)
        self._lblHealth.update(screen)
        self._lblMoney.update(screen)

        if(self._newWaveMessage == True):
            self._lblNewWave.update(screen)
            self._lblNewWaveInfo.update(screen)
            self._lblNewWaveNumber.update(screen)
        if(self._startWaveMessage == True):
            self._lblNewWaveInfo.update(screen)

    def updateHealth(self, health):
        self._lblHealth.setText("Liv: " + str(health))
    def updateMoney(self, money):
        self._lblMoney.setText("Pengar: " + str(money))
    def updateWave(self, wave):
        self._lblWave.setText(str(wave))
    def showNewWaveMessage(self, wave):
        self._newWaveMessage = True
        self._lblNewWaveNumber.setText(str(wave))
    def hideNewWaveMessage(self):
        self._newWaveMessage = False
    def showStartMessage(self):
        self._startWaveMessage = True
    def hideStartMessage(self):
        self._startWaveMessage = False
    
    def hide(self):
        pass