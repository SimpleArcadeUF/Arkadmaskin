import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((50, 50), (pygame.SRCALPHA), pygame.Rect(30, 30, 60, 60))
        self.orig_image = self.image 
    
    
    def update(self):
        pygame.draw.rect(self.orig_image, pygame.Color("red"))