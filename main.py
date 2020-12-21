import pygame
from libs.SimpleArcade.gui import GUI

pygame.init()
screen = pygame.display.set_mode((0,0))#, pygame.FULLSCREEN)

pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

running = True

guiTest = GUI.GUI(color=(0,255,0), x=200, y=200, width=500, height=500)
guiTest2 = GUI.GUI(color=(255,0,0), width=200, height=200)
guiTest2.centerVertically(guiTest)
guiTest2.centerHorizontally(None)

while running:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
            
    screen.fill((255,255,255))
    
    if(pygame.key.get_pressed()[pygame.K_ESCAPE] and pygame.key.get_pressed()[pygame.K_LCTRL]):
        running = False
    
    guiTest.render(screen)
    guiTest2.render(screen)

    pygame.display.flip()
    
pygame.joystick.quit()
pygame.quit()
