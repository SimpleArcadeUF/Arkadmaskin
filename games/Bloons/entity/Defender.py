import math, pygame

from libs.SimpleArcade import Animation

from games.Bloons.entity import Entity, Dart
from games.Bloons.utils import Timer

class Defender(Entity.Entity):

    def __init__(self, x, y, size, name, spriteSheet, attackRange, attackSpeed, amimAttackSpeed, projectile, use=True):
        super().__init__(x-size/2, y-size/2, size, color=None, draw=False)

        self._use = use
        self._name = name
        self._spriteSheet = spriteSheet
        self._attackRange = attackRange
        self._projectile = projectile
        self._showAttackRange = False
        self._selected = False
        self._attackRangeSurface = pygame.Surface((self._attackRange*2, self._attackRange*2))
        self._attackRangeSurface.set_colorkey((0,0,0))
        self._attackRangeSurface.set_alpha(100)
        pygame.draw.circle(self._attackRangeSurface, (50,50,50), (self._attackRange,self._attackRange), self._attackRange)

        self._targetBalloon = None
        self._searchForNearestBallon = False
        self._attackWaitTimer = Timer.Timer(attackSpeed)
        self._attackWaitTimer.start()
        self._canAttack = True

        self._upgrades = []

        self._dir = 0
        self._animAttack = Animation.Animation(spriteSheet.getImagesByRow(0), amimAttackSpeed, continuous=False)
        self._animIdle = Animation.Animation([spriteSheet.getImage(0,0), spriteSheet.getImage(0,0)], 1000)

        self.setCurrentAnim(self._animIdle)

    def update(self, screen):
        super().update(screen)

        self._currentAnim.update()

        currentImage = self._currentAnim.getCurrentFrame()
        rect = None

        if(self._targetBalloon != None):
            if(self._targetBalloon.isDeleted()):
                self._targetBalloon = None
            else:
                if(self._canAttack):
                    #attack
                    self._attackWaitTimer.update()

                    if(self._attackWaitTimer.isDone()):
                        self._attackWaitTimer.start()
                        self.setCurrentAnim(self._animAttack)
                        self._projectile.create(self._x+self._size/2, self._y+self._size/2, self._targetBalloon)

                    #rotated image
                    self._dir = -math.degrees(math.atan2((self._y+self._size/2)-(self._targetBalloon.getY()+self._targetBalloon.getSize()/2), (self._x+self._size/2)-(self._targetBalloon.getX()+self._targetBalloon.getSize()/2)))+90
        
        if(self._currentAnim == self._animAttack and self._animAttack.isDone()):
            self.setCurrentAnim(self._animIdle)
        
        currentImage = pygame.transform.rotate(currentImage, self._dir)
        rect = currentImage.get_rect(center=self._currentAnim.getCurrentFrame().get_rect(center=(self._x, self._y)).center)
        
        offsetX = 0
        offsetY = 0
        if(rect != None):
            offsetX = rect[2]/2-self._size/2
            offsetY = rect[3]/2-self._size/2

        screen.blit(currentImage, (self._x-offsetX, self._y-offsetY))

        if(self._showAttackRange or self._selected):
            screen.blit(self._attackRangeSurface, ((self._x+self._size/2)-self._attackRange,(self._y+self._size/2)-self._attackRange))
        
        #if(self._selected):
            #pygame.draw.circle(screen, (250,250,250), (self._x+self._size/2, self._y+self._size/2), self._size, width=3)

    def setCurrentAnim(self, anim):
        self._currentAnim = anim
        self._currentAnim.start()

    def removeTargetIfNotInRange(self):
        dist = math.hypot(self._x-self._targetBalloon.getX(), self._y-self._targetBalloon.getY())
        if(dist > self._attackRange+self._targetBalloon.getSize()):
            self._targetBalloon = None

    def setTargetBallon(self, balloons):
        if(self._searchForNearestBallon == False): return
        if(self._targetBalloon != None): return

        nearestBalloon = None
        nearestDist = 10000
        for balloon in balloons:
            dist = math.hypot(self._x-balloon.getX(), self._y-balloon.getY())
            if(dist < nearestDist and dist < self._attackRange+balloon.getSize()):
                nearestDist = dist
                nearestBalloon = balloon

        self._targetBalloon = nearestBalloon
    
    def addUpgrade(self, upgrade):
        self._upgrades.append(upgrade)
    def getUpgrades(self):
        return self._upgrades
    def showAttackRange(self, tof):
        self._showAttackRange = tof
    def setCanAttack(self, tof):
        self._canAttack = tof
    def getName(self):
        return self._name
    def getImage(self):
        return self._spriteSheet.getImage(0,0)
    def setSelected(self, tof):
        self._selected = tof
    def isUse(self):
        return self._use

    def create(self, x, y):
        return None

