import pygame

from games.Bloons.states import State
from games.Bloons.utils import Handler, Timer, Assets
from games.Bloons.entity import Balloons, Monkey, Projectile
from games.Bloons.guis import GameplayGUI, ShopGUI, PlaceDefenderGUI

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

        self._shopGUI = ShopGUI.ShopGUI()
        self._placeDefenderGUI = PlaceDefenderGUI.PlaceDefenderGUI()

    def update(self, screen):
        super().update(screen)

        #screen.fill((20, 250, 15))
        screen.blit(Assets.map1, (0,0))

        #if(pygame.mouse.get_pressed()[0]):
        #    if(self._mouseClicked == False):
        #        self._mouseClicked = True
        #        self._defenders.append(Monkey.Monkey(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]))
        #else:
        #    self._mouseClicked = False

        if(pygame.key.get_pressed()[pygame.K_SPACE]):
            if(self._waveOneStarted == False):
                self._waveOneStarted = True
                self._gameplayGUI.hideStartMessage()

        if(Handler.currentMap != None):
            Handler.currentMap.update(screen)

        for balloon in self._balloons:

            if(balloon.shouldCreateNextBalloon()):
                if(balloon.getNextBalloon() == "r"):
                    self._balloons.append(Balloons.red.createOnParent(balloon))
                elif(balloon.getNextBalloon() == "b"):
                    self._balloons.append(Balloons.blue.createOnParent(balloon))
                elif(balloon.getNextBalloon() == "g"):
                    self._balloons.append(Balloons.green.createOnParent(balloon))
                elif(balloon.getNextBalloon() == "y"):
                   self._balloons.append(Balloons.yellow.createOnParent(balloon))

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
            defender.update(screen)
            defender.setTargetBallon(self._balloons)

        for projectile in Projectile.PROJECTILES:
            projectile.update(screen, self._balloons)
            projectile.updateCollision(self._balloons)

        if(self._waveOneStarted):
            self.updateSpawnBalloons()

        self.updateStartNewWave()

        self._gameplayGUI.update(screen)
        self._shopGUI.update(screen, self._money)
        if(self._shopGUI.boughtDefender()):
            self._shopGUI.setBoughtDefender(False)
            self.addMoney(-self._shopGUI.getBoughtDefenderCost())

        self._placeDefenderGUI.update(screen)
        self._placeDefenderGUI.updatePlace(screen, self._defenders)
    
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
        if(self._waveDone):
            keys = pygame.key.get_pressed()
            if(keys[pygame.K_SPACE]):
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