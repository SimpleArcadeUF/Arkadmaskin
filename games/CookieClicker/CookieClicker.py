import pygame
from libs.SimpleArcade import Game, Arcade

from games.CookieClicker.assets import handler, state, gameState, shopState, save

class CookieClicker(Game.Game):
    
    def __init__(self):
        super().__init__("CookieCliker", (pygame.image.load("games/CookieClicker/res/img/CCLogo.jpg")))

    def onPlay(self):
        handler.gameState = gameState.GameState()
        handler.shopState = shopState.ShopState()
        handler.setCurrentState(handler.gameState)
        save.readSaveFile()
        
    def update(self, screen):
        handler.currentState.update(screen)
        handler.update()
        
        if (handler.quit == True):
            self.quit()
            save.writeSave()
            handler.quit = False