import pygame, os
from libs.SimpleArcade.gui import Frame, Button, Label, GUI
from libs.SimpleArcade import Arcade, GameList
from states import StartState, GamesState, PlayState

Arcade.init()
GameList.initGames() 

Arcade.startState = StartState.StartState()
Arcade.gamesState = GamesState.GamesState()
Arcade.playState = PlayState.PlayState()

Arcade.setCurrentState(Arcade.startState)

while Arcade.isRunning:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            Arcade.isRunning = False
            
    Arcade.screen.fill((20,20,20))
    Arcade.update()
    Arcade.currentState.update(Arcade.screen)

    key_pressed = pygame.key.get_pressed()
    if(key_pressed[pygame.K_ESCAPE]):
        Arcade.isRunning = False

    pygame.display.flip()
    
pygame.joystick.quit()
pygame.quit()