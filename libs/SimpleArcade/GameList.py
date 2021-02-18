from games.Pong import Pong
from games.Pacman import Pacman
<<<<<<< HEAD
from games.Snake import Snake
=======
from games.Escape import Escape
from games.Faestone import Faestone
>>>>>>> 85405a328cdd8440020ce00552c4197c0b63fe92

GAMES = []

def initGames():
    global GAMES

    GAMES.append( Faestone.Faestone() )
    GAMES.append( Pacman.Packman() )
<<<<<<< HEAD
    GAMES.append( Snake.Snake() )
=======
    GAMES.append( Pong.Pong() )
    GAMES.append( Escape.Escape() )
>>>>>>> 85405a328cdd8440020ce00552c4197c0b63fe92
