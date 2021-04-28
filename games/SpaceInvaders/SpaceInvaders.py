import pygame
from libs.SimpleArcade import Game, Arcade

from games.SpaceInvaders.assets import Handler, State, GameState, StartState

class SpaceInvaders(Game.Game):
    def __init__(self):
        super().__init__("SpaceInvaders", pygame.image.load("games/SpaceInvaders/res/img/logo.jpg"))

    def onPlay(self):
        Handler.gameState = GameState.GameState() 
        Handler.startState = StartState.StartState()
        Handler.setCurrentState(Handler.startState)
    
    def update(self, screen):
        Handler.currentState.update(screen)

        if (Handler.quit == True):
            self.quit()
            Handler.quit = False


