from games.Pong import Pong
from games.Pacman import Pacman
from games.Snake import Snake
from games.Escape import Escape
from games.Faestone import Faestone
from games.GeoDash import GeoDash

GAMES = []

def initGames():
    global GAMES

    GAMES.append( Faestone.Faestone() )
    GAMES.append( Pacman.Packman() )
    GAMES.append( Snake.Snake() )
    GAMES.append( Pong.Pong() )
    GAMES.append( Escape.Escape() )
    GAMES.append( GeoDash.GeoDash() )

