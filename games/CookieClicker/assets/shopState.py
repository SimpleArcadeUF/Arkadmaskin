import pygame
from games.CookieClicker.assets import state, handler
from libs.SimpleArcade import Arcade
from libs.SimpleArcade.gui import Label
from libs.SimpleArcade.gui import Button

class ShopState:
    def __init__(self):
        super().__init__()

        self.PerClickUpgrade = Button.Button(x = 20, y = 20, width = 200, height = 80)
        self.PerClickUpgrade.addText("Clickier clicks!", Arcade.FONT, (0, 0, 0), 24)
        self.PerClickUpgrade.addBorder(2, (0, 0, 0))
        self.PerClickUpgrade.addHighlightedBorder(Arcade.RED)

        self.CookiePerSecond = Button.Button(x = 20, y = 120, width = 200, height = 80)
        self.CookiePerSecond.addText("Auto clicker!", Arcade.FONT, (0, 0, 0), 24)
        self.CookiePerSecond.addBorder(2, (0, 0, 0))
        self.CookiePerSecond.addHighlightedBorder(Arcade.RED)

    def onShow(self):
        Arcade.setSelectedGUI(self.PerClickUpgrade)
        self.Labels()

    def update(self, screen):
        self.render(screen) 
        self.gui(screen)
        self.goBack()

    def goBack(self):
        if (Arcade.BUTTON_PRESSED_2):
            handler.setCurrentState(handler.gameState)

    def render(self, screen):
        screen.fill((200, 200, 200))

    def gui(self, screen):
        self.PerClickUpgrade.update(screen)
        self.CPCLabel.update(screen)
        if (self.PerClickUpgrade.isClicked()):
            if (handler.cookies >= handler.cookiesPerClickPrice):
                handler.cookiesPerClick = handler.cookiesPerClick * 2
                handler.cookies -= handler.cookiesPerClickPrice
                handler.cookiesPerClickPrice = handler.cookiesPerClickPrice * 2
                self.Labels()
        
        self.CookiePerSecond.update(screen)
        self.CPSLabel.update(screen)
        if (self.CookiePerSecond.isClicked()):
            if (handler.cookies >= handler.cookiesPerSecondsPrice):
                if (handler.cookiesPerSeconds == 0):
                    handler.cookiesPerSeconds = 1
                else:
                    handler.cookiesPerSeconds = handler.cookiesPerSeconds * 2 
                handler.cookies -= handler.cookiesPerSecondsPrice
                handler.cookiesPerSecondsPrice = handler.cookiesPerSecondsPrice * 2
                self.Labels()

        self.PerClickUpgrade.setNeighbors(None, self.CookiePerSecond, None, None)
        self.CookiePerSecond.setNeighbors(self.PerClickUpgrade, None, None, None)

    def Labels(self):
        self.CPCLabel = Label.Label(x=250,y=40)
        self.CPCLabel.addText(f"{handler.cookiesPerClickPrice} : cookies", Arcade.FONT, "black", 32)

        self.CPSLabel = Label.Label(x=250,y=150)
        self.CPSLabel.addText(f"{handler.cookiesPerSecondsPrice} : cookies", Arcade.FONT, "black", 32)
        