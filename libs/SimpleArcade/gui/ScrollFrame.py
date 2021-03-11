from libs.SimpleArcade.gui import Frame

class ScrollFrame(Frame.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._guis = []

    def update(self, screen):
        super().update(screen)

    def addGUI(self, gui):
        self._guis.append(gui)

    def show(self, tof):
        super().show(tof)