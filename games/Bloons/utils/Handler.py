selectMapState = None
gameState = None
currentState = None

IMAGE_SCALE = 2
BALLOON_SIZE = 32
GAME_SPEED = 1

currentMap = None

def setCurrentState(state):
    global currentState

    if(currentState != None):
        currentState.show(False)
    state.show(True)
    currentState = state