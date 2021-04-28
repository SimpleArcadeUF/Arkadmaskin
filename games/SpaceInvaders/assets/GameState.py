import pygame, random 
from games.SpaceInvaders.assets import SpaceShip, Player, Handler, Enemy
from libs.SimpleArcade import Arcade, Timer
from libs.SimpleArcade.gui import Label

class GameState():
    def __init__(self):
        super().__init__()

    def onShow(self):
        self.player = Player.Player(Arcade.SCREEN_WIDTH / 2, Arcade.SCREEN_HEIGHT - 120)
        self.guiElements()

    def update(self, screen):
        screen.fill((0, 0, 0))
        self.background(screen)
        self.enemiesLogic(screen)
        self.player.update(screen)
        self.updateGUI(screen)

        if (Handler.lost):
            Handler.level = 0
            Handler.laserVel = 0
            Handler.enemyVel = 0
            Handler.shootChance = 10000
            Handler.BGMovementSpeed = 0
            self.player.movementSpeed = 0
            self.player.canShoot = False
            self.lost(screen)

            if(Arcade.BUTTON_PRESSED_1):
                Handler.lost = False
                Handler.enemies = []
                Handler.laserVel = 7.5
                Handler.enemyVel = 1 + (Handler.level * 0.2)
                Handler.shootChance = 4 - (Handler.level * 0.5)
                Handler.BGMovementSpeed = 0.5
                Handler.lives = 5
                Handler.waveLength = 4
                self.player.movementSpeed = 7.5
                self.player.canShoot = True
                self.player.health = 100
                self.player.x = Arcade.SCREEN_WIDTH / 2
                self.player.lasers = []
            
            if (Arcade.BUTTON_PRESSED_2):
                Handler.setCurrentState(Handler.startState)
                


    def background(self, screen):
        Handler.moveBG()
        screen.blit(Handler.BG, (0, Handler.BGMovement -Handler.BG.get_height()))
        screen.blit(Handler.BG, (0, Handler.BGMovement))
        screen.blit(Handler.BG, (0, Handler.BGMovement + Handler.BG.get_height()))

    def collide(self, obj1, obj2):
        offset_x = obj2.x - obj1.x
        offset_y = obj2.y - obj1.y 
        return obj1.mask.overlap(obj2.mask, (int(offset_x), int(offset_y))) != None

    def enemiesLogic(self, screen):
        for enemy in Handler.enemies:
            enemy.update(screen)

        if (len(Handler.enemies) == 0):
            Handler.level += 1
            Handler.waveLength += 4
            for i in range(Handler.waveLength):
                enemy = Enemy.Enemy(random.randrange(75, Arcade.SCREEN_WIDTH - 75), random.randrange(-1200, -100), random.choice(["red", "blue", "green"]))

        for enemy in Handler.enemies:
            enemy.move(Handler.enemyVel)
            enemy.moveLasers(Handler.laserVel, self.player)
            if (random.randrange(0, Handler.shootChance * 60) == 1 and enemy.y >= -100):
                enemy.shoot()

            if (enemy.y + enemy.getHeight() > Arcade.SCREEN_HEIGHT):
                Handler.lives -= 1
                Handler.enemies.remove(enemy)

            if (self.collide(enemy, self.player)):
                self.player.health -= 10
                Handler.enemies.remove(enemy)

        self.player.moveLasers(Handler.laserVel, Handler.enemies)
            
    def guiElements(self):
        self.HealthText = Label.Label(20, 20)
        self.HealthText.addText(f"Lives: {Handler.lives}", Arcade.FONT, Arcade.WHITE, 32)

        self.LevelText = Label.Label(Arcade.SCREEN_WIDTH - 160, 20)
        self.LevelText.addText(f"Level: {Handler.level}", Arcade.FONT, Arcade.WHITE, 32)

        self.LostText = Label.Label(Arcade.SCREEN_WIDTH / 2, Arcade.SCREEN_HEIGHT / 2)
        self.LostText.alignHorizontally(None, Arcade.ALIGN_CENTER)
        self.LostText.alignVertically(None, Arcade.ALIGN_CENTER)
        self.LostText.addText("GAME OVER!", Arcade.FONT, Arcade.RED, 96)

    def updateGUI(self, screen):
        self.HealthText.addText(f"Lives: {Handler.lives}", Arcade.FONT, Arcade.WHITE, 32)
        self.HealthText.update(screen)
        self.LevelText.addText(f"Level: {Handler.level}", Arcade.FONT, Arcade.WHITE, 32)
        self.LevelText.update(screen)
        
    def lost(self, screen):
        self.LostText.update(screen)
        
        

