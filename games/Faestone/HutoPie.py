"""
//General
-init(title, width, height) initialize application
-quit() quit application
-isRunning() returns the running state of the application
-beginUpdate(color) begins the update
-endUpdate() ends the update, checks for events, flips the display
-setResizeable(resizable) set the screens resizable state

//Assets
-loadImage(path) loads an image/surface
-scaleImage(image, width, height, destinationSurface = None) scales an image/surface
-scaleImageSmooth(image, width, height, destinationSurface = None) smooth scales an image/surface
-rotateImage(image, angle) rotates an image/surface
-subImage(image, x, y, width, height) gets a part of a image
-loadSound(path) loads a sound file

//Rendering
-drawCircle(x, y, radius, color)
-drawRect(x, y, width, height, color)
-drawImage(x, y, image)

//Inputs
-isKeyDown(keyCode)
-MOUSE_X
-MOUSE_Y
-isLeftMousePressed()
-isLeftMouseReleased()
-isLeftMouseDown()
-isRightMousePressed()
-isRightMouseReleased()
-isRightMouseDown()
"""

import pygame
import time
import sys

SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0
DELTA_TIME = 0
FPS = 0
MAX_FPS = 60
MOUSE_X = 0
MOUSE_Y = 0

__isRunning = False
__isResizeable = True
__screen = None;
__keys = []
__clock = None;
__leftMousePressed = False
__leftMouseReleased = False
__leftMouseDown = False
__rightMousePressed = False
__rightMouseReleased = False
__rightMouseDown = False

def init(title, w, h):
    global SCREEN_WIDTH, SCREEN_HEIGHT, __isRunning, __screen, __clock
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption(title)
    pygame.mixer.init()

    SCREEN_WIDTH = w
    SCREEN_HEIGHT = h
    __isRunning = True

    if(__isResizeable):
        __screen = pygame.display.set_mode([w, h], pygame.RESIZABLE)
    else:
        __screen = pygame.display.set_mode([w, h])

    __clock = pygame.time.Clock()

def quit():
    global __isRunning

    __isRunning = False

    pygame.mixer.quit()
    pygame.quit()

def beginUpdate(color=(255, 255, 255)):
    global __keys, MOUSE_X, MOUSE_Y

    __keys = pygame.key.get_pressed()
    __screen.fill(color)

    MOUSE_X = pygame.mouse.get_pos()[0]
    MOUSE_Y = pygame.mouse.get_pos()[1]

def endUpdate():
    global DELTA_TIME, FPS, __leftMousePressed, __leftMouseReleased, __rightMousePressed, __rightMouseReleased
    global __leftMouseDown, __rightMouseDown

    pygame.display.flip()

    __leftMousePressed = False
    __leftMouseReleased = False
    __rightMousePressed = False
    __rightMouseReleased = False

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            quit()
        if (event.type == pygame.VIDEORESIZE):
            SCREEN_WIDTH = event.w
            SCREEN_HEIGHT = event.h
            __screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        if (event.type == pygame.MOUSEBUTTONDOWN):
            if(event.button == 1):
                __leftMousePressed = True
                __leftMouseDown = True
            elif(event.button == 3):
                __rightMousePressed = True
                __rightMouseDown = True
        if (event.type == pygame.MOUSEBUTTONUP):
            if(event.button == 1):
                __leftMouseReleased = True
                __leftMouseDown = False
            elif(event.button == 3):
                __rightMouseReleased = True
                __rightMouseDown = False

    DELTA_TIME = __clock.tick(MAX_FPS) / 10
    FPS = __clock.get_fps()

def isRunning():
    return __isRunning

def setResizeable(resizeable):
    __isResizeable = resizeable
    if(resizeable):
        pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], pygame.RESIZABLE)
    else:
        pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], 0)

def isKeyDown(keyCode):
    return __keys[keyCode]

def isLeftMousePressed():
    return __leftMousePressed
def isLeftMouseReleased():
    return __leftMouseReleased
def isRightMousePressed():
    return __rightMousePressed
def isRightMouseReleased():
    return __rightMouseReleased
def isLeftMouseDown():
    return __leftMouseDown
def isRightMouseDown():
    return __rightMouseDown

#---------RENDERING---------

def drawCircle(x, y, radius, color):
    pygame.draw.circle(__screen, color, (int(x), int(y)), radius)

def drawRect(x, y, width, height, color):
    pygame.draw.rect(__screen, color, (int(x), int(y), width, height))

def drawImage(x, y, image):
    __screen.blit(image, (int(x), int(y)))

def drawText(x, y, text):
    __screen.blit(text, (int(x), int(y)))

#---------ASSETS-----------

def loadImage(path):
    return pygame.image.load(path)

def scaleImage(image, width,height, destinationSurface = None):
    if(destinationSurface == None):
        return pygame.transform.scale(image, (width, height))
    else:
        return pygame.transform.scale(image, (width, height), destinationSurface)

def scaleImageSmooth(image, width, height, destinationSurface = None):
    if(destinationSurface == None):
        return pygame.transform.smoothscale(image, (width, height))
    else:
        return pygame.transform.smoothscale(image, (width, height), destinationSurface)

def rotateImage(image, angle):
    return pygame.transform.rotate(image, angle)

def subImage(image, x, y, width, height):
    return image.subsurface((x, y, width, height))

def getFont(fontName, fontSize):
    """Expensive to call every frame"""
    return pygame.font.SysFont(fontName, fontSize)

def createText(text, font, color):
    """Expensive to call every frame"""
    return font.render(text, True, color)

def loadSound(path):
    return pygame.mixer.Sound(path)
    
#---------KEYCODES---------
#https://wiki.libsdl.org/SDLKeycodeLookup

K_BACKSPACE = 8
K_TAB = 9
K_ESCAPE = 27
K_SPACE = 32
K_A = 97
K_B = 98
K_C = 99
K_D = 100
K_E = 101
K_F = 102
K_G = 103
K_H = 104
K_I = 105
K_J = 106
K_K = 107
K_L = 108
K_M = 109
K_N = 110
K_O = 111
K_P = 112
K_Q = 113
K_R = 114
K_S = 115
K_T = 116
K_U = 117
K_V = 118
K_W = 119
K_X = 120
K_Y = 121
K_Z = 122
K_RIGHT = 1073741903
K_LEFT = 1073741904
K_DOWN = 1073741905
K_UP = 1073741906
K_ENTER = 1073741912

def __LOG_ERROR(e):
    print("[ERROR] ({})".format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)