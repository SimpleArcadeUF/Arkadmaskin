from games.Bloons.entity import Projectile
from games.Bloons.utils import Assets

class Dart(Projectile.Projectile):

    def __init__(self, x, y, balloon, health):
        super().__init__(Assets.dart, 12, x, y, balloon, health)

    def update(self, screen):
        super().update(screen)