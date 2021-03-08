from games.Bloons.entity import Defender, Dart
from games.Bloons.utils import Assets

class Monkey(Defender.Defender):

    def __init__(self, x, y, use=True):
        super().__init__(x,y, 40, "Monkey", Assets.monkeySheet, 100, 800, 300, Dart.Dart(0,0,None,use=False), use=use)

        self._searchForNearestBallon = True

    def update(self, screen):
        if(self._use == False): return

        super().update(screen)

        if(self._targetBalloon != None):
            self.removeTargetIfNotInRange()

    def create(self, x, y):
        return Monkey(x, y) 