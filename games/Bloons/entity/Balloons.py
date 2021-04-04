from games.Bloons.entity import Balloon
from games.Bloons.utils import Assets

red = blue = green = yellow = black = white = None

def init():
    global red, blue, green, yellow, black

    red = Balloon.Balloon(0,0, 2, Assets.balloonSheet.getImage(0,0), "r", 1, None, template=True)
    blue = Balloon.Balloon(0,0, 2.5, Assets.balloonSheet.getImage(1,0), "b", 2, "r", template=True)
    green = Balloon.Balloon(0,0, 3, Assets.balloonSheet.getImage(2,0), "g", 3, "b", template=True)
    yellow = Balloon.Balloon(0,0, 4, Assets.balloonSheet.getImage(3,0), "y", 4, "g", template=True)
    black = Balloon.Balloon(0,0, 3, Assets.balloonSheet.getImage(4,0), "bl", 5, "y", template=True, blastProtection=True)

waves = []

def initWaves():
    global waves

    waves = [                                  
        [["r", 12]],                                            #1
        [["r", 25]],                                            #2
        [["r", 24], ["b", 5]],                                  #3
        [["r", 10], ["b", 24]],                                 #4
        [["r", 30], ["b", 25]],                                 #5
        [["g", 15]],                                            #6
        [["b", 75]],                                            #7
        [["r", 115], ["b", 68]],                                #8
        [["b", 49], ["g", 22]],                                 #9
        [["g", 40]],                                            #10
        [["y", 24]],                                            #11
        [["b", 30], ["g", 25], ["y", 3]],                       #12
        [["r", 40], ["b", 75], ["g", 30]],                      #13
        [["y", 26]],                                            #14
        [["b", 30], ["g", 60]],                                 #15
        [["b", 80], ["g", 80]],                                 #16
        [["b", 150], ["g", 30]],                                #17
        [["b", 30], ["g", 26], ["y", 28]],                      #18
        [["g", 92]],                                            #19
        [["b", 40], ["y", 60]],                                 #20
        [["b", 10], ["g", 85], ["y", 30]],                      #21
        [["y", 45]],                                            #22
        [["y", 64], ["g", 35]],                                 #23
        [["b", 20], ["g", 60], ["y", 30]],                      #24
        [["g", 80], ["y", 50]],                                 #25
        [["y", 85]],                                            #26
        [["bl", 20]],                                           #27
        [["g", 40], ["y", 55]],                                 #28
        [["y", 125], ["bl", 20]],                               #29
        [["g", 252]],                                           #30
        [["b", 10], ["g", 58], ["bl", 28]],                     #31
        [["g", 25], ["y", 20], ["bl", 23]],                     #32
        [["y", 150]],                                           #33
        [["g", 35], ["y", 35], ["bl", 25]],                     #34
        [["g", 85], ["y", 117]],                                #35
        [["y", 118], ["bl", 33]],                               #36
        [["bl", 59]],                                           #37
        [["y", 225]],                                           #38
        [["r", 50],["b", 50],["g", 50],["y",50],["bl", 40]],    #39
        [["bl", 80]]                                            #40
    ]