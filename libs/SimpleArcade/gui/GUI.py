import pygame

class GUI:
    
    def __init__(self, x=0, y=0, width=100, height=100, color=(255,0,0)):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._color = color
        
    def update(self):
        pass
    
    def render(self, screen):
        pygame.draw.rect(screen, self._color, (self._x, self._y, self._width, self._height))
    
    def centerHorizontally(self, gui):
        if(gui == None):
            w, h = pygame.display.get_surface().get_size()
            self._x = w / 2 - self._width/2
        else:
            self._x = gui.getX() + (gui.getWidth() - self._width) / 2
            
    def centerVertically(self, gui):
        if(gui == None):
            w, h = pygame.display.get_surface().get_size()
            self._y = h / 2 - self._height/2
        else:
            self._y = gui.getY() + (gui.getHeight() - self._height) / 2
    
    def getX(self):
        return self._x
    def getY(self):
        return self._y
    def getWidth(self):
        return self._width
    def getHeight(self):
        return self._height