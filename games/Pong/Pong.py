import pygame, math
from libs.SimpleArcade import Game, Arcade
from libs.SimpleArcade.gui import Label

class Pong(Game.Game):

    def __init__(self):
        super().__init__("Pong", (pygame.image.load("res/images/logo.png")))

    def onPlay(self):
        self._player1 = pygame.Rect(15, 200, 5, 70)
        self._player2 = pygame.Rect(Arcade.SCREEN_WIDTH-20, 200, 5, 70)
        self._playerSpeed = 5
        self._player1Score = 0
        self._player2Score = 0
        self._ball = pygame.Rect(40, 200, 10, 10)
        self._ballSpeed = 8
        self._ballVx = self._ballSpeed
        self._ballVy = 0
        self._ballY = 200

        self._lblScore = Label.Label(y=20)
        self._lblScore.addText("0 : 0", Arcade.FONT, (255,255,255), 80)
        self._lblScore.alignHorizontally(None, Arcade.ALIGN_CENTER)

    def update(self, screen):
        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, (255,0,0), self._player1)
        pygame.draw.rect(screen, (0,0,255), self._player2)
        pygame.draw.rect(screen, (255,255,255), self._ball)
        
        self._lblScore.update(screen)

        self._playerMovement()
        self._collision()
        self._checkForScores()

        self._ballY += self._ballVy

        self._ball[0] += self._ballVx
        self._ball[1] = round(self._ballY)

    def _checkForScores(self):
        #Player 1 score
        if self._ball[0] > Arcade.SCREEN_WIDTH:
            self._player1Score += 1
            self._ballY = 200
            self._ball[0] = 80
            self._ball[1] = self._ballY
            self._ballVx = self._ballSpeed
            self._ballVy = 0
            self._updateScore()

        #Player 2 score
        if self._ball[0] < 0:
            self._player2Score += 1
            self._ballY = 200
            self._ball[0] = Arcade.SCREEN_WIDTH-100
            self._ball[1] = self._ballY
            self._ballVx = -self._ballSpeed
            self._ballVy = 0
            self._updateScore()

    def _collision(self):
        #Player 1
        if(pygame.Rect.colliderect(self._player1, self._ball)):
            relativeIntersectY = (self._player1[1]+(self._player1[3]/2)) - self._ball[1]
            normalizedRelativeIntersectionY = (relativeIntersectY/(self._player1[3]/2))
            bounceAngle = normalizedRelativeIntersectionY * 0.5
            self._ballVx = self._ballSpeed *  math.cos(bounceAngle)
            self._ballVy = self._ballSpeed * -math.sin(bounceAngle)

        #Player 2
        if(pygame.Rect.colliderect(self._player2, self._ball)):
            relativeIntersectY = (self._player2[1]+(self._player2[3]/2)) - self._ball[1]
            normalizedRelativeIntersectionY = (relativeIntersectY/(self._player2[3]/2))
            bounceAngle = normalizedRelativeIntersectionY * 0.5
            self._ballVx = -self._ballSpeed *  math.cos(bounceAngle)
            self._ballVy =  self._ballSpeed * -math.sin(bounceAngle)

        #Ball
        if((self._ball[1] + self._ballVy <= 0) or (self._ball[1] + self._ball[3] + self._ballVy >= Arcade.SCREEN_HEIGHT)):
            self._ballVy = -self._ballVy

    def _playerMovement(self):
        keys = pygame.key.get_pressed()
        #Player 1
        if keys[pygame.K_w]: #Up
            if self._player1[1] > 0:
                self._player1[1] -= self._playerSpeed
        if keys[pygame.K_s]: #Down
            if self._player1[1]+self._player1[3] < Arcade.SCREEN_HEIGHT:
                self._player1[1] += self._playerSpeed

        #Player 2
        if keys[pygame.K_UP]: #Up
            if self._player2[1] > 0:
                self._player2[1] -= self._playerSpeed
        if keys[pygame.K_DOWN]: #Down
            if self._player2[1]+self._player2[3] < Arcade.SCREEN_HEIGHT:
                self._player2[1] += self._playerSpeed
 
    def _updateScore(self):
        self._lblScore.setText(str(self._player1Score) + " : " + str(self._player2Score))
        self._lblScore.alignHorizontally(None, Arcade.ALIGN_CENTER)