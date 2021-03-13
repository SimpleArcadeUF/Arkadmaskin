
class Upgrade:

    def __init__(self, name, image, infos):
        self._name = name
        self._image = image
        self._infos = infos
        self._tier = 0
        self._haveUpgrade = False
    
    def getInfo(self):
        return self._infos[self._tier]
    def nextTier(self):
        self._tier += 1
    def getName(self):
        return self._name
    def getImage(self):
        return self._image
    def getTier(self):
        return self._tier