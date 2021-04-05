import pygame
from games.CookieClicker.assets import state, handler
from libs.SimpleArcade import Arcade
from libs.SimpleArcade.gui import Label

class GameState:
    def __init__(self):
        super().__init__()
        
        self.cookie = pygame.image.load("games/CookieClicker/res/img/Cookie.png")
        self.cookie = pygame.transform.scale(self.cookie, (32 * 8, 32 * 8))
        self.cookieSelect = pygame.image.load("games/CookieClicker/res/img/CookieSelect.png")
        self.cookieSelect = pygame.transform.scale(self.cookieSelect, (int(32 * 8 * 1.02), int(32 * 8 * 1.02)))

        self.shop = pygame.image.load("games/CookieClicker/res/img/Shop.png")
        self.shop = pygame.transform.scale(self.shop, (32 * 4, 32 * 4))
        self.shopSelect = pygame.image.load("games/CookieClicker/res/img/ShopSelect.png")
        self.shopSelect = pygame.transform.scale(self.shopSelect, (int(32 * 4 * 1.04), int(32 * 4 * 1.04)))

        self.exit = pygame.image.load("games/CookieClicker/res/img/Exit.png")
        self.exit = pygame.transform.scale(self.exit, (32 * 4, 32 * 4))
        self.exitSelect = pygame.image.load("games/CookieClicker/res/img/ExitSelect.png")
        self.exitSelect = pygame.transform.scale(self.exitSelect, (int(32 * 4 * 1.04), int(32 * 4 * 1.04)))

        self.cookieWidth = self.cookie.get_width()
        self.cookieHeight = self.cookie.get_height()
        self.cookieAngle = 0
        self.cookieRotateSpeed = -0.2

        self.hover = "cookie"
        
    def onShow(self):
        pass
        
    def update(self, screen):
        self.cookieAngle += self.cookieRotateSpeed

        self.render(screen)
        self.inputs()
        self.gui(screen)

    def render(self, screen):
        screen.fill((0, 200, 200))

        if (self.hover == "cookie"):
            self.blitRotateCenter(screen, self.cookieSelect, (screen.get_width()/2 - self.cookieSelect.get_width()/2 , screen.get_height()/2 - self.cookieSelect.get_height() + 3), self.cookieAngle)
        
        if (self.hover == "shop"):
            screen.blit(self.shopSelect, (screen.get_width()/2 - 200 - 3, screen.get_height() - self.shopSelect.get_height() + 2))

        if (self.hover == "exit"):
            screen.blit(self.exitSelect, (screen.get_width()/2 + 100 - 3, screen.get_height() - self.shopSelect.get_height() + 2))

        self.blitRotateCenter(screen, self.cookie, (screen.get_width()/2 - self.cookie.get_width()/2, screen.get_height()/2 - self.cookie.get_height()), self.cookieAngle)
        screen.blit(self.shop, (screen.get_width()/2 - 200, screen.get_height() - self.shop.get_height()))
        screen.blit(self.exit, (screen.get_width()/2 + 100, screen.get_height() - self.exit.get_height()))


    def blitRotateCenter(self, surf, image, topleft, angle):     
        rotated_image = pygame.transform.rotate(image, angle)     
        new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)      
        surf.blit(rotated_image, new_rect.topleft)

    def inputs(self):
        if (Arcade.JOYSTICK_PRESSED_DOWN):
            if (self.hover == "cookie"):
                self.hover = "shop";

        if (Arcade.JOYSTICK_PRESSED_RIGHT):
            if (self.hover == "shop"):
                self.hover = "exit"
        
        if (Arcade.JOYSTICK_PRESSED_LEFT):
            if (self.hover == "exit"):
                self.hover = "shop"

        if (Arcade.JOYSTICK_PRESSED_UP):
            if (self.hover != "cookie"):
                self.hover = "cookie"

        if (Arcade.BUTTON_PRESSED_1):
            if (self.hover == "cookie"):
                handler.cookies += handler.cookiesPerClick
            
            if (self.hover == "exit"):
                handler.quit = True
                self.hover = "cookie"

            if (self.hover == "shop"):
                handler.setCurrentState(handler.shopState)
                

    def gui(self, screen):
        self.cookiesLabel = Label.Label(x=0,y=10)
        self.cookiesLabel.alignHorizontally(None, Arcade.ALIGN_LEFT)
        self.cookiesLabel.addText(f" Cookies: {handler.cookies}", Arcade.FONT, "black", 32)
        self.cookiesLabel.update(screen)

