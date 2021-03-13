from games.Bloons.entity import Defender, CannonBall
from games.Bloons.utils import Assets
from games.Bloons.upgrades import RangeUpgrade

class Cannon(Defender.Defender):

    def __init__(self, x, y, use=True):
        super().__init__(x, y, 42*2, "Cannon", Assets.cannonSheet, 80, 1600, 200, CannonBall.CannonBall(0,0,None,use=False), use=use)
        
        self._searchForNearestBallon = True

        self.addUpgrade(RangeUpgrade.RangeUpgrade(Assets.monkeyUpgrades.getImage(0,0), ["10% längre räckvidd.", "20% längre räckvidd.", "30% längre räckvidd."], [150, 300, 600], [[1.1, 1.2, 1.3]]))
        self.addUpgrade(RangeUpgrade.RangeUpgrade(Assets.monkeyUpgrades.getImage(0,0), ["10% längre räckvidd.", "20% längre räckvidd.", "30% längre räckvidd."], [150, 300, 600], [[1.1, 1.2, 1.3]]))


    def update(self, screen):
        if(self._use == False): return

        super().update(screen)

        if(self._targetBalloon != None):
            self.removeTargetIfNotInRange()

    def create(self, x, y):
        return Cannon(x, y) 