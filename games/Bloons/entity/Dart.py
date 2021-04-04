from games.Bloons.entity import Projectile
from games.Bloons.utils import Assets

class Dart(Projectile.Projectile):

    def __init__(self, x, y, balloon, angle=0, use=True):
        super().__init__(Assets.dart, 12, x, y, balloon, 3, angle=angle, use=use)

        self._id = 2

    def update(self, screen, balloons):
        if(self._use == False): return

        super().update(screen, balloons)

    def create(self, x, y, balloon, angle=0):
        return Dart(x, y, balloon, angle=angle)