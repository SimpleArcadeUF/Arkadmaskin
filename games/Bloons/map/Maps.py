from games.Bloons.map import Map
from games.Bloons.entity import Node

MAPS = []

def init():
    global MAPS
    
    #------------
    path = [Node.Node(0, 81*2), 
    Node.Node(118*2, 81*2), 
    Node.Node(118*2, 142*2), 
    Node.Node(200*2, 142*2), 
    Node.Node(200*2, 81*2),
    Node.Node(445*2, 81*2),
    Node.Node(445*2, 162*2),
    Node.Node(356*2, 162*2),
    Node.Node(356*2, 227*2),
    Node.Node(0, 227*2)]

    m = Map.Map("Default", path)
    m.showPath(False)
    MAPS.append(m)
    #--------------