
import pygame 
import pygame.freetype
from pygame.math import Vector2

#other imports
import random
import time



class Player():

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('games/GeoDash/res/images/player_sprite.png').convert()
        #self.orig_image = self.image  # Store a reference to the original.
       
        # self.pos = Vector2(pos)

    
    # def update(self):
    #     global kill_counter
    #     self.rotate()
    #     key = pygame.key.get_pressed()
    #     mouse_button = pygame.mouse.get_pressed()
    #     if key[pygame.K_w]:
    #         self.rect[1] += -p_vel  #flyttar spelaren 3, 4 eller 6 frames
    #     if key[pygame.K_a]:
    #         self.rect[0] += -p_vel
    #     if key[pygame.K_s]:
    #         self.rect[1] += p_vel
    #     if key[pygame.K_d]:
    #         self.rect[0] += p_vel
    #     if mouse_button[0]:
    #         print("bang")
    #         kill_counter += 1
            
            
    #     if self.rect[0] <= 0:                           #checkar om spelaren nuddar vänstra sidan av fönstret
    #         self.rect[0] = 0
    #     if self.rect[0] >= screen_width - self.rect[2]: #checkar om spelaren nuddar högra sidan av fönstret
    #         self.rect[0] = screen_width - self.rect[2]
    #     if self.rect[1] <= 0:                           #checkar om spelaren nuddar toppen av fönstret
    #         self.rect[1] = 0
    #     if self.rect[1] >= screen_width - self.rect[3]: #checkar om spelaren nuddar botten sidan av fönstret
    #         self.rect[1] = screen_width - self.rect[3]

    # def rotate(self):
    #     #print(self.pos)
    #     #print(direction)
    #     direction = pygame.mouse.get_pos() - Vector2(self.rect[0]+self.rect[2]/2, 
    #                                                  self.rect[1]+self.rect[2]/2)   #Positionen av musen från mitten av polygonen
    #     radius, angle = direction.as_polar()                                        #as_polar ger koordinaterna av vectorn från polarna
    #     self.image = pygame.transform.rotate(self.orig_image, -angle)               #roterar bilden mot musen
    #     self.rect = self.image.get_rect(center=self.rect.center)                    #Skapa en ny rect i centern av den gamla
    