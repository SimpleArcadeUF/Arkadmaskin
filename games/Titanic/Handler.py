gameState = None
currentState = None
quit = False
SCALE = 4

def setState(state):
    global currentState
    currentState = state
    state.onShow()