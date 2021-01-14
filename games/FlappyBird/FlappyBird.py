import pygame
import os
from libs.SimpleArcade import Game
from libs.SimpleArcade import Arcade

class FlappyBird(Game.Game):
    
    def __init__(self):
        super().__init__("Flappy Bird", pygame.image.load("games/FlappyBird/images/logo.png"))

    def onPlay(self):
        super().onPlay()
        print("Playyyyyyyyyyyy")
        

    def update(self, screen):
        super().update(screen)