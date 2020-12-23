import pygame, os
from libs.SimpleArcade.gui import Frame, Button, Label, GUI
from libs.SimpleArcade import Arcade
from states import StartState

Arcade.init()

startState = StartState.StartState()

while Arcade.isRunning:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            Arcade.isRunning = False
            
    Arcade.screen.fill((20,20,20))
    Arcade.update()
    startState.update()
    pygame.display.flip()
    
pygame.joystick.quit()
pygame.quit()