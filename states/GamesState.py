import pygame
from states import State
from libs.SimpleArcade.gui import Label, Frame
from libs.SimpleArcade import Arcade, GameList

class GamesState(State.State):

    def __init__(self):
        super().__init__()

        self._lblTitle = Label.Label(y=20)
        self._lblTitle.addText("SPEL", Arcade.FONT, Arcade.GUI_COLOR_BLUE, 80)
        self._lblTitle.addUnderline(2, Arcade.GUI_COLOR_BLUE)
        self._lblTitle.alignHorizontally(None, Arcade.ALIGN_CENTER)

        self._games = []
        self._keyRightPressed = False
        self._keyLeftPressed = False
        self._selectedGameOffset = 0

        self._frameSize = 300
        self._spacing = 40
        self._cornerSpace = (Arcade.SCREEN_WIDTH - (3*self._frameSize+2*self._spacing)) / 2

        for i in range(len(GameList.GAMES)):
            game = GameList.GAMES[i]

            frame = Frame.Frame(x = self._cornerSpace+i*self._frameSize+i*self._spacing, y=150, width=self._frameSize, height=self._frameSize)
            frame.addBorder(2, Arcade.GUI_COLOR_RED)
            frame.addHighlightedBorder(Arcade.GUI_COLOR_ORANGE)
            frame.updateAttachedGuis(True)

            lbl = Label.Label()
            lbl.alignHorizontally(frame, Arcade.ALIGN_CENTER)
            lbl.alignVertically(frame, Arcade.ALIGN_TOP, 10)
            lbl.addText(game.getTitle(), Arcade.FONT, Arcade.GUI_COLOR_BLUE, 50)
            
            img = Frame.Frame(width = frame.getWidth()-100, height = frame.getWidth()-100)
            img.alignVertically(frame, Arcade.ALIGN_TOP, 60)
            img.alignHorizontally(frame, Arcade.ALIGN_CENTER)
            img.addImage(game.getLogo())

            frame.attachGui(lbl)
            frame.attachGui(img)

            self._games.append(frame)

    def update(self, screen):
        super().update(screen)

        self._lblTitle.update(screen)

        for i in range(len(self._games)):
            game = self._games[i]
            game.update(screen)
            
            if(game.isClicked()):
                Arcade.setCurrentState(Arcade.playState)
                Arcade.playState.playGame(GameList.GAMES[i])
        
        self._changeGame()

    def _changeGame(self):
        if(Arcade.PLATFORM == Arcade.PLATFORM_DESKTOP):
            keys = pygame.key.get_pressed()

            if(keys[pygame.K_LEFT]):
                if(self._keyLeftPressed == False):
                    if(self._selectedGameOffset < 0):
                        self._selectedGameOffset += 1

                        for i in range(len(self._games)):
                            game = self._games[i]
                            game.setX(self._cornerSpace+(i+self._selectedGameOffset)*self._frameSize+(i+self._selectedGameOffset)*self._spacing)
                        
                        self._keyLeftPressed = True
            else:
                self._keyLeftPressed = False

            if(keys[pygame.K_RIGHT]):
                if(self._keyRightPressed == False):
                    print(self._selectedGameOffset)
                    if(self._selectedGameOffset > 3-len(self._games)):
                        self._selectedGameOffset -= 1
                        
                        for i in range(len(self._games)):
                            game = self._games[i]
                            game.setX(self._cornerSpace+(i+self._selectedGameOffset)*self._frameSize+(i+self._selectedGameOffset)*self._spacing)
                        
                        self._keyRightPressed = True
            else:
                self._keyRightPressed = False

    def onShow(self):
        super().onShow()
    
        Arcade.setSelectedGUI(self._games[0])