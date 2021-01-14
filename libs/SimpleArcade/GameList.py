from games.FlappyBird import FlappyBird
from games.Pong import Pong
from games.Pacman import Pacman

GAMES = []

def initGames():
    global GAMES

    GAMES.append( FlappyBird.FlappyBird() )
    GAMES.append( Pong.Pong() )
    GAMES.append( Pacman.Packman() )
