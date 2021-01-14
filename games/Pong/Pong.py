import pygame
from libs.SimpleArcade import Game
import os

class Pong(Game.Game):
    
    def __init__(self):
        super().__init__("Pong", pygame.image.load("games/FlappyBird/images/logo.png"))

    def onPlay(self):
        super().onPlay()

    def update(self, screen):
        super().update(screen)