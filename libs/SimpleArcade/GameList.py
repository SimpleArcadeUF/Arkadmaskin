from games.Pong import Pong
from games.Pacman import Pacman
from games.Snake import Snake
from games.Escape import Escape
from games.Faestone import Faestone
from games.Bloons import Bloons
from games.GeoDash import GeoDash
from games.PolygonArena import PolygonArena
from games.CookieClicker import CookieClicker
from games.SpaceInvaders import SpaceInvaders

GAMES = []

def initGames():
    global GAMES
    
    GAMES.append( SpaceInvaders.SpaceInvaders() )
    GAMES.append( CookieClicker.CookieClicker() )
    GAMES.append( GeoDash.GeoDash() )
    GAMES.append( Bloons.Bloons() )
    GAMES.append( PolygonArena.PolygyonArena() )
    GAMES.append( Faestone.Faestone() )
    GAMES.append( Pacman.Packman() )
    GAMES.append( Snake.Snake() )
    GAMES.append( Pong.Pong() )
    GAMES.append( Escape.Escape() )
    
