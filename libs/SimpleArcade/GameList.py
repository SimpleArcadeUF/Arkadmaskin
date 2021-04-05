from games.Pong import Pong
from games.Pacman import Pacman
from games.Snake import Snake
from games.Escape import Escape
from games.Faestone import Faestone
from games.Bloons import Bloons
from games.GeoDash import GeoDash
from games.PolygonArena import PolygonArena
from games.Titanic import Titanic

GAMES = []

def initGames():
    global GAMES
    
    GAMES.append( Titanic.Titanic() )
    GAMES.append( GeoDash.GeoDash() )
    GAMES.append( Bloons.Bloons() )
    GAMES.append( PolygonArena.PolygyonArena() )
    GAMES.append( Faestone.Faestone() )
    GAMES.append( Pacman.Packman() )
    GAMES.append( Snake.Snake() )
    GAMES.append( Pong.Pong() )
    GAMES.append( Escape.Escape() )
