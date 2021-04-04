from games.Bloons.upgrades import Upgrade

class ProjectileHealthUpgrade(Upgrade.Upgrade):

    def __init__(self, image, costs, healths):
        super().__init__("Projektil liv", image, costs)

        self._healths = healths

    def getHealthBonus(self):
        return self._healths[self._tier]