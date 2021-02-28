# Initializing pygame + some important variables

import pygame
from random import randint

pygame.init()

score = 0
total = 0

myfont = pygame.font.SysFont('monospace', 50)

# Jumping Variables
yVel = 0
Jumping = 0
# Dead People :D
Dead = False
# Making dictionaries with settings for everything.

display = {
  "width": 800,
  "height": 600
}

character = {
  "width": 20,
  "height": 20,
  "x": 200,
  "y": 580,
  "velocity": 50
}


platform = {
    'y': 580,
    "x": 700,
    "pass": 0,
    "length": 20,
    "ammount": 2,
    "distanceApart": 50
}
spike = {
  "height": -15,
  "y": 600,
  "x": 700,
  "pass": 0,
  "length": 20,
  "ammount": 2,
  "distanceApart": 50
}
test = 0


def nextSection(a):
    spike["x"] = 700
    spike['pass'] += spike['ammount']
    spike['ammount'] = randint(1,5)
    spike['distanceApart'] = randint(2,8)*10
    return a + 1


def triangleDraw(i):  # Draws the triangles
    pygame.draw.polygon(win,(0,0,0),((spike["x"]+spike['distanceApart']*i,spike["y"]),(spike['x']+spike['distanceApart']*i+spike["length"],spike['y']),(spike['x']+spike['length']/2+spike['distanceApart']*i,spike['y']+spike['height'])))


def jump():  # Start Jumping
    global yVel
    global Jumping
    if Jumping == 0:
        Jumping = 1
        yVel = 10
        character['y'] = character['y']-yVel
        if character['y'] > platform['y']:
            Jumping = 0
        yVel -= 0.5


def cJump():  # Contine Jump
    global yVel
    global Jumping
    if Jumping == 0:
        if character['y'] > platform['y']:
            pass
        else:
            Jumping = 1
    if Jumping == 1:
        character['y'] = character['y']-yVel
        if character['y'] > platform['y']:
            Jumping = 2
        yVel -= 0.5
    elif Jumping == 2:
        Jumping =3
    elif Jumping == 3:
        Jumping = 4
    elif Jumping == 4:
        Jumping = 5
    elif Jumping == 5:
        Jumping = 0


def next():
    cJump()
    pygame.draw.rect(win, (255, 0, 0), (character["x"], character["y"], character["width"], character["height"]))
    pygame.display.update()
    spike['x'] -= 5


# Launching the window, setting it to the dimensions of the `display` dictionary.
win = pygame.display.set_mode((display["width"], display["height"]))

jump()
while True:  # Main Game Loop
    pygame.time.delay(10)
    win.fill((255, 255, 255))
    for i in range(spike['ammount']):  # Spike Drawing
        triangleDraw(i)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:  # Checks if need to Jump
        jump()
    for event in pygame.event.get():  # Quit statement 
        if event.type == pygame.QUIT:
            break
    if spike['x']+spike['distanceApart']*spike['ammount'] < character['x']:  # checks to start next section
        i = nextSection(i)
    if spike['pass'] < 100:  # Win Statement
        textsurface = myfont.render("Debug {0}".format(Dead), False, (0, 0, 0))
        textsurface2 = myfont.render("Percentage {0}%".format(spike['pass']), False, (0, 0, 0))
        win.blit(textsurface, (0,10))
        win.blit(textsurface2, (300,10))
    else:
        textsurface2 = myfont.render("YOU WIN",False, (255,0,0))
        win.blit(textsurface2, (300,10))
        break
    for i in range(spike['ammount']):  # Checks if death occurs
        if spike['x']+spike['distanceApart']*i <= character['x'] and spike['x']+spike['distanceApart']*i+spike['length'] >= character['x']:
            posOnSpike = abs(character['x'] - (spike['x']+spike['length']/2))
            test = 1
            if posOnSpike*2+spike['y'] > character['y'] and spike['y'] < character['y'] or posOnSpike*2+spike['y'] > character['y'] + character['height'] and spike['y'] < character['y']+character['height']:
                textsurface2 = myfont.render("YOU LOSE",False, (255,0,0))
                win.blit(textsurface2, (300,10))
                Dead = True
        else:
            None
    # Drawing Stuff
    next()
    if Dead:
        break
pygame.time.delay(1000)
