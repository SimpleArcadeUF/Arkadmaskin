from games.Bloons.map import Map
from games.Bloons.entity import Node

MAPS = []

def init():
    global MAPS
    
    #------------
    path = [Node.Node(0, 200), 
    Node.Node(200, 200), 
    Node.Node(200, 300), 
    Node.Node(400, 300), 
    Node.Node(400, 150),
    Node.Node(800, 150),
    Node.Node(800, 500),
    Node.Node(0, 500)]

    m = Map.Map("Default", path)
    m.showPath(True)
    MAPS.append(m)
    #--------------