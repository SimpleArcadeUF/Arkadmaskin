import pygame
from states import State
from libs.SimpleArcade.gui import Frame, Button, Label, GUI
from libs.SimpleArcade import Arcade

class StartState(State.State):

    def __init__(self):
        super().__init__()

        self._image = GUI.GUI(width=300, height=300)
        self._image.alignHorizontally(None, Arcade.ALIGN_CENTER, 200)
        self._image.alignVertically(None, Arcade.ALIGN_CENTER)
        self._image.addImage(pygame.image.load("res/images/logo.png"))

        self._frame = Frame.Frame(x=200, y=200, width=320, height=400)
        self._frame.addBorder(2, Arcade.GUI_COLOR_BLUE)
        self._frame.alignHorizontally(None, Arcade.ALIGN_CENTER, -200)
        self._frame.alignVertically(None, Arcade.ALIGN_CENTER, 20)

        self._lblTitle = Label.Label()
        self._lblTitle.addText("SIMPLE ARCADE UF", "roboto", Arcade.GUI_COLOR_BLUE, 80)
        self._lblTitle.addUnderline(2, Arcade.GUI_COLOR_BLUE, -5)
        self._lblTitle.alignHorizontally(None, Arcade.ALIGN_CENTER)
        self._lblTitle.alignVertically(None, Arcade.ALIGN_TOP, 25)

        self._lblWelcome = Label.Label()
        self._lblWelcome.addText("VÄLKOMMEN", "roboto", Arcade.GUI_COLOR_BLUE, 60)
        self._lblWelcome.addUnderline(2, Arcade.GUI_COLOR_BLUE, -5)
        self._lblWelcome.alignHorizontally(self._frame, Arcade.ALIGN_CENTER)
        self._lblWelcome.alignVertically(self._frame, Arcade.ALIGN_TOP, 25)

        self._btnGames = Button.Button(width=270, height=50)
        self._btnGames.addText("SPEL", "roboto", Arcade.GUI_COLOR_RED, 40)
        self._btnGames.alignHorizontally(self._frame, Arcade.ALIGN_CENTER)
        self._btnGames.alignVertically(self._frame, Arcade.ALIGN_CENTER, -50)

        self._btnHighScores = Button.Button(width=270, height=50)
        self._btnHighScores.addText("HIGHSCORES", "roboto", Arcade.GUI_COLOR_RED, 40)
        self._btnHighScores.alignHorizontally(self._frame, Arcade.ALIGN_CENTER)
        self._btnHighScores.alignVertically(self._frame, Arcade.ALIGN_CENTER, 30)

        self._btnExit = Button.Button(width=270, height=50)
        self._btnExit.addText("AVSLUTA", "roboto", Arcade.GUI_COLOR_RED, 40)
        self._btnExit.alignHorizontally(self._frame, Arcade.ALIGN_CENTER)
        self._btnExit.alignVertically(self._frame, Arcade.ALIGN_CENTER, 110)

        self._btnGames.setNeighbors(None, self._btnHighScores, None, None)
        self._btnHighScores.setNeighbors(self._btnGames, self._btnExit, None, None)
        self._btnExit.setNeighbors(self._btnHighScores, None, None, None)

        if(Arcade.PLATFORM == Arcade.PLATFORM_ARCADE):
            Arcade.setSelectedGUI(self._btnGames)

    def update(self, screen):
        super().update(screen)
    
        self._lblTitle.update(screen)
        self._image.update(screen)

        self._frame.update(screen)
        self._lblWelcome.update(screen)
        self._btnGames.update(screen)
        self._btnExit.update(screen)
        self._btnHighScores.update(screen)

        if(self._btnGames.isClicked()):
            Arcade.setCurrentState(Arcade.gamesState)
            Arcade.GUI_IS_CLICKED = True

        if(self._btnExit.isClicked()):
            Arcade.isRunning = False