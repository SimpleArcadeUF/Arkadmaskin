import pygame, math

class SpriteSheet():

    def __init__(self, path, spriteSize):
        self._image = pygame.image.load(path)
        self._spriteSize = spriteSize

        self._rows = int(self._image.get_height() / spriteSize)
        self._columns = int(self._image.get_width() / spriteSize)

        self._images = []

        for y in range(self._rows):
            self._images.append([])
            for x in range(self._columns):
                self._images[y].append(self._image.subsurface((x*spriteSize, y*spriteSize, spriteSize, spriteSize)))

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

    def scaleImages(self, newSize):
        for y in range(self._rows):
            for x in range(self._columns):
                self._images[y][x] = pygame.transform.scale(self._images[y][x], (int(newSize), int(newSize)))