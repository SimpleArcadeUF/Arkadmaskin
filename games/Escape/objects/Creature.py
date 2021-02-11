from games.Escape.objects import GameObject
from games.Escape.utils import Handler

CREATURES = []

class Creature(GameObject.GameObject):

    def __init__(self, order, image, tileX, tileY):
        super().__init__(GameObject.TAG_CREATURE, order, image.get_width(), image.get_height())

        self._image = image
        self._x = tileX * Handler.TILE_SIZE
        self._y = tileY * Handler.TILE_SIZE
        self._movementSpeed = 1
        self._dir = 1 # left = -1 & right = 1

        CREATURES.append(self)

    def update(self, screen):
        if(self._xVel < 0):
            self._dir = -1
        elif(self._xVel > 0):
            self._dir = 1

        super().update(screen)

        if(self._show == False): return
        
        #screen.blit(self._image, (self._x - Handler.gameCamera.getXOffset(), self._y - Handler.gameCamera.getYOffset()))

    def _collision(self):
        super()._collision()

        if(self._static == True or self._onScreen == False):
            return

        if(self._yVel != 0 or self._xVel != 0):
            for tile in Handler.gameState.getWorld().getTiles():
                if(tile.isOnScreen() and tile.getTileType().isSolid()):
                    
                    #Bottom
                    if(self._grounded == False):
                        if(self._yVel > 0 and self._y + self._collisionBox[1] + self._collisionBox[3] <= tile.getY()):
                            if(self._y + self._collisionBox[1] + self._collisionBox[3] + self._yVel > tile.getY() + tile.getCollisionBox()[1] and self._y + self._collisionBox[1] + self._collisionBox[3] <= tile.getY() + tile.getCollisionBox()[1]):
                                if(self._x + self._collisionBox[0] + self._collisionBox[2] > tile.getX() + tile.getCollisionBox()[0] and self._x + self._collisionBox[0] < tile.getX() + tile.getCollisionBox()[0] + tile.getCollisionBox()[2]):
                                    self._yVel = 0
                                    self._y = tile.getY() + tile.getCollisionBox()[1] - self._collisionBox[1] - self._collisionBox[3]
                                    self._grounded = True
                    #Top
                    if(self._yVel < 0 and self._y + self._collisionBox[1] >= tile.getY()):
                        if(self._y + self._collisionBox[1] + self._yVel < tile.getY() + tile.getCollisionBox()[1] + tile.getCollisionBox()[3] and self._y + self._collisionBox[1] >= tile.getY() + tile.getCollisionBox()[1] + tile.getCollisionBox()[3]):
                            if(self._x + self._collisionBox[0] + self._collisionBox[2] > tile.getX() + tile.getCollisionBox()[0] and self._x + self._collisionBox[0] < tile.getX() + tile.getCollisionBox()[0] + tile.getCollisionBox()[2]):
                                self._yVel = 0
                                self._y = tile.getY() + tile.getCollisionBox()[1] + tile.getCollisionBox()[3] - self._collisionBox[1]
                            
                    #Right
                    if(self._xVel > 0 and self._x <= tile.getX()):
                        if(self._x + self._collisionBox[0] + self._collisionBox[2] + self._xVel > tile.getX() + tile.getCollisionBox()[0] and self._x + self._collisionBox[0] + self._collisionBox[2] <= tile.getX() + tile.getCollisionBox()[0]):
                            if(self._y + self._collisionBox[1] + self._collisionBox[3] > tile.getY() + tile.getCollisionBox()[1] and self._y + self._collisionBox[1] < tile.getY() + tile.getCollisionBox()[1] + tile.getCollisionBox()[3]):
                                self._xVel = 0
                                self._x = tile.getX() + tile.getCollisionBox()[0] - self._collisionBox[0] - self._collisionBox[2]
                    
                    #Left nice
                    if(self._xVel < 0 and self._x >= tile.getX()):
                        if(self._x + self._collisionBox[0] + self._xVel < tile.getX() + tile.getCollisionBox()[0] + tile.getCollisionBox()[2] and self._x + self._collisionBox[0] >= tile.getX() + tile.getCollisionBox()[0] + tile.getCollisionBox()[2]):
                            if(self._y + self._collisionBox[1] + self._collisionBox[3] > tile.getY() + tile.getCollisionBox()[1] and self._y + self._collisionBox[1] < tile.getY() + tile.getCollisionBox()[1] + tile.getCollisionBox()[3]):
                                self._xVel = 0
                                self._x = tile.getX() + tile.getCollisionBox()[0] + tile.getCollisionBox()[2] - self._collisionBox[0]

    def show(self, tof):
        super().show(tof)