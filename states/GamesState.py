import os

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

        for i in range(len(GameList.GAMES)):
            game = GameList.GAMES[i]

            frame = Frame.Frame(y=100, width=400, height=400)
            frame.addBorder(2, Arcade.GUI_COLOR_RED)
            frame.addHighlightedBorder(Arcade.GUI_COLOR_ORANGE)
            frame.updateAttachedGuis(True)

            lbl = Label.Label(y = 110, x=i*420+10)
            lbl.alignHorizontally(frame, Arcade.ALIGN_CENTER)
            lbl.addText(game.getTitle(), Arcade.FONT, Arcade.GUI_COLOR_BLUE, 50)
            
            img = Frame.Frame(x = 50, y = 160, width = frame.getWidth()-100, height = frame.getWidth()-100)
            img.addImage(game.getLogo())

            x = 0
            if(i % 2 == 0): x = -1
            else:           x = 1

            frame.attachGui(lbl)
            frame.attachGui(img)

            frame.alignHorizontally(None, Arcade.ALIGN_CENTER, x*420/2)
            self._games.append(frame)

    def update(self, screen):
        super().update(screen)

        self._lblTitle.update(screen)

        for i in range(len(self._games)):
            game = self._games[i]
            game.update(screen)
            
            #if(game.isClicked()):
                #Arcade.setCurrentState(Arcade.playState)
                #Arcade.playState.playGame(GameList.GAMES[i])
            

    def onShow(self):
        super().onShow()
    
        Arcade.setSelectedGUI(self._games[0])