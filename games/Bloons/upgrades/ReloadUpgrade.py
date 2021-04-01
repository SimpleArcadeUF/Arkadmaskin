from games.Bloons.upgrades import Upgrade

class ReloadUpgrade(Upgrade.Upgrade):

    def __init__(self, image, costs, speeds):
        super().__init__("Laddningtid", image, costs)

        self._speeds = speeds

    def getReloadBonus(self):
        return self._speeds[self._tier]