selectSaveState = None
gameState = None
currentState = None

IMAGE_SCALE = 64

def setCurrentState(state):
    global currentState

    if(currentState != None):
        currentState.show(False)
    state.show(True)
    currentState = state