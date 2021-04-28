import pygame
from games.SpaceInvaders.assets import SpaceShip, Handler, Laser

class Enemy(SpaceShip.SpaceShip):
    COLOR_MAP = {
        "red" : (Handler.RED_SPACE_SHIP, Handler.RED_LASER),
        "green" : (Handler.GREEN_SPACE_SHIP, Handler.GREEN_LASER),
        "blue" : (Handler.BLUE_SPACE_SHIP, Handler.BLUE_LASER)
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
        Handler.enemies.append(self)
        self.color = color

    def shoot(self):
        if (self.cooldown_time == 0 and self.timer.isDone()):
            if(self.color == "blue"):
                self.laser = Laser.Laser(self.x - self.ship_img.get_width()/2, self.y, self.laser_img)
            else:
                self.laser = Laser.Laser(self.x - 15, self.y - 10, self.laser_img)
            self.lasers.append(self.laser)
            self.timer.start()
            self.cooldown_time = 1

    def move(self, vel):
        self.y += vel

    