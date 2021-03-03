from games.GeoDash import State, Handler
from libs.SimpleArcade.gui import Label, Button, Frame
from libs.SimpleArcade import Game, Arcade


class LevelState(State.State):

    def __init__(self):

        #Main frame
        self.Main_frame = Frame.Frame(x=0,y=200, width=500, height=300)
        self.Main_frame.alignHorizontally(None, Arcade.ALIGN_CENTER)
        self.Main_frame.updateAttachedGuis(True)    

        #subframe top
        self.Sub_frame_top = Frame.Frame(x=0,y=200, width=500, height=150)
        self.Sub_frame_top.alignVertically(self.Main_frame, Arcade.ALIGN_TOP)
        self.Sub_frame_top.alignHorizontally(self.Main_frame, Arcade.ALIGN_CENTER)
        self.Sub_frame_top.updateAttachedGuis(True)

        #subframe bottom
        self.Sub_frame_bottom = Frame.Frame(x=0,y=350, width=500, height=150)
        self.Sub_frame_bottom.alignVertically(self.Main_frame, Arcade.ALIGN_BOTTOM)
        self.Sub_frame_bottom.alignHorizontally(self.Main_frame, Arcade.ALIGN_CENTER)
        self.Sub_frame_bottom.updateAttachedGuis(True)


        #Main menu label
        self.Label = Label.Label(x=0,y=10)
        self.Label.alignHorizontally(None, Arcade.ALIGN_CENTER)
        self.Label.addText("GeoRush", Arcade.FONT, "white", 100)

        #Level 1 button
        self.B_LEVEL1 = Button.Button(x=0,y=30, width=120, height=60)
        self.B_LEVEL1.alignHorizontally(self.Sub_frame_top, Arcade.ALIGN_CENTER, offset=-150)
        self.B_LEVEL1.alignVertically(self.Sub_frame_top, Arcade.ALIGN_CENTER)
        self.B_LEVEL1.addText("Level 1", Arcade.FONT, "white", 20)

        #Level 2 button
        self.B_LEVEL2 = Button.Button(x=0,y=30, width=120, height=60)
        self.B_LEVEL2.alignHorizontally(self.Sub_frame_top, Arcade.ALIGN_CENTER)
        self.B_LEVEL2.alignVertically(self.Sub_frame_top, Arcade.ALIGN_CENTER)
        self.B_LEVEL2.addText("Level 2", Arcade.FONT, "white", 20)

        #Level 3 button
        self.B_LEVEL3 = Button.Button(x=0,y=30, width=120, height=60)
        self.B_LEVEL3.alignHorizontally(self.Sub_frame_top, Arcade.ALIGN_CENTER, offset=150)
        self.B_LEVEL3.alignVertically(self.Sub_frame_top, Arcade.ALIGN_CENTER)
        self.B_LEVEL3.addText("Level 3", Arcade.FONT, "white", 20)


        #Main menu button | Quit
        self.B_QUIT = Button.Button(x=0,y=30, width=120, height=60)
        self.B_QUIT.alignHorizontally(self.Sub_frame_bottom, Arcade.ALIGN_CENTER)
        self.B_QUIT.alignVertically(self.Sub_frame_bottom, Arcade.ALIGN_TOP)
        self.B_QUIT.addText("Quit", Arcade.FONT, "white", 20)

        self.Main_frame.attachGui(self.Sub_frame_top)
        self.Main_frame.attachGui(self.Sub_frame_bottom)

        self.Sub_frame_top.attachGui(self.B_LEVEL1)
        self.Sub_frame_top.attachGui(self.B_LEVEL2)
        self.Sub_frame_top.attachGui(self.B_LEVEL3)
        self.Sub_frame_bottom.attachGui(self.B_QUIT)


    def update(self, screen):
      
        self.Main_frame.update(screen)
        self.Label.update(screen)

        if self.B_QUIT.isClicked(True):
            Handler.quit = True

        if self.B_LEVEL1.isClicked(True):
            Handler.currentState = Handler.GameState



