from games.PolygonArena.states import State 
from games.PolygonArena.utils import Handler, classes
# from games.PolygonArena.tileSystem import TileType, GeoPlayer
from libs.SimpleArcade.gui import Label, Button, Frame
from libs.SimpleArcade import Game, Arcade

import pygame, random, time

class GameState():

    def __init__(self):
        
        self.timer = 0
        self.game_called = time.time()
        
        self.player_sprite = classes.Player((300, 300))
        self.player_group = pygame.sprite.Group(self.player_sprite)
        
        enemy_list = []
        for i in range(0, 0):
            enemy_sprite = classes.Enemy((random.randint(0,Arcade.SCREEN_WIDTH), random.randint(0,Arcade.SCREEN_HEIGHT)))
            enemy_list.append(enemy_sprite)
        self.enemy_group = pygame.sprite.Group(enemy_list)

        self.font = pygame.font.Font('freesansbold.ttf', 32)


    def update(self, screen):

        screen.fill((30, 30, 30)) 

        self.time_label = Label.Label(x=0,y=5)
        self.time_label.alignHorizontally(None, Arcade.ALIGN_CENTER)
        self.time_label.alignVertically(None, Arcade.ALIGN_CENTER, offset=-180)
        self.time_label.addText(str(int(self.timer/1000)), Arcade.FONT, Arcade.LIGHT_BLACK_OFF, 36)

        # self.level_label = Label.Label(x=0,y=5)
        # self.level_label.alignHorizontally(None, Arcade.ALIGN_CENTER, offset=-90)
        # self.level_label.alignVertically(None, Arcade.ALIGN_CENTER, offset=90)
        # self.level_label.addText(str("1"), Arcade.FONT, Arcade.LIGHT_BLACK_OFF, 32)


        if Handler.game_over == False:

            #timer
            self.timer = (time.time() - self.game_called) * 1000

            #update
            self.player_group.update()
            self.enemy_group.update(self.player_sprite)
            self.player_sprite.update_player_gui(screen)
            self.time_label.update(screen)
            Handler.bullets.update(screen)
            # self.level_label.update(screen)
            
            
            #draw
            self.player_group.draw(screen)
            self.enemy_group.draw(screen)
            Handler.all_sprites.draw(screen)
           


        #game over screen
        if Handler.game_over == True:

            self.game_over_label = Label.Label(x=0,y=0)
            self.game_over_label.alignHorizontally(None, Arcade.ALIGN_CENTER)
            self.game_over_label.alignVertically(None, Arcade.ALIGN_CENTER, offset=-30)
            self.game_over_label.addText("Game Over", Arcade.FONT, Arcade.WHITE, 100)


            self.score_label = Label.Label(x=0,y=0)
            self.score_label.alignHorizontally(None, Arcade.ALIGN_CENTER)
            self.score_label.alignVertically(None, Arcade.ALIGN_CENTER, offset=40)
            self.score_label.addText("Score : "+str(int(Handler.kill_counter/((self.timer/1000)/100)+Handler.kill_counter)), Arcade.FONT, Arcade.WHITE, 32)
            

            self.image = pygame.Surface((600, 360), pygame.SRCALPHA)
            self.image_polygon = pygame.draw.polygon(self.image, pygame.Color(Arcade.STEELBLUE2), [(0,0),(600,180),(0,360)])
            self.rotated_image = pygame.transform.rotate(self.image, 5)

            self.bg_polygon = Frame.Frame(x=0,y=0, width=int(600*1.3), height=int(360*1.1))
            self.bg_polygon.alignHorizontally(None, Arcade.ALIGN_CENTER, offset=40)
            self.bg_polygon.alignVertically(None, Arcade.ALIGN_CENTER, offset=-10)
            self.bg_polygon.addImage(self.rotated_image)


            self.bg_polygon.update(screen)
            self.game_over_label.update(screen)
            self.score_label.update(screen)


    

