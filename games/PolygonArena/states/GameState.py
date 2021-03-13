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
        self.game_over = False

        
        self.player_sprite = classes.Player((300, 300))
        self.player_group = pygame.sprite.Group(self.player_sprite)

        enemy_list = []
        for i in range(0, 0):
            enemy_sprite = classes.Enemy((random.randint(0,800), random.randint(0,800)))
            enemy_list.append(enemy_sprite)
        self.enemy_group = pygame.sprite.Group(enemy_list)

        self.font = pygame.font.Font('freesansbold.ttf', 32)


    def update(self, screen):

        screen.fill((30, 30, 30)) 

        self.time_label = Label.Label(x=0,y=5)
        self.time_label.alignHorizontally(None, Arcade.ALIGN_RIGHT, offset=-10)
        self.time_label.addText(str(int(self.timer/1000)), Arcade.FONT, Arcade.WHITE, 32)

        if self.game_over == False:

            #timer
            self.timer = (time.time() - self.game_called) * 1000

            #update
            self.player_group.update()
            self.enemy_group.update(self.player_sprite)
            self.player_sprite.update_player_gui(screen)
            self.time_label.update(screen)

            #draw
            self.player_group.draw(screen)
            self.enemy_group.draw(screen)


        #game over screen
        if self.game_over == True:
            game_over_screen = self.font.render("Game Over", True, (255, 255, 255))
            screen.blit(game_over_screen, (300, 350))


    

