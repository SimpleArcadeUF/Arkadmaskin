from games.Escape.objects import Tile, TileType, GameObject

class World():

    def __init__(self):
        self._tiles = [] #Simulate as a 2D array

    def update(self, screen):
        for obj in GameObject.GAME_OBJECTS:
            obj.update(screen)

    def loadMap(self, path):
        file = open(path, "r")
        
        sizeRaw = file.readline().split(" ")
        self._mapWidth = int(sizeRaw[0])
        self._mapHeight = int(sizeRaw[1])

        for y in range(self._mapHeight):
            row = file.readline().split(" ")
            for x in range(self._mapWidth):
                tileType = TileType.getTileTypeByID(int(row[x]))
                tile = Tile.Tile(tileType.getOrder(), tileType, x, y)
                self._tiles.append(tile)
    
    def getTiles(self):
        return self._tiles
