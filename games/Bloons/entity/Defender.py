import math, pygame

from games.Bloons.entity import Entity

class Defender(Entity.Entity):

    def __init__(self, x, y, size, color, attackRange):
        super().__init__(x, y, size, color=color, draw=True)

        self._attackRange = attackRange
        self._showAttackRange = True
        self._attackRangeSurface = pygame.Surface((self._attackRange*2, self._attackRange*2))
        self._attackRangeSurface.set_colorkey((0,0,0))
        self._attackRangeSurface.set_alpha(100)
        pygame.draw.circle(self._attackRangeSurface, (50,50,50), (self._attackRange,self._attackRange), self._attackRange)

        self._targetBalloon = None
        self._searchForNearestBallon = False

    def update(self, screen):
        super().update(screen)

        if(self._showAttackRange):
            screen.blit(self._attackRangeSurface, (self._x-self._attackRange,self._y-self._attackRange))

    def removeTargetIfNotInRange(self):
        dist = math.hypot(self._x-self._targetBalloon.getX(), self._y-self._targetBalloon.getY())
        if(dist > self._attackRange+self._targetBalloon.getSize()):
            self._targetBalloon = None

    def setTargetBallon(self, balloons):
        if(self._searchForNearestBallon == False): return
        if(self._targetBalloon != None): return

        nearestBalloon = None
        nearestDist = 10000
        for balloon in balloons:
            dist = math.hypot(self._x-balloon.getX(), self._y-balloon.getY())
            if(dist < nearestDist and dist < self._attackRange+balloon.getSize()):
                nearestDist = dist
                nearestBalloon = balloon

        self._targetBalloon = nearestBalloon

