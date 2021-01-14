import pygame, sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
os.chdir(path)
print(os.getcwd())
print(path)

from settings import *
from libs.SimpleArcade import Arcade
from libs.SimpleArcade.gui import Label



pygame.init()

class Game:
    def __init__(self):
        self.screen = None
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = "start"

        self.load()

    def run(self):
        while self.running:
            if (self.state == "start"):
                self.start_events()
                self.start_update()
                self.start_draw()
            elif (self.state == "playing"):
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

    # -------------------- " FUNCTIONS " -------------------- #
    def render_text(self, words, screen, size, colour, font_name, posX, posY):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_width = text.get_width()
        screen.blit(text, ((posX - text_width/2, posY)))

    def load(self):
        self.background = pygame.image.load("games/Pacman/img/maze.png")
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

    # -------------------- " START STATE " -------------------- #
    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = "playing"

    def start_update(self):
        pass

    def start_draw(self):
        self.screen.fill(BLACK)
        self.render_text('PUSH "BUTTON 1" TO START', self.screen, START_SIZE, (170, 131, 58), START_FONT, WIDTH/2, HEIGHT/2)
        self.render_text('1 Player Only', self.screen, START_SIZE, (33, 137, 156), START_FONT, WIDTH/2, HEIGHT/2 + 50)
        self.render_text('HIGH SCORE', self.screen, START_SIZE, (255, 255, 255), START_FONT, 70, 10)
        pygame.display.update()


    # -------------------- " PLAYING STATE " -------------------- #
    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def playing_update(self):
        pass

    def playing_draw(self):
        self.screen.blit(self.background, (0, 0))
        pygame.display.update()