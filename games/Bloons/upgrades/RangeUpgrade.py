from games.Bloons.upgrades import Upgrade

class RangeUpgrade(Upgrade.Upgrade):

    def __init__(self, image, costs, ranges):
        super().__init__("Räckvidd", image, costs)

        self._ranges = ranges

    def getRangeBonus(self):
        return self._ranges[self._tier]