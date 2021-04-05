import pygame
from libs.SimpleArcade import Game
from games.Titanic import Handler, GameState, Assets

class Titanic(Game.Game):

    def __init__(self):
        super().__init__("TitanicDriver", (pygame.image.load("res/images/logo.png")))

    def onPlay(self):
        Assets.init()

        Handler.gameState = GameState.GameState()

        Handler.setState(Handler.gameState)

    def update(self, screen):
        Handler.currentState.update(screen)

        if(Handler.quit == True):
            self.quit()
            Handler.quit = False