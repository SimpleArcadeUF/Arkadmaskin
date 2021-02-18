from games.Escape.objects import Creature
from games.Escape.utils import Assets, Handler

class Rocket(Creature.Creature):

    def __init__(self, tileX, tileY):
        super().__init__(-1, Assets.rocket, tileX, tileY)

        self._collisionBox = [0, 0, 36*Handler.IMAGE_SCALE, 55*Handler.IMAGE_SCALE]

    def update(self, screen):
        super().update(screen)

        screen.blit(self._image, (self._x - Handler.gameCamera.getXOffset(), self._y - Handler.gameCamera.getYOffset()))

    def show(self, tof):
        super().show(tof)