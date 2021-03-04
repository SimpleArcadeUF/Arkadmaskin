import pygame, math

class SpriteSheet():

    def __init__(self, path, spriteSize=0, width=0, height=0):
        self._image = pygame.image.load(path)

        self._width = spriteSize
        self._height = spriteSize

        if(width != 0 or height != 0):
            self._width = width
            self._height = height

        self._rows = int(self._image.get_height() / self._height)
        self._columns = int(self._image.get_width() / self._width)

        self._images = []

        for y in range(self._rows):
            self._images.append([])
            for x in range(self._columns):
                self._images[y].append(self._image.subsurface((x*self._width, y*self._height, self._width, self._height)))

    def getImagesByRow(self, row, amount):
        images = []
        for x in range(amount):
            images.append(self._images[row][x])
        return images


    def getImage(self, x, y):
        return self._images[y][x]

    def getImageByID(self, ID):
        y = math.floor(ID / self._columns)
        x = ID - y*self._columns

        return self.getImage(x, y)

    def scaleImages(self, newSize=0, width=0, height=0):
        w = newSize
        h = newSize
        if(width != 0 or height != 0):
            w = width
            h = height
        for y in range(self._rows):
            for x in range(self._columns):
                self._images[y][x] = pygame.transform.scale(self._images[y][x], (int(w), int(h)))