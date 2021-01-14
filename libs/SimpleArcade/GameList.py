from games.FlappyBird import FlappyBird
from games.Pong import Pong
from games.Pacman import Pacman

GAMES = []

def initGames():
    global GAMES

    GAMES.append( FlappyBird.FlappyBird() )
