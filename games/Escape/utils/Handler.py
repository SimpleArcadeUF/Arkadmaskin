selectSaveState = None
gameState = None
currentState = None

TILE_SIZE = 64
IMAGE_SCALE = TILE_SIZE/16

gameCamera = None

def setCurrentState(state):
    global currentState

    if(currentState != None):
        currentState.show(False)
    state.show(True)
    currentState = state