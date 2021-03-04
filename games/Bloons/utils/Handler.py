selectMapState = None
gameState = None
currentState = None

IMAGE_SCALE = 64
GAME_SPEED = 1

currentMap = None

def setCurrentState(state):
    global currentState

    if(currentState != None):
        currentState.show(False)
    state.show(True)
    currentState = state