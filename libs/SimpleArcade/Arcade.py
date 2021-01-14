import pygame, os

PLATFORM_ARCADE = 0
PLATFORM_DESKTOP = 1
PLATFORM = PLATFORM_DESKTOP

ALIGN_CENTER = 0 
ALIGN_LEFT = 1
ALIGN_RIGHT = 2
ALIGN_TOP = 3 
ALIGN_BOTTOM = 4

GUI_COLOR_RED = (255,50,50)
GUI_COLOR_BLUE = (60,130,255)
GUI_COLOR_ORANGE = (255, 135, 10)

FONT = "roboto"
SELECTED_GUI = None
joystick = None
screen = None
isRunning = True
currentState = None
clock = None
FPS = 60

SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0

startState = None
gamesState = None
playState = None

def init():
    global screen, joystick, SCREEN_WIDTH, SCREEN_HEIGHT, clock
    global startState, gamesState

    pygame.init()
    pygame.font.init()

    clock = pygame.time.Clock()

    if(PLATFORM == PLATFORM_ARCADE):
        pygame.joystick.init()
        joystick = pygame.joystick.Joystick(0)
        joystick.init()

        screen = pygame.display.set_mode((1024,600))

    elif(PLATFORM == PLATFORM_DESKTOP):
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        screen = pygame.display.set_mode((1024,600))
    
    SCREEN_WIDTH = screen.get_width()
    SCREEN_HEIGHT = screen.get_height()

BUTTON_PRESSED_1 = False
BUTTON_PRESSED_2 = False
BUTTON_PRESSED_3 = False
BUTTON_PRESSED_4 = False

JOYSTICK_PRESSED_UP = False
JOYSTICK_PRESSED_DOWN = False
JOYSTICK_PRESSED_LEFT = False
JOYSTICK_PRESSED_RIGHT = False

_JOYSTICK_UP = False
_JOYSTICK_DOWN = False
_JOYSTICK_LEFT = False
_JOYSTICK_RIGHT = False

_BUTTON_1 = False
_BUTTON_2 = False
_BUTTON_3 = False
_BUTTON_4 = False

def update():
    global BUTTON_PRESSED_1, BUTTON_PRESSED_2, BUTTON_PRESSED_3, BUTTON_PRESSED_4
    global _BUTTON_1, _BUTTON_2, _BUTTON_3, _BUTTON_4
    global _JOYSTICK_UP, _JOYSTICK_DOWN, _JOYSTICK_LEFT, _JOYSTICK_RIGHT
    global JOYSTICK_PRESSED_UP, JOYSTICK_PRESSED_DOWN, JOYSTICK_PRESSED_LEFT, JOYSTICK_PRESSED_RIGHT
    
    BUTTON_PRESSED_1 = False
    BUTTON_PRESSED_2 = False
    BUTTON_PRESSED_3 = False
    BUTTON_PRESSED_4 = False

    JOYSTICK_PRESSED_DOWN = False
    JOYSTICK_PRESSED_LEFT = False
    JOYSTICK_PRESSED_RIGHT = False
    JOYSTICK_PRESSED_UP = False

    clock.tick(FPS)

    if(PLATFORM == PLATFORM_ARCADE):
        
        axisVertical = round(joystick.get_axis(0))
        axisHorizontal = round(joystick.get_axis(1))
        
        #Joystick Top
        if(axisVertical == 1):
            if(_JOYSTICK_UP == False):
                _JOYSTICK_UP = True
                JOYSTICK_PRESSED_UP = True
        else:
            _JOYSTICK_UP = False
        #Joystick Bottom
        if(axisVertical == -1):
            if(_JOYSTICK_DOWN == False):
                _JOYSTICK_DOWN = True
                JOYSTICK_PRESSED_DOWN = True
        else:
            _JOYSTICK_DOWN = False
        #Joystick Left
        if(axisHorizontal == -1):
            if(_JOYSTICK_LEFT == False):
                _JOYSTICK_LEFT = True
                JOYSTICK_PRESSED_LEFT = True
        else:
            _JOYSTICK_LEFT = False
        #Joystick Right
        if(axisHorizontal == 1):
            if(_JOYSTICK_RIGHT == False):
                _JOYSTICK_RIGHT = True
                JOYSTICK_PRESSED_RIGHT = True
        else:
            _JOYSTICK_RIGHT = False

        #Knapp 1
        if(joystick.get_button(0)):
            if(_BUTTON_1 == False):
                _BUTTON_1 = True
                BUTTON_PRESSED_1 = True
        else:
            _BUTTON_1 = False
        #Knapp 2
        if(joystick.get_button(1)):
            if(_BUTTON_2 == False):
                _BUTTON_2 = True
                BUTTON_PRESSED_2 = True
        else:
            _BUTTON_2 = False
        #Knapp 3
        if(joystick.get_button(2)):
            if(_BUTTON_3 == False):
                _BUTTON_3 = True
                BUTTON_PRESSED_3 = True
        else:
            _BUTTON_3 = False
        #Knapp 4
        if(joystick.get_button(3)):
            if(_BUTTON_4 == False):
                _BUTTON_4 = True
                BUTTON_PRESSED_4 = True
        else:
            _BUTTON_4 = False

def setSelectedGUI(gui):
    global SELECTED_GUI
    
    if(SELECTED_GUI != None):
        SELECTED_GUI.setHovered(False)
    
    SELECTED_GUI = gui
    gui.setHovered(True)

def setCurrentState(state):
    global currentState
    currentState = state
    currentState.onShow()