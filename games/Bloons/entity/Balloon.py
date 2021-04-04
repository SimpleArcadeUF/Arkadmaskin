import pygame

from games.Bloons.entity import Entity, Balloons
from games.Bloons.utils import Handler

class Balloon(Entity.Entity):

    def __init__(self, x, y, speed, image, balloon, rbe, nextBalloon, template=False, blastProtection=False):
        super().__init__(x, y, Handler.BALLOON_SIZE, draw=False)

        self._speed = speed
        self._image = image
        self._nextBalloon = nextBalloon
        self._template = template
        self._type = balloon
        self._rbe = rbe
        self._currentNodeIndex = 1
        self._delete = False
        self._currentNode = None
        self._immuneProjectile = None
        self._createNextBalloon = False
        self._hitProjectile = None
        self._blastProtection = blastProtection

    def update(self, screen):
        if(self._template == True):
            return

        super().update(screen)

        #pygame.draw.rect(screen, (0,0,0), (self._x, self._y, self._size, self._size))
        screen.blit(self._image, (self._x, self._y))
        #pygame.draw.circle(screen, self._color, (self._x, self._y), self._size)

    def move(self, path):
        self._currentNode = path[self._currentNodeIndex]

        dx = self._x + self._size/2 - self._currentNode.getX()
        dy = self._y + self._size/2 - self._currentNode.getY()            

        if(dx < 0):
            self._x += self._speed * Handler.GAME_SPEED
        if(dx > 0):
            self._x -= self._speed * Handler.GAME_SPEED
        if(dy < 0):
            self._y += self._speed * Handler.GAME_SPEED
        if(dy > 0):
            self._y -= self._speed * Handler.GAME_SPEED
        
        if(abs(dx) <= self._speed * Handler.GAME_SPEED and abs(dy) <= self._speed * Handler.GAME_SPEED):
            self._x = self._currentNode.getX() - self._size/2
            self._y = self._currentNode.getY() - self._size/2
            self._currentNodeIndex += 1
    
    def hit(self, projectile):
        if(self._blastProtection == True and projectile.getID() == 1):
            return

        if(self._immuneProjectile == projectile):
            return

        self.delete()
        self._hitProjectile = projectile
        if(self._nextBalloon != None):
            self._createNextBalloon = True

    def getCurrentNodeIndex(self):
        return self._currentNodeIndex
    def getRBE(self):
        return self._rbe
    def setColor(self, color):
        self._color = color
    def isDeleted(self):
        return self._delete
    def shouldCreateNextBalloon(self):
        return self._createNextBalloon
    def getNextBalloon(self):
        return self._nextBalloon
    def getHitProjectile(self):
        return self._hitProjectile
    def delete(self):
        self._delete = True
    def create(self, node):
        return Balloon(node.getX()-self._size/2,node.getY()-self._size/2, self._speed, self._image, self._type, self._rbe, self._nextBalloon, blastProtection=self._blastProtection)
    def createOnParent(self, balloon):
        b = Balloon(balloon._x, balloon._y, self._speed, self._image, self._type, self._rbe, self._nextBalloon, blastProtection=self._blastProtection) 
        b._currentNodeIndex = balloon._currentNodeIndex
        b._immuneProjectile = balloon._hitProjectile
        return b