import pygame

from libs.SimpleArcade import Arcade

from games.Bloons.states import State
from games.Bloons.utils import Handler, Timer, Assets
from games.Bloons.entity import Balloons, Monkey, Projectile
from games.Bloons.guis import GameplayGUI, ShopGUI, PlaceDefenderGUI, MenuGUI, GeneralGUI, DefendersGUI, SelectDefenderGUI

class GameState(State.State):

    def __init__(self):
        super().__init__()

        self._balloons = []
        self._spawnBallonTimer = Timer.Timer(200, applyGameSpeed=True)
        self._currentBalloonWave = None
        self._currentBalloonSpawnIndex = 0
        self._spawningBalloons = False
        self._currentBalloonsSpawned = 0
        self._currentWave = 1
        self._waveDone = False

        self._defenders = []
        self._mouseClicked = False

        self._maxHealth = 100
        self._health = self._maxHealth
        self._money = 350
        self._waveOneStarted = False

        self._gameplayGUI = GameplayGUI.GameplayGUI()
        self._gameplayGUI.updateHealth(self._health)
        self._gameplayGUI.updateMoney(self._money)
        self._gameplayGUI.updateWave(self._currentWave)
        self._gameplayGUI.showStartMessage()

        self._currentMenu = None
        
        self._menuGUI = MenuGUI.MenuGUI()
        self._shopGUI = ShopGUI.ShopGUI()
        self._defendersGUI = DefendersGUI.DefendersGUI()
        self._generalGUI = GeneralGUI.GeneralGUI()
        self._placeDefenderGUI = PlaceDefenderGUI.PlaceDefenderGUI()
        self._selectDefenderGUI = SelectDefenderGUI.SelectDefenderGUI()

        self._changeCurrentMenu(self._menuGUI)

    def update(self, screen):
        super().update(screen)

        screen.blit(Assets.map1, (0,0))

        if(Handler.currentMap != None):
            Handler.currentMap.update(screen)

        for balloon in self._balloons:

            if(balloon.shouldCreateNextBalloon()):
                if(balloon.getNextBalloon() == "r"):
                    self._balloons.append(Balloons.red.createOnParent(balloon, frozen=balloon.shouldCreateNextBalloonFrozen()))
                elif(balloon.getNextBalloon() == "b"):
                    self._balloons.append(Balloons.blue.createOnParent(balloon, frozen=balloon.shouldCreateNextBalloonFrozen()))
                elif(balloon.getNextBalloon() == "g"):
                    self._balloons.append(Balloons.green.createOnParent(balloon, frozen=balloon.shouldCreateNextBalloonFrozen()))
                elif(balloon.getNextBalloon() == "y"):
                   self._balloons.append(Balloons.yellow.createOnParent(balloon, frozen=balloon.shouldCreateNextBalloonFrozen()))

            if(balloon.isDeleted() == True):
                self._balloons.remove(balloon)
                if(len(self._balloons) == 0 and self._spawningBalloons == False):
                    self.waveDone()
                if(balloon.getHitProjectile() != None):
                    self.addMoney(1)

            balloon.update(screen)
            balloon.move(Handler.currentMap.getPath())
            
            if(balloon.getCurrentNodeIndex() == len(Handler.currentMap.getPath())):
                self._balloons.remove(balloon)
                balloon.delete()
                self.addHealth(-balloon.getRBE())
                self._gameplayGUI.updateHealth(self._health)
                
                if(len(self._balloons) == 0):
                    self.waveDone()
        
        for defender in self._defenders:
            defender.update(screen, self._balloons)
            defender.setTargetBallon(self._balloons)

        for projectile in Projectile.PROJECTILES:
            projectile.update(screen, self._balloons)
            projectile.updateCollision(self._balloons)

        if(self._waveOneStarted):
            self.updateSpawnBalloons()

        self.updateStartNewWave()

        self._updateGUI(screen)

    def _updateGUI(self, screen):
        
        if(Arcade.BUTTON_PRESSED_2 and self._currentMenu != self._menuGUI):
            self._changeCurrentMenu(self._menuGUI)

        self._gameplayGUI.update(screen)

        if(self._currentMenu == self._shopGUI):
            self._currentMenu.update(screen, self._money)
        else:
            self._currentMenu.update(screen)

        if(self._currentMenu == self._menuGUI):
            menuID = self._currentMenu.returnNewOpenMenu()
            if(menuID == 0):
                self._changeCurrentMenu(self._defendersGUI)
            elif(menuID == 1):
                self._changeCurrentMenu(self._shopGUI)
            elif(menuID == 2):
                self._changeCurrentMenu(self._generalGUI)

        #-----PlaceDefenderGUI-----
        self._placeDefenderGUI.update(screen)
        self._placeDefenderGUI.updatePlace(self._defenders)
        if(self._placeDefenderGUI.onPlace()):
            self._changeCurrentMenu(self._currentMenu)
            self._placeDefenderGUI.reset()

            if(self._shopGUI.boughtDefender()):
                self._shopGUI.setBoughtDefender(False)
                self.addMoney(-self._shopGUI.getBoughtDefenderCost())
        if(self._placeDefenderGUI.onCancel()):
            self._changeCurrentMenu(self._currentMenu)
            self._placeDefenderGUI.reset()

        #-----SelectDefenderGUI-----
        self._selectDefenderGUI.update(screen)
        self._selectDefenderGUI.updateSelect(self._defenders)
        if(self._selectDefenderGUI.onSelect()):
            self._changeCurrentMenu(self._currentMenu)
            self._defendersGUI.setSelectedDefender(self._selectDefenderGUI.getSelectedDefender())
            self._selectDefenderGUI.resetSelect()
        if(self._selectDefenderGUI.onCancel()):
            self._changeCurrentMenu(self._currentMenu)
            self._selectDefenderGUI.resetSelect()
    
    def _changeCurrentMenu(self, gui):
        if(self._currentMenu != None):
            self._currentMenu.hide()
        self._currentMenu = gui

        if(self._currentMenu == self._defendersGUI):
            self._currentMenu.show(self._defenders)
        else:
            self._currentMenu.show()

        if(self._currentMenu == self._menuGUI):
            self._currentMenu.resetNewOpenMenu()

    def waveDone(self):
        self._waveDone = True
        self._currentWave += 1
        self._gameplayGUI.showNewWaveMessage(self._currentWave)
        self._gameplayGUI.updateWave(self._currentWave)
        self.addMoney(250 + 100*(self._currentWave-1))

    def startWave(self):
        self._waveDone = False
        
        self._gameplayGUI.hideNewWaveMessage()
        self._spawnBalloons()

    def updateStartNewWave(self):
        if(Arcade.BUTTON_PRESSED_3):
            if(self._waveOneStarted == False):
                self._waveOneStarted = True
                self._gameplayGUI.hideStartMessage()
                return

        if(self._waveDone):
            if(Arcade.BUTTON_PRESSED_3):
                self.startWave()

    def _spawnBalloons(self):
        self._currentBalloonWave = Balloons.waves[self._currentWave-1]
        self._currentBalloonSpawnIndex = 0
        self._currentBalloonsSpawned = 0
        self._spawningBalloons = True
        self._spawnBallonTimer.start()

    def updateSpawnBalloons(self):
        self._spawnBallonTimer.update()

        if(self._spawningBalloons):
            if(self._spawnBallonTimer.isDone()):
                self._spawnBallonTimer.start()
                ballonType = self._currentBalloonWave[self._currentBalloonSpawnIndex]
                t = ballonType[0]
                amount = ballonType[1]

                if(t == "r"):
                    self._balloons.append(Balloons.red.create(Handler.currentMap.getPath()[0]))
                elif(t == "b"):
                    self._balloons.append(Balloons.blue.create(Handler.currentMap.getPath()[0]))
                elif(t == "g"):
                    self._balloons.append(Balloons.green.create(Handler.currentMap.getPath()[0]))
                elif(t == "y"):
                    self._balloons.append(Balloons.yellow.create(Handler.currentMap.getPath()[0]))
                elif(t == "bl"):
                    self._balloons.append(Balloons.black.create(Handler.currentMap.getPath()[0]))

                self._currentBalloonsSpawned += 1

                if(self._currentBalloonsSpawned == amount):
                    self._currentBalloonsSpawned = 0
                    self._currentBalloonSpawnIndex += 1

                    if(self._currentBalloonSpawnIndex == len(self._currentBalloonWave)):
                        self._spawningBalloons = False

    def setHealth(self, health):
        self._health = health
        self._gameplayGUI.updateHealth(self._health)
    def addHealth(self, health):
        self.setHealth(self._health+health)
    def setMoney(self, money):
        self._money = money
        self._gameplayGUI.updateMoney(self._money)

    def addMoney(self, money):
        self.setMoney(self._money + money)

    def show(self, tof):
        super().show(tof)

        self._changeCurrentMenu(self._menuGUI)