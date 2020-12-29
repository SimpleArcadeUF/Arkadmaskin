import pygame, os
from libs.SimpleArcade.gui import Frame, Button, Label, GUI
from libs.SimpleArcade import Arcade
from states import StartState, GamesState

Arcade.init()

Arcade.startState = StartState.StartState()
Arcade.gamesState = GamesState.GamesState()

Arcade.currentState = Arcade.startState

while Arcade.isRunning:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            Arcade.isRunning = False
            
    Arcade.screen.fill((20,20,20))
    Arcade.update()
    Arcade.currentState.update(Arcade.screen)
    pygame.display.flip()
    
pygame.joystick.quit()
pygame.quit()