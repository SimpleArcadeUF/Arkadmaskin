from libs.SimpleArcade.gui import GUI

class Frame(GUI.GUI):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update(self, screen):
        super().update(screen)