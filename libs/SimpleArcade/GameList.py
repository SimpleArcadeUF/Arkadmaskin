from games.Pong import Pong
from games.Pacman import Pacman
from games.Escape import Escape

GAMES = []

def initGames():
    global GAMES

    GAMES.append( Pacman.Packman() )
    GAMES.append( Pong.Pong() )
    GAMES.append( Escape.Escape() )