from games.Escape.objects import Creature
from games.Escape.utils import Assets, Handler

class RocketBroken(Creature.Creature):

    def __init__(self, tileX, tileY):
        super().__init__(-1, Assets.rocketBroken, tileX, tileY)

    def update(self, screen):
        super().update(screen)

        screen.blit(self._image, (self._x - Handler.gameCamera.getXOffset(), self._y - Handler.gameCamera.getYOffset()))
    
    def show(self, tof):
        super().show(tof)