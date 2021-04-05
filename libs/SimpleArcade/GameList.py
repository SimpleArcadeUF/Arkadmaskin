from games.Pong import Pong
from games.Pacman import Pacman
from games.Snake import Snake
from games.Escape import Escape
from games.Faestone import Faestone
from games.Bloons import Bloons
from games.GeoDash import GeoDash
from games.PolygonArena import PolygonArena
<<<<<<< HEAD
from games.CookieClicker import CookieClicker
from games.SpaceInvaders import SpaceInvaders
=======
from games.Titanic import Titanic
>>>>>>> 5ec2748df2f5cd5f193e0db5cedebe519ccdcfcc

GAMES = []

def initGames():
    global GAMES
    
<<<<<<< HEAD
    GAMES.append( SpaceInvaders.SpaceInvaders() )
    GAMES.append( CookieClicker.CookieClicker() )
=======
    GAMES.append( Titanic.Titanic() )
>>>>>>> 5ec2748df2f5cd5f193e0db5cedebe519ccdcfcc
    GAMES.append( GeoDash.GeoDash() )
    GAMES.append( Bloons.Bloons() )
    GAMES.append( PolygonArena.PolygyonArena() )
    GAMES.append( Faestone.Faestone() )
    GAMES.append( Pacman.Packman() )
    GAMES.append( Snake.Snake() )
    GAMES.append( Pong.Pong() )
    GAMES.append( Escape.Escape() )
    
