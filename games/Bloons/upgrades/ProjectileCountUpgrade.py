from games.Bloons.upgrades import Upgrade

class ProjectileCountUpgrade(Upgrade.Upgrade):

    def __init__(self, image, costs, counts):
        super().__init__("Flera skott", image, costs)

        self._counts = counts

    def getCountBonus(self):
        return self._counts[self._tier]