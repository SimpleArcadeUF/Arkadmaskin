import pygame
from libs.SimpleArcade import Arcade
from games.SpaceInvaders.assets import SpaceShip, Handler

class Player(SpaceShip.SpaceShip):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = Handler.YELLOW_SPACE_SHIP
        self.laser_img = Handler.YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.maxHealth = health
        self.movementSpeed = 7.5
        self.canShoot = True

    def update(self, screen):
        self.movement()
        self.logics()
        self.healthbar(screen)
        return super().update(screen)

    def logics(self):
        if (Handler.lives <= 0 or self.health <= 0):
            Handler.lost = True

        if (Arcade.BUTTON_PRESSED_1 and self.canShoot):
            self.shoot()

    def moveLasers(self, vel, objs):
        for laser in self.lasers:
            laser.movement(-vel)
            if (laser.offScreen()):
                self.lasers.remove(laser)
            else: 
                for obj in objs:
                    if (laser.collision(obj)):
                        objs.remove(obj)
                        self.lasers.remove(laser)

    def healthbar(self, screen):
        pygame.draw.rect(screen, (Arcade.RED), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(screen, (Arcade.GREEN), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (1 - (self.maxHealth - self.health)/self.maxHealth), 10))

    def movement(self):
        if (Arcade._JOYSTICK_LEFT and self.x != 0):
            self.x -= self.movementSpeed
        elif (Arcade._JOYSTICK_RIGHT and self.x != Arcade.SCREEN_WIDTH - self.getWidth()):
            self.x += self.movementSpeed

        # if (Arcade._JOYSTICK_UP and self.y != 0):
        #     self.y -= self.movementSpeed
        # elif (Arcade._JOYSTICK_DOWN and self.y != Arcade.SCREEN_HEIGHT - self.getHeight()):
        #     self.y += self.movementSpeed

    