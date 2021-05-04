import math

from libs.SimpleArcade import Animation, Arcade

from games.Bloons.entity import Defender, Dart
from games.Bloons.utils import Assets
from games.Bloons.upgrades import RangeUpgrade, ProjectileHealthUpgrade, ProjectileCountUpgrade

class IceMonkey(Defender.Defender):

    def __init__(self, x, y, use=True):
        super().__init__(x,y, 40, "Is apa", Assets.iceMonkeySheet, 60, 2000, 300, None, use=use)

        self._searchForNearestBallon = True

        self._startAttackRange = self._attackRange
        self._iceAnim = Animation.Animation(Assets.iceMonkeyAttackSheet.getImagesByRow(0), 700, continuous=False)

        self.addUpgrade(RangeUpgrade.RangeUpgrade(Assets.monkeyUpgrades.getImage(0,0), [150, 300, 600], [1, 1.1, 1.2, 1.3]))

    def update(self, screen, balloons): 
        if(self._use == False): return

        super().update(screen, balloons)

        self._attackRange = int(self._startAttackRange * self._upgrades[0].getRangeBonus())

        if(self._targetBalloon != None):
            self.removeTargetIfNotInRange()

        self._iceAnim.update()
        if(self._onFire):
            self._iceAnim.start()
        if(self._iceAnim.isStarted()):
            screen.blit(self._iceAnim.getCurrentFrame(), (self._x+self._size/2 - self._iceAnim.getCurrentFrame(0).get_width()/2, self._y+self._size/2 - self._iceAnim.getCurrentFrame(0).get_height()/2))
        
        if(self._iceAnim.isDone()):
            self._iceAnim.reset()
            for balloon in balloons:
                currentDistance = Arcade.getDistance((self._x+self._size/2,self._y+self._size/2), (balloon.getX()+balloon.getSize()/2,balloon.getY()+balloon.getSize()/2))
                if(currentDistance < self._attackRange*2):
                    balloon.hit(createNextFrozen=True)

    def create(self, x, y):
        return IceMonkey(x, y) 