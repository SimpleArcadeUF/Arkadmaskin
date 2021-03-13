
class Upgrade:

    def __init__(self, name, infos):
        self._name = name
        self._infos = infos
        self._tier = 0
        self._haveUpgrade = False
    
    def getInfo(self):
        return self._infos[self._tier]

    def nextTier(self):
        self._tier += 1