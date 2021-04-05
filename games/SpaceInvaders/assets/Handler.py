import pygame, math

gameState = None 
startState = None
curentState = None

quit = False

def setCurrentState(state):
    global currentState, gameState
    currentState = state
    currentState.onShow()

# Enemies
RED_SPACE_SHIP = pygame.image.load("games/SpaceInvaders/res/img/pixel_ship_red_small.png")
BLUE_SPACE_SHIP = pygame.image.load("games/SpaceInvaders/res/img/pixel_ship_blue_small.png")
GREEN_SPACE_SHIP = pygame.image.load("games/SpaceInvaders/res/img/pixel_ship_green_small.png")

# Main player
YELLOW_SPACE_SHIP = pygame.image.load("games/SpaceInvaders/res/img/pixel_ship_yellow.png")

# Lasers "PEW PEW"
RED_LASER = pygame.image.load("games/SpaceInvaders/res/img/pixel_laser_red.png")
BLUE_LASER = pygame.image.load("games/SpaceInvaders/res/img/pixel_laser_blue.png")
GREEN_LASER = pygame.image.load("games/SpaceInvaders/res/img/pixel_laser_green.png")
YELLOW_LASER = pygame.image.load("games/SpaceInvaders/res/img/pixel_laser_yellow.png")

# Space background
BG = pygame.image.load("games/SpaceInvaders/res/img/background-black.png")
BGMovement = 0

def moveBG():
    global BGMovement
    if (BGMovement >= BG.get_height()):
        BGMovement = 0
    else:
        BGMovement += BGMovementSpeed
    


# Settings and configs
enemies = []
waveLength = 4
level = 0
enemyVel = 1 + (level * 0.2)
laserVel = 7.5
lives = 5
lost = False
shootChance = 2 + (level * 0.5)
if (shootChance < 1):
    shootChance = 1
BGMovementSpeed = 0.5
