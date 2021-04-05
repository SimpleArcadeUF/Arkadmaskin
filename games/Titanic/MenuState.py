from games.Titanic import State, Handler
from libs.SimpleArcade.gui import Label, Button
from libs.SimpleArcade import Arcade

class MenuState:

    def __init__(self):
        super().__init__()

        self._lblTitle = Label.Label(y=5)
        self._lblTitle.addText("Titanic Driver", Arcade.FONT, (255,255,255), 50)
        self._lblTitle.alignHorizontally(None, Arcade.ALIGN_CENTER)

        self._btnPlay = Button.Button(width=250, height=55)
        self._btnPlay.addText("Spela", Arcade.FONT, (0,0,0), 40)
        self._btnPlay.alignHorizontally(None, Arcade.ALIGN_CENTER)
        self._btnPlay.alignVertically(None, Arcade.ALIGN_CENTER, -50)

        self._btnQuit = Button.Button(width=250, height=55)
        self._btnQuit.addText("Avsluta", Arcade.FONT, (0,0,0), 40)
        self._btnQuit.alignHorizontally(None, Arcade.ALIGN_CENTER)
        self._btnQuit.alignVertically(None, Arcade.ALIGN_CENTER, 50)

        self._btnPlay.setNeighbors(None, self._btnQuit, None, None)
        self._btnQuit.setNeighbors(self._btnPlay, None, None, None)


    def update(self, screen):
        screen.fill((45,45,75))

        self._lblTitle.update(screen)
        self._btnPlay.update(screen)
        self._btnQuit.update(screen)

        if(self._btnPlay.isClicked()):
            Handler.setState(Handler.gameState)

        if(self._btnQuit.isClicked()):
            Handler.quit = True
    
    def onShow(self):
        Arcade.setSelectedGUI(self._btnPlay)