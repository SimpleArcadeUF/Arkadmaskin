class Game:

    def __init__(self, title, logo):
        super().__init__()

        self._title = title
        self._logo = logo

    def onPlay(self):
        pass

    def update(self, screen):
        pass

    def getTitle(self):
        return self._title
    def getLogo(self):
        return self._logo


"""
class Pong(Game.Game):

    def __init__(self):
        super().__init__("Pong", (imagefile))

    def onPlay(self):
        pass

    def update(self, screen):
        pass
"""