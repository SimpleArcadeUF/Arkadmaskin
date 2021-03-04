import math, pygame

from games.Bloons.entity import Entity
from games.Bloons.utils import Handler

PROJECTILES = []

class Projectile(Entity.Entity):
    
    def __init__(self, image, speed, x, y, balloon, health):
        super().__init__(x, y, 1, draw=False, color=None)

        self._image = image
        self._speed = speed
        self._width = image.get_width()
        self._height = image.get_height()
        self._projectileHealth = health

        self._dir = math.atan2((y+self._height/2)-(balloon.getY()+balloon.getSize()/2), (x+self._width/2)-(balloon.getX()+balloon.getSize()/2)) + math.radians(180)
        self._xVel = math.cos(self._dir) * self._speed
        self._yVel = math.sin(self._dir) * self._speed
        self._collisionDistance = math.dist((x+self._width/2,y+self._height/2), (balloon.getX()+balloon.getSize()/2,balloon.getY()+balloon.getSize()/2))

        self._x += self._xVel * 2
        self._y += self._yVel * 2

        self._image = pygame.transform.rotate(self._image, -(math.degrees(self._dir)+90))
        self._rect = self._image.get_rect(center=image.get_rect(center=(self._x, self._y)).center)

        PROJECTILES.append(self)

    def update(self, screen):
        super().update(screen)
        
        self._x += self._xVel * Handler.GAME_SPEED
        self._y += self._yVel * Handler.GAME_SPEED

        screen.blit(self._image, (self._x - (self._rect[2]/2 - self._width/2), self._y - (self._rect[3]/2 - self._height/2)))
    
    def updateCollision(self, balloons):
        for balloon in balloons:
            currentDistance = math.dist((self._x+self._width/2,self._y+self._height/2), (balloon.getX()+balloon.getSize()/2,balloon.getY()+balloon.getSize()/2))

            if(currentDistance < balloon.getSize()/2):
                balloon.hit(self)
                self._projectileHealth -= 1

                if(self._projectileHealth == 0):
                    PROJECTILES.remove(self)