from libs.SimpleArcade import Timer

gameState = None
shopState = None
currentState = None

quit = False

# Important Configs
cookies = 0 

# Upgrades
global cookiesPerClick, cookiesPerSeconds
cookiesPerClick = 1
cookiesPerClickPrice = 50
cookiesPerSeconds = 0
cookiesPerSecondsPrice = 200

timer = Timer.Timer(1000)
timer.start()

def setCurrentState(state):
    global currentState
    currentState = state
    currentState.onShow()

def update():
    global cookies
    timer.update()
    if (timer.isDone()):
        cookies += cookiesPerSeconds
        timer.start()
