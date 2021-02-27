from games.Bloons.entity import Defender

class Monkey(Defender.Defender):

    def __init__(self, x, y):
        super().__init__(x,y, 15, (165,42,42), 100)

        self._searchForNearestBallon = True

    def update(self, screen):
        super().update(screen)

        if(self._targetBalloon != None):
            self._targetBalloon.setColor((100, 20, 200))

            self.removeTargetIfNotInRange()