from games.Bloons.entity import Balloon
from games.Bloons.utils import Assets

red = blue = green = yellow = black = white = None

def init():
    global red, blue, green, yellow

    red = Balloon.Balloon(0,0, 2, Assets.balloonSheet.getImage(0,0), "r", 1, None, template=True)
    blue = Balloon.Balloon(0,0, 4, Assets.balloonSheet.getImage(1,0), "b", 2, "r", template=True)
    green = Balloon.Balloon(0,0, 6, Assets.balloonSheet.getImage(2,0), "g", 3, "b", template=True)
    yellow = Balloon.Balloon(0,0, 8, Assets.balloonSheet.getImage(3,0), "y", 4, "g", template=True)

waves = []

def initWaves():
    global waves

    waves = [                                  
        [["r", 12]],                                #1
        [["r", 25]],                                #2
        [["r", 24], ["b", 5]],                      #3
        [["r", 10], ["b", 24]],                     #4
        [["r", 30], ["b", 25]],                     #5
        [["g", 15]],                                #6
        [["b", 75]],                                #7
        [["r", 115], ["b", 68]],                    #8
        [["b", 49], ["g", 22]],                     #9
        [["g", 40]],                                #10
        [["y", 24]],                                #11
        [["b", 30], ["g", 25], ["y", 3]],           #12
        [["r", 40], ["b", 75], ["g", 30]],          #13
    ]