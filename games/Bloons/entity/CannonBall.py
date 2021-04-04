import math

from libs.SimpleArcade import Animation

from games.Bloons.entity import Projectile
from games.Bloons.utils import Assets

class CannonBall(Projectile.Projectile):

    def __init__(self, x, y, balloon, use=True):
        super().__init__(Assets.cannonBall, 12, x, y, balloon, 1, use=use)

        self._waitToRemove = True
        self._animExplosion = Animation.Animation(Assets.cannonBallExplosionSpriteSheet.getImagesByRow(0), 500, continuous=False)
        self._explosionRange = 35
        self._id = 1

    def update(self, screen, balloons):
        if(self._use == False): return

        if(self._hitRemove == True):
            self._animExplosion.start()
            self._hitRemove = False

            for balloon in balloons:
                currentDistance = math.dist((self._x+self._width/2,self._y+self._height/2), (balloon.getX()+balloon.getSize()/2,balloon.getY()+balloon.getSize()/2))
                if(currentDistance < self._explosionRange*2):
                    balloon.hit(self)

        if(self._animExplosion.isStarted()):
            self._animExplosion.update()
            screen.blit(self._animExplosion.getCurrentFrame(), (self._x - self._animExplosion.getCurrentFrame().get_width()/2, self._y - self._animExplosion.getCurrentFrame().get_height()/2))
        
        if(self._animExplosion.isDone()):
            Projectile.PROJECTILES.remove(self)

        if(self._update == False): return

        super().update(screen, balloons)

    def addExplosionRangeBonus(self, bonus):
        self._explosionRange *= bonus

    def create(self, x, y, balloon):
        return CannonBall(x, y, balloon) 