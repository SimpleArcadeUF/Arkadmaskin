from games.Bloons.upgrades import Upgrade

class RangeUpgrade(Upgrade.Upgrade):

    def __init__(self, image, infos, costs, ranges):
        super().__init__("Räckvidd", image, infos)

        self._costs = costs
        self._ranges = ranges

    def getRangeBonus(self):
        if(self._haveUpgrade == False): return 1
        return self._ranges[self._tier]

    def getCost(self):
        return self._costs[self._tier]