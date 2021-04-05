import pygame
from libs.SimpleArcade import Arcade

class Laser: 
    def __init__(self, x, y, img):
        super().__init__()
        self.x = x 
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
    
    def update(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def movement(self, vel):
        self.y += vel

    def offScreen(self):
        return not self.y <= Arcade.SCREEN_HEIGHT and self.y >= 0

    def collision(self, obj):
        return self.collide(obj)

    def collide(self, obj):
        offset_x = obj.x - self.x
        offset_y = obj.y - self.y 
        return self.mask.overlap(obj.mask, (int(offset_x), int(offset_y))) != None
