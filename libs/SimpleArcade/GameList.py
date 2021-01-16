from games.FlappyBird import FlappyBird
from games.Pong import Pong
from games.Pacman import Pacman

GAMES = []

def initGames():
    global GAMES

    GAMES.append( Pacman.Packman() )
    GAMES.append( Pong.Pong() )
    #GAMES.append( Pacman.Packman() )
    #GAMES.append( FlappyBird.FlappyBird() )
