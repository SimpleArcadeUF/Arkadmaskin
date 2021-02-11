from games.Escape.states import State
from games.Escape.objects import Tile, TileType, Player, Rocket, Creature, RocketBroken
from games.Escape.world import World, GameCamera
from games.Escape.utils import Handler

class GameState(State.State):

    def __init__(self):
        super().__init__()

        self._world = World.World()
        self._world.loadMap("games/Escape/res/maps/escape.txt")

        self._player = Player.Player(5, 2)
        #self._rocket = Rocket.Rocket(3, 0)
        self._rocketBroken = RocketBroken.RocketBroken(3, 0)

        Handler.gameCamera = GameCamera.GameCamera()
        Handler.gameCamera.setFollowedCreature(self._player)

    def update(self, screen):
        super().update(screen)

        screen.fill((40, 60, 255))

        self._world.update(screen)

        Handler.gameCamera.update()

    def show(self, tof):
        super().show(tof)
    
    def getWorld(self):
        return self._world