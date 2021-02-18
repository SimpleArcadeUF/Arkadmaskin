from games.FlappyBird import FlappyBird
from games.Pong import Pong
from games.Pacman import Pacman
from games.Snake import Snake

GAMES = []

def initGames():
    global GAMES

    GAMES.append( Pacman.Packman() )
    GAMES.append( Snake.Snake() )