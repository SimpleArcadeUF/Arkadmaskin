import random, time, sqlite3, math
import pygame, pygame.freetype 
from pygame.math import Vector2





#variabler
p_hp = 1
p_dmg = 2
p_vel = 4

timer = 0
game_over = False
kill_counter = 0


class Player(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((50, 30), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, pygame.Color('steelblue2'), [(0, 0), (50, 15), (0, 30)])
        self.orig_image = self.image  # Store a reference to the original.
        self.rect = self.image.get_rect(center=pos)
        self.pos = Vector2(pos)

        self.left_click = False
        self.right_click = False


    
    def update(self):
        global kill_counter
        self.rotate()
        key = pygame.key.get_pressed()
        mouse_button = pygame.mouse.get_pressed()

        #Key input
        if key[pygame.K_w]:
            self.rect[1] += -p_vel  #flyttar spelaren 3, 4 eller 6 frames
        if key[pygame.K_a]:
            self.rect[0] += -p_vel
        if key[pygame.K_s]:
            self.rect[1] += p_vel
        if key[pygame.K_d]:
            self.rect[0] += p_vel

        #Mouse input
        if mouse_button[0]:
            if self.left_click == False:
                kill_counter += 1
                self.left_click = True
        else: 
            self.left_click = False
           
        if mouse_button[2]:
            if self.right_click == False:
                print("right")
                self.right_click = True
        else:
            self.right_click = False
            

        #Collision with edge of map    
        if self.rect[0] <= 0:                           
            self.rect[0] = 0
        if self.rect[0] >= screen_width - self.rect[2]: 
            self.rect[0] = screen_width - self.rect[2]
        if self.rect[1] <= 0:                           
            self.rect[1] = 0
        if self.rect[1] >= screen_width - self.rect[3]: 
            self.rect[1] = screen_width - self.rect[3]


    def rotate(self):
        #print(self.pos)
        #print(direction)
        direction = pygame.mouse.get_pos() - Vector2(self.rect[0]+self.rect[2]/2, 
                                                     self.rect[1]+self.rect[2]/2)   #Positionen av musen från mitten av polygonen
        radius, angle = direction.as_polar()                                        #as_polar ger koordinaterna av vectorn från polarna
        self.image = pygame.transform.rotate(self.orig_image, -angle)               #roterar bilden mot musen
        self.rect = self.image.get_rect(center=self.rect.center)                    #Skapa en ny rect i centern av den gamla
    
                



class Enemy(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((50, 30), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, pygame.Color('red'), [(0, 0), (50, 15), (0, 30)])
        self.orig_image = self.image  # Store a reference to the original.
        self.rect = self.image.get_rect(center=pos)
        self.pos = Vector2(pos)
        self.speed = 3


    def move(self):
        global p_hp, game_over
        if abs(player_sprite.rect[0] - self.rect.x) > 35 or abs(player_sprite.rect[1] - self.rect.y) > 35:
            dirvect = pygame.math.Vector2(player_sprite.rect[0] - self.rect.x,
                                    player_sprite.rect[1] - self.rect.y)
            dirvect.normalize()
            dirvect.scale_to_length(self.speed)
            self.rect.move_ip(dirvect)
        else:
            if p_hp > 0:
                p_hp -= 1 
            elif p_hp <= 0:
                game_over = True


    def update(self):
        self.move()
        self.rotate()


    def rotate(self):
        player_position = pygame.math.Vector2(player_sprite.rect[0] - self.rect.x,
                                              player_sprite.rect[1] - self.rect.y)  #Positionen av spelaren från mitten av polygonen
        radius, angle = player_position.as_polar()                                  #as_polar ger koordinaterna av vectorn från polarna   
        self.image = pygame.transform.rotate(self.orig_image, -angle)               #roterar bilden mot spelaren
        self.rect = self.image.get_rect(center=self.rect.center)                    #Skapa en ny rect i centern av den gamla                


#Variabler från databasen
# def get_vars():
#     global p_id, p_name, p_hp, p_dmg, p_vel
#     sql = "SELECT * FROM player ORDER BY p_id DESC LIMIT 1"
#     data = c.execute(sql)
#     for row in data:
#         p_id = row[0]       
#         p_name = row[1]
#         p_hp = row[2]
#         p_dmg = row[3]
#         p_vel = row[4]    
#     print(p_id,p_name,p_hp,p_dmg,p_vel)

# def send_vars():
#     sql ="""INSERT INTO score (p_kills, p_timer) VALUES (?, ?)"""   
#     tot_score = (kill_counter, timer)                             
#     c.execute(sql, tot_score)
#     conn.commit()





#setup
# get_vars()
pygame.init()
clock = pygame.time.Clock()

#Game screen
screen_width, screen_height = 800, 800  
screen = pygame.display.set_mode((screen_width,screen_height))

#player
player_sprite = Player((300, 300))
player_group = pygame.sprite.Group(player_sprite)


#enemy
enemy_list = []
for i in range(0, 1):
    enemy_sprite = Enemy((random.randint(0,800), random.randint(0,800)))
    enemy_list.append(enemy_sprite)
enemy_group = pygame.sprite.Group(enemy_list)

#text
font = pygame.font.Font('freesansbold.ttf', 32)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    
    screen.fill((30, 30, 30)) #bakgrundsfärg på spelet


    #gui
    life_gui = font.render("Life : " + str(p_hp), True, (255, 255, 255))
    screen.blit(life_gui, (10, 10))

    time_gui = font.render("Time : " + str(int(timer/1000)), True, (255, 255, 255))
    screen.blit(time_gui, (10, 720))

    kills_gui = font.render("Kills : " + str(kill_counter), True, (255, 255, 255))
    screen.blit(kills_gui, (10, 760))

    if game_over == False:

        #timer
        timer = pygame.time.get_ticks() 

        #update
        player_group.update()
        enemy_group.update()

        #draw
        player_group.draw(screen)
        enemy_group.draw(screen)


    #game over screen
    if game_over == True:
        game_over_screen = font.render("Game Over", True, (255, 255, 255))
        screen.blit(game_over_screen, (300, 350))

        send_vars()
    

    pygame.display.flip()
    clock.tick(60)
