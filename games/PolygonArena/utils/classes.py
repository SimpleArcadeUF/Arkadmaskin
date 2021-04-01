from libs.SimpleArcade.gui import Label, Button, Frame
from libs.SimpleArcade import Game, Arcade

import random, time, sqlite3, math
import pygame, pygame.freetype 
from pygame.math import Vector2


class Player(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((50, 30), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, pygame.Color(Arcade.STEELBLUE2), [(0, 0), (50, 15), (0, 30)])
        self.orig_image = self.image  # Store a reference to the original.
        self.rect = self.image.get_rect(center=pos)
        self.pos = Vector2(pos)

        self.left_click = False
        self.right_click = False

        self.p_hp = 1
        self.p_dmg = 2
        self.p_vel = 4
        self.kill_counter = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)


    def update(self):
        global kill_counter
        self.rotate()
        key = pygame.key.get_pressed()
        mouse_button = pygame.mouse.get_pressed()

        #Key input
        if key[pygame.K_w]:
            self.rect[1] += -self.p_vel  #flyttar spelaren 3, 4 eller 6 frames
        if key[pygame.K_a]:
            self.rect[0] += -self.p_vel
        if key[pygame.K_s]:
            self.rect[1] += self.p_vel
        if key[pygame.K_d]:
            self.rect[0] += self.p_vel

        #Mouse input
        if mouse_button[0]:
            if self.left_click == False:
                self.kill_counter += 1
                self.left_click = True
        else: 
            self.left_click = False
           
        if mouse_button[2]:
            if self.right_click == False:
                print("right")
                self.right_click = True
        else:
            self.right_click = False
            

        #Collision with edge of map    
        if self.rect[0] <= 0:                           
            self.rect[0] = 0
        if self.rect[0] >= Arcade.SCREEN_WIDTH - self.rect[2]: 
            self.rect[0] = Arcade.SCREEN_WIDTH - self.rect[2]
        if self.rect[1] <= 0:                           
            self.rect[1] = 0
        if self.rect[1] >= Arcade.SCREEN_HEIGHT - self.rect[3]: 
            self.rect[1] = Arcade.SCREEN_HEIGHT - self.rect[3]


    def rotate(self):
        #print(self.pos)
        #print(direction)
        direction = pygame.mouse.get_pos() - Vector2(self.rect[0]+self.rect[2]/2, 
                                                     self.rect[1]+self.rect[2]/2)   #Positionen av musen från mitten av polygonen
        radius, angle = direction.as_polar()                                        #as_polar ger koordinaterna av vectorn från polarna
        self.image = pygame.transform.rotate(self.orig_image, -angle)               #roterar bilden mot musen
        self.rect = self.image.get_rect(center=self.rect.center)                    #Skapa en ny rect i centern av den gamla
    

    def update_player_gui(self, screen):

        life_gui = self.font.render("Life : " + str(self.p_hp), True, (255, 255, 255))
        screen.blit(life_gui, (10, 10))

        # self.life_label = Label.Label(x=0,y=0)
        # self.life_label.alignHorizontally(None, Arcade.ALIGN_LEFT)
        # self.life_label.alignVertically(None, Arcade.ALIGN_CENTER)
        # self.life_label.addText('Life : '+str(self.p_hp), Arcade.FONT, Arcade.LIGHT_BLACK_OFF, 32)

        self.kill_label = Label.Label(x=0,y=0)
        self.kill_label.alignHorizontally(None, Arcade.ALIGN_CENTER)
        self.kill_label.alignVertically(None, Arcade.ALIGN_CENTER)
        self.kill_label.addText(str(self.kill_counter), Arcade.FONT, Arcade.LIGHT_BLACK_OFF, 175)

        
        # self.life_label.update(screen)
        self.kill_label.update(screen)


                



class Enemy(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((50, 30), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, pygame.Color(Arcade.RED), [(0, 0), (50, 15), (0, 30)])
        self.orig_image = self.image  # Store a reference to the original.
        self.rect = self.image.get_rect(center=pos)
        self.pos = Vector2(pos)
        self.speed = 3


    def move(self, player_sprite):
        global p_hp, game_over
        if abs(player_sprite.rect[0] - self.rect.x) > 35 or abs(player_sprite.rect[1] - self.rect.y) > 35:
            dirvect = pygame.math.Vector2(player_sprite.rect[0] - self.rect.x,
                                    player_sprite.rect[1] - self.rect.y)
            dirvect.normalize()
            dirvect.scale_to_length(self.speed)
            self.rect.move_ip(dirvect)
        else:
            if self.p_hp > 0:
                self.p_hp -= 1 
            elif self.p_hp <= 0:
                self.game_over = True


    def update(self, player_sprite):
        self.move(player_sprite)
        self.rotate(player_sprite)


    def rotate(self, player_sprite):
        player_position = pygame.math.Vector2(player_sprite.rect[0] - self.rect.x,
                                              player_sprite.rect[1] - self.rect.y)  #Positionen av spelaren från mitten av polygonen
        radius, angle = player_position.as_polar()                                  #as_polar ger koordinaterna av vectorn från polarna   
        self.image = pygame.transform.rotate(self.orig_image, -angle)               #roterar bilden mot spelaren
        self.rect = self.image.get_rect(center=self.rect.center)                    #Skapa en ny rect i centern av den gamla                
