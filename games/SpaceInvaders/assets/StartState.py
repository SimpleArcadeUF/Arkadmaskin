import pygame
from games.SpaceInvaders.assets import Handler
from libs.SimpleArcade.gui import Label, Button
from libs.SimpleArcade import Arcade, Timer

class StartState():
    def __init__(self):
        super().__init__()

    def onShow(self):
        self.LOGOFONT = 56
        self.LOGOFONTDIRECTION = 0
        self.initGUI()
        self.BG = pygame.image.load("games/SpaceInvaders/res/img/background-black.png")
        self.timer = Timer.Timer(50)
        self.timer.start()

    def update(self, screen):
        self.updateGUI(screen)
        self.resizeLogo()
        self.timer.update()

    def resizeLogo(self):
        self.SpaceInvadersLogo.addText("Space Invaders", Arcade.FONT, Arcade.GUI_COLOR_ORANGE, self.LOGOFONT)
        if(self.timer.isDone()):
            if (self.LOGOFONTDIRECTION == 0):
                if (self.LOGOFONT <= 56):
                    self.LOGOFONTDIRECTION = 1
                self.LOGOFONT -= 1
            if (self.LOGOFONTDIRECTION == 1):
                if (self.LOGOFONT >= 64):
                    self.LOGOFONTDIRECTION = 0
                self.LOGOFONT += 1
            self.timer.start()

    def initGUI(self):
        self.SpaceInvadersLogo = Label.Label(x=0, y=60)
        self.SpaceInvadersLogo.alignHorizontally(None, Arcade.ALIGN_CENTER)
        self.SpaceInvadersLogo.addText("Space Invaders", Arcade.FONT, Arcade.GUI_COLOR_ORANGE, self.LOGOFONT)

        self.startBTN = Button.Button(y=215, width=250, height=50)
        self.startBTN.alignHorizontally(None, Arcade.ALIGN_CENTER)
        self.startBTN.addText("START", Arcade.FONT, Arcade.WHITE, 24)
        self.startBTN._borderColor = Arcade.BLUE

        self.leaderboardBTN = Button.Button(y=275, width=250, height=50)
        self.leaderboardBTN.alignHorizontally(None, Arcade.ALIGN_CENTER)
        self.leaderboardBTN.addText("LEADERBOARD", Arcade.FONT, Arcade.WHITE, 24)
        self.leaderboardBTN._borderColor = Arcade.BLUE

        self.quitBTN = Button.Button(y=335, width=250, height=50)
        self.quitBTN.alignHorizontally(None, Arcade.ALIGN_CENTER)
        self.quitBTN.addText("QUIT", Arcade.FONT, Arcade.WHITE, 24)
        self.quitBTN._borderColor = Arcade.BLUE
        
        Arcade.setSelectedGUI(self.startBTN)
        self.startBTN.setNeighbors(None, self.leaderboardBTN, None, None)
        self.leaderboardBTN.setNeighbors(self.startBTN, self.quitBTN, None, None)
        self.quitBTN.setNeighbors(self.leaderboardBTN, None, None, None)

    def updateGUI(self, screen):
        screen.blit(self.BG, (0,0))
        self.SpaceInvadersLogo.update(screen)
        self.startBTN.update(screen)
        self.leaderboardBTN.update(screen)
        self.quitBTN.update(screen)

        if (self.startBTN.isClicked()):
            Handler.setCurrentState(Handler.gameState)

        if (self.quitBTN.isClicked()):
            Handler.quit = True

