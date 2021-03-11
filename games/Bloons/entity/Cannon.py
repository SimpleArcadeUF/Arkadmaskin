from games.Bloons.entity import Defender, CannonBall
from games.Bloons.utils import Assets

class Cannon(Defender.Defender):

    def __init__(self, x, y, use=True):
        super().__init__(x, y, 42*2, "Cannon", Assets.cannonSheet, 80, 1600, 200, CannonBall.CannonBall(0,0,None,use=False), use=use)
        
        self._searchForNearestBallon = True

    def update(self, screen):
        if(self._use == False): return

        super().update(screen)

        if(self._targetBalloon != None):
            self.removeTargetIfNotInRange()

    def create(self, x, y):
        return Cannon(x, y) 