from games.Escape.utils import Assets

tileTypes = []
air = grass = dirt = None

def init():
    global air, grass, dirt

    air = TileType(0, False, -10)
    grass = TileType(1, True, -2)
    dirt = TileType(2, True, -2)
    silverOre = TileType(3, False, 2)

def getTileTypeByID(ID):
    for tileType in tileTypes:
        if(tileType.getID() == ID):
            return tileType

class TileType():

    def __init__(self, ID, solid, order):
        self._id = ID
        self._solid = solid
        self._order = order
        self._image = Assets.tileSheet.getImageByID(ID)

        tileTypes.append(self)

    def getImage(self):
        return self._image
        
    def getID(self):
        return self._id
    
    def isSolid(self):
        return self._solid

    def getOrder(self):
        return self._order