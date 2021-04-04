from games.Bloons.entity import Defender, Dart
from games.Bloons.utils import Assets
from games.Bloons.upgrades import RangeUpgrade, ProjectileHealthUpgrade, ProjectileCountUpgrade

class Monkey(Defender.Defender):

    def __init__(self, x, y, use=True):
        super().__init__(x,y, 40, "Apa", Assets.monkeySheet, 100, 800, 300, Dart.Dart(0,0,None,use=False), use=use)

        self._searchForNearestBallon = True
        self._startAttackRange = self._attackRange

        self.addUpgrade(RangeUpgrade.RangeUpgrade(Assets.monkeyUpgrades.getImage(0,0), [150, 300, 600], [1, 1.1, 1.2, 1.3]))
        self.addUpgrade(ProjectileHealthUpgrade.ProjectileHealthUpgrade(Assets.monkeyUpgrades.getImage(2,0), [400, 800, 1200], [0, 1, 2, 3]))
        self.addUpgrade(ProjectileCountUpgrade.ProjectileCountUpgrade(Assets.monkeyUpgrades.getImage(1,0), [600, 1200], [1, 2, 3]))

    def update(self, screen, balloons):
        if(self._use == False): return

        super().update(screen, balloons)

        if(self._targetBalloon != None):
            self.removeTargetIfNotInRange()

        self._attackRange = int(self._startAttackRange * self._upgrades[0].getRangeBonus())
        self._projectileHealthBonus = self._upgrades[1].getHealthBonus()
        self._fireCount = self._upgrades[2].getCountBonus()

    def create(self, x, y):
        return Monkey(x, y) 