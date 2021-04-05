from libs.SimpleArcade.gui import Label, Button, Frame
from libs.SimpleArcade import Game, Arcade
from games.PolygonArena.utils import Handler, classes

import random, time, sqlite3, math
import pygame, pygame.freetype 
from pygame.math import Vector2


class Player(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.player_color = 92,172,238
        self.image = pygame.Surface((50, 30), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, pygame.Color(self.player_color), [(0, 0), (50, 15), (0, 30)])
        self.orig_image = self.image  # Store a reference to the original.
        self.rect = self.image.get_rect(center=pos)
        self.pos = Vector2(pos)
        self.direction = Vector2(1, 0)
    
        self.angle = 0
        self.orig_angle = 0
        self.p_hp = 1
        self.p_dmg = 2
        self.p_vel = 4
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        # self.x = Arcade.SCREEN_WIDTH//2
        # self.y = Arcade.SCREEN_HEIGHT//2
        # self.cosine = math.cos(math.radians(self.angle + 90))
        # self.sine = math.sin(math.radians(self.angle + 90))
        # self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2)


    def update(self):
        global kill_counter
        self.rotate()
        key = pygame.key.get_pressed()
        mouse_button = pygame.mouse.get_pressed()
    
        if Arcade._JOYSTICK_UP:
            angle = math.radians(self.angle)
            self.rect[0] += self.p_vel * math.cos(angle)
            self.rect[1] += self.p_vel * math.sin(angle)

        #Mouse input
        if Arcade._BUTTON_1:
            pass
        if Arcade._BUTTON_2:
            Handler.kill_counter += 1
            #self.player_color += 1
            self.shoot()
        if Arcade._BUTTON_3:
            self.angle -= 5
        if Arcade._BUTTON_4:
            self.angle += 5
        
            
        #Collision with edge of map    
        if self.rect[0] >= Arcade.SCREEN_WIDTH:
            self.rect[0] = 1 
        if self.rect[0] <= 0 - self.rect[2]: 
            self.rect[0] = Arcade.SCREEN_WIDTH 
        if self.rect[1] >= Arcade.SCREEN_HEIGHT:
            self.rect[1] = 1
        if self.rect[1] <= 0 - self.rect[3]: 
            self.rect[1] = Arcade.SCREEN_HEIGHT


    def rotate(self):
        if self.angle != 0:
            self.direction.rotate_ip(self.angle)
            self.image = pygame.transform.rotate(self.orig_image, -self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)

    # def rotate(self):
    #     #print(self.pos)
    #     #print(direction)
    #     direction = pygame.mouse.get_pos() - Vector2(self.rect[0]+self.rect[2]/2, 
    #                                                  self.rect[1]+self.rect[2]/2)   #Positionen av musen från mitten av polygonen
    #     radius, angle = direction.as_polar()                                        #as_polar ger koordinaterna av vectorn från polarna
    #     self.image = pygame.transform.rotate(self.orig_image, -angle)               #roterar bilden mot musen
    #     self.rect = self.image.get_rect(center=self.rect.center)                    #Skapa en ny rect i centern av den gamla
    

    def update_player_gui(self, screen):
        self.kill_label = Label.Label(x=0,y=0)
        self.kill_label.alignHorizontally(None, Arcade.ALIGN_CENTER)
        self.kill_label.alignVertically(None, Arcade.ALIGN_CENTER)
        self.kill_label.addText(str(Handler.kill_counter), Arcade.FONT, Arcade.LIGHT_BLACK_OFF, 175)

        self.kill_label.update(screen)
    

    def shoot(self):
        bullet = Bullet((self.rect[0],self.rect[1]))
        Handler.all_sprites.add(bullet)
        Handler.bullets.add(bullet)



class Bullet(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        pygame.draw.rect(self.image, Arcade.GUI_COLOR_BLUE, (0,10,0,20))
        self.rect = self.image.get_rect(center=pos)
        self.orig_image = self.image
        self.pos = Vector2(pos)
        self.speed = 10
        direction = pygame.mouse.get_pos() - Vector2(self.rect[0]+self.rect[2]/2, self.rect[1]+self.rect[2]/2) 
        angle = math.atan2(direction[1],direction[0]) #get angle to target in radians
        self.dx = math.cos(angle)*self.speed
        self.dy = math.sin(angle)*self.speed
        
        
    def move(self):
        self.x = self.rect.x + self.dx
        self.y = self.rect.y + self.dy
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        if self.rect.bottom < 0:
            print("yo")
            self.kill()

    
    def rotate(self):
        player_position = pygame.math.Vector2(self.rect[0] - (self.rect.x + self.dx), self.rect[1] - (self.rect.y + self.dy))  
        radius, angle = player_position.as_polar()                                  
        image = pygame.transform.rotate(self.image, -angle)               
        self.rect = image.get_rect(center=self.rect.center)                    


    def update(self, screen):
        screen.blit(self.image, (self.rect[0], self.rect[1]))
        self.move()
        self.rotate()        



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
            if player_sprite.p_hp > 0:
                player_sprite.p_hp -= 1 
            elif player_sprite.p_hp <= 0:
                Handler.game_over = True


    def update(self, player_sprite):
        self.move(player_sprite)
        self.rotate(player_sprite)


    def rotate(self, player_sprite):
        player_position = pygame.math.Vector2(player_sprite.rect[0] - self.rect.x,
                                              player_sprite.rect[1] - self.rect.y)  #Positionen av spelaren från mitten av polygonen
        radius, angle = player_position.as_polar()                                  #as_polar ger koordinaterna av vectorn från polarna   
        self.image = pygame.transform.rotate(self.orig_image, -angle)               #roterar bilden mot spelaren
        self.rect = self.image.get_rect(center=self.rect.center)                    #Skapa en ny rect i centern av den gamla                

