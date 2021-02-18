from libs.SimpleArcade import Arcade

class GameCamera():

    def __init__(self):
        self._followedCreature = None
        self._xOffset = 0
        self._yOffset = 0

    def update(self):
        if(self._followedCreature == None): return

        self._xOffset = self._followedCreature.getX() + self._followedCreature.getWidth() / 2 - Arcade.SCREEN_WIDTH / 2
        self._yOffset = self._followedCreature.getY() + self._followedCreature.getHeight() / 2 - Arcade.SCREEN_HEIGHT / 2

    def setFollowedCreature(self, creature):
        self._followedCreature = creature

    def getXOffset(self):
        return self._xOffset
    def getYOffset(self):
        return self._yOffset