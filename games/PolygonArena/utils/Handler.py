import pygame

currentState = None
MenuState = None
GameState = None
game_over = False
quit = False
kill_counter = 0


all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()