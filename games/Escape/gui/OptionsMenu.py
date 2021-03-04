from libs.SimpleArcade.gui import GUI, Button
from libs.SimpleArcade import Arcade

class OptionsMenu(GUI.GUI):

    def __init__(self, buttonSize, margin, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._buttonSize = buttonSize
        self._margin = margin
        self._optionButtons = []

    def update(self, screen):
        super().update(screen)

        for i in range(len(self._optionButtons)):
            self._optionButtons[i].update(screen)

    def show(self, tof):
        super().show(tof)
        for i in range(len(self._optionButtons)):
            self._optionButtons[i].show(tof)

    def addButton(self, image):
        btn = Button.Button(width = self._buttonSize, height = self._buttonSize, show=False)
        btn.addImage(image)
        self._optionButtons.append(btn)

        for i in range(len(self._optionButtons)):
            self._optionButtons[i].alignHorizontally(None, Arcade.ALIGN_CENTER, (-len(self._optionButtons)/2 + i+1)*(self._optionButtons[i].getWidth()+self._margin)-self._optionButtons[i].getWidth()/2-self._margin/2)
            self._optionButtons[i].alignVertically(None, Arcade.ALIGN_CENTER, -100)
    
    def getButton(self, index):
        return self._optionButtons[index]