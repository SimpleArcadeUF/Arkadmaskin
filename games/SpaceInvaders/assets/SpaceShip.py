import pygame
from games.SpaceInvaders.assets import Laser
from libs.SimpleArcade import Timer, Arcade

class SpaceShip():
    def __init__(self, x, y, health = 100):
        super().__init__()
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cooldown_time = 0
        self.timer = Timer.Timer(200)
        self.timer.start()

    def update(self, screen):
        screen.blit(self.ship_img, (self.x, self.y))
        self.timer.update()
        self.cooldown()

        for laser in self.lasers:
            laser.update(screen)

    def moveLasers(self, vel, obj):
        for laser in self.lasers:
            laser.movement(vel)
            if (laser.offScreen()):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def getWidth(self):
        return self.ship_img.get_width()

    def getHeight(self):
        return self.ship_img.get_height()

    def shoot(self):
        if (self.cooldown_time == 0 and self.timer.isDone()):
            self.laser = Laser.Laser(self.x, self.y, self.laser_img)
            self.lasers.append(self.laser)
            self.timer.start()
            self.cooldown_time = 1
    
    def cooldown(self):
        if (self.timer.isDone()):
            self.cooldown_time = 0



            
