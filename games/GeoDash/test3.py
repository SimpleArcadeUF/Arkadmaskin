import pygame, sys



clock = pygame.time.Clock()
pygame.init()

pygame.display.set_caption("Geometry test")

screen = (600,400) # set up window size

display = pygame.Surface((300, 200))

player_image = pygame.image.load("games/GeoDash/images/player_sprite.png")

ground_image = pygame.image.load("games/GeoDash/images/ground_sprite.png")
TILE_SIZE = ground_image.get_width()

game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','0','0','0'],
            ['1','0','0','0','0','0','0','0','0','1','1','1','0','0','0','0','0','0','0'],
            ['1','0','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]


while True: # game loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    
    display.fill((146,244,255))

    tile_rects = []
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            if tile == '1':
                display.blit(ground_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile != '0':
                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1

    
    surf = pygame.transform.scale(display, screen)
    display.blit(surf, (0, 0))
    pygame.display.update() # update display
    clock.tick(60) # maintain 60 fps
