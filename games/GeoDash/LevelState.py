from games.GeoDash import State, Handler
from libs.SimpleArcade.gui import Label, Button, Frame
from libs.SimpleArcade import Game, Arcade


class LevelState(State.State):

    def __init__(self):

        #Main frame
        self.Main_frame = Frame.Frame(x=0,y=200, width=500, height=300)
        self.Main_frame.alignHorizontally(None, Arcade.ALIGN_CENTER)
        #self.Main_frame.addBorder(3, "red")
        self.Main_frame.updateAttachedGuis(True)

        #Main menu label
        self.Label = Label.Label(x=0,y=10)
        self.Label.alignHorizontally(None, Arcade.ALIGN_CENTER)
        self.Label.addText("GeoRush", Arcade.FONT, "white", 100)


        #Main menu button | Quit
        self.B_QUIT = Button.Button(x=0,y=30, width=120, height=60)
        self.B_QUIT.alignHorizontally(None, Arcade.ALIGN_CENTER)
        self.B_QUIT.alignVertically(None, Arcade.ALIGN_BOTTOM)
        self.B_QUIT.addText("Quit", Arcade.FONT, "white", 20)

    def update(self, screen):
      
        self.Main_frame.update(screen)
        self.Label.update(screen)
    
        if self.B_QUIT.isClicked(True):
            self.quit()
            running = False

