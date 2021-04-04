from games.Bloons.entity import Defender, CannonBall
from games.Bloons.utils import Assets
from games.Bloons.upgrades import RangeUpgrade, ExplosionRangeUpgrade, ReloadUpgrade

class Cannon(Defender.Defender):

    def __init__(self, x, y, use=True):
        super().__init__(x, y, 42*2, "Kanon", Assets.cannonSheet, 80, 1400, 200, CannonBall.CannonBall(0,0,None,use=False), use=use)
        
        self._searchForNearestBallon = True
        self._startAttackRange = self._attackRange

        self.addUpgrade(RangeUpgrade.RangeUpgrade(Assets.cannonUpgrades.getImage(0,0), [200, 400, 900], [1, 1.2, 1.4, 1.6]))
        self.addUpgrade(ExplosionRangeUpgrade.ExplosionRangeUpgrade(Assets.cannonUpgrades.getImage(1,0), [300, 600, 900], [1, 1.2, 1.3, 1.5]))
        self.addUpgrade(ReloadUpgrade.ReloadUpgrade(Assets.cannonUpgrades.getImage(2,0), [500, 1000, 1300], [1, 0.8, 0.7, 0.5]))

    def update(self, screen, balloons):
        if(self._use == False): return

        super().update(screen, balloons)

        if(self._targetBalloon != None):
            self.removeTargetIfNotInRange()

        self._attackRange = int(self._startAttackRange * self._upgrades[0].getRangeBonus())
        self._attackWaitTimer.setSpeed(self._attackSpeed * self._upgrades[2].getReloadBonus())

        if(self._onFire):
            for projectile in self._firedProjectiles:
                projectile.addExplosionRangeBonus(self._upgrades[1].getRangeBonus())

    def create(self, x, y):
        return Cannon(x, y) 