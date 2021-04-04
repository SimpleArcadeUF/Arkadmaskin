
class Upgrade:

    def __init__(self, name, image, costs):
        self._name = name
        self._image = image
        self._costs = costs
        self._tier = 0
    
    def getInfo(self):
        return self._infos[self._tier]
    def nextTier(self):
        self._tier += 1
    def getCost(self):
        return self._costs[self._tier]
    def isMaxTier(self):
        return self._tier == self.getMaxTier()
    def getMaxTier(self):
        return len(self._costs)
    def getName(self):
        return self._name
    def getImage(self):
        return self._image
    def getTier(self):
        return self._tier