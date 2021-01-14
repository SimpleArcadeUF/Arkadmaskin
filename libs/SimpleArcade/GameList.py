from games.FlappyBird import FlappyBird
from games.Pong import Pong

GAMES = []

def initGames():
    global GAMES

    GAMES.append( FlappyBird.FlappyBird() )
    GAMES.append( Pong.Pong() )
