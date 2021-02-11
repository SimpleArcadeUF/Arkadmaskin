import math, pygame

from libs.SimpleArcade import Arcade

from games.Escape.objects import Creature
from games.Escape.utils import Assets, Handler, Animation

STATE_NONE = 0
STATE_EQUIP_JETPACK = 1
STATE_FLY_JETPACK = 2
STATE_UNEQUIP_JETPACK = 3

class Player(Creature.Creature):
    
    def __init__(self, tileX, tileY):
        super().__init__(0, Assets.playerSheet.getImagesByRow(0,1)[0], tileX, tileY)

        self._collisionBox = [5*Handler.IMAGE_SCALE, 9*Handler.IMAGE_SCALE, 13*Handler.IMAGE_SCALE, 11*Handler.IMAGE_SCALE]
        self._movementSpeed = 3
        self._thrust = 4
        self._spacePressed = False

        self._animIdle = Animation.Animation(Assets.playerSheet.getImagesByRow(0, 1), 10000, flip=True)
        self._animIdle.start()
        
        self._animWalk = Animation.Animation(Assets.playerSheet.getImagesByRow(1, 2), 300, flip=True)
        self._animWalk.start()

        self._animOpen = Animation.Animation(Assets.playerSheet.getImagesByRow(2, 2), 300, flip=True, continuous=False)
        self._animOpen.start()

        self._animClose = Animation.Animation(Assets.playerSheet.getImagesByRow(3, 2), 300, flip=True, continuous=False)
        self._animClose.start()

        self._animJetpack = Animation.Animation(Assets.playerSheet.getImagesByRow(4, 4), 500, flip=True, continuous=False)
        self._animJetpack.start()

        self._animJetpackFire = Animation.Animation(Assets.playerSheet.getImagesByRow(5, 3), 400, flip=True)
        self._animJetpackFire.start()

        self._animWalkJetpack = Animation.Animation(Assets.playerSheet.getImagesByRow(6, 2), 400, flip=True)
        self._animWalkJetpack.start()

        self._animJetpackClose = Animation.Animation(Assets.playerSheet.getImagesByRow(7, 4), 500, flip=True, continuous=False)
        self._animJetpackClose.start()

        self._currentAnim = self._animWalk
        self._currentAnimState = STATE_NONE

    def update(self, screen):
        super().update(screen)

        self._movement()
        self._currentAnim.update()

        if(self._currentAnimState == STATE_NONE):
            if(self._xVel == 0 and self._yVel == 0):
                self._currentAnim = self._animIdle

        if(self._xVel != 0):
            if(self._currentAnimState == STATE_NONE):
                self._currentAnim = self._animWalk
            elif(self._currentAnimState == STATE_FLY_JETPACK):
                if(self._yVel < 0):
                    self._currentAnim = self._animJetpackFire
                else:
                    self._currentAnim = self._animWalkJetpack
        
        if(self._currentAnimState == STATE_EQUIP_JETPACK):
            if(self._currentAnim == self._animOpen):
                if(self._animOpen.isDone()):
                    self._currentAnim = self._animJetpack
                    self._currentAnim.start()

            if(self._currentAnim == self._animJetpack):
                if(self._animJetpack.isDone()):
                    self._currentAnimState = STATE_FLY_JETPACK
        
        if(self._currentAnimState == STATE_UNEQUIP_JETPACK):
            if(self._currentAnim == self._animJetpackClose):
                if(self._animJetpackClose.isDone()):
                    self._currentAnim = self._animClose
                    self._currentAnim.start()
            if(self._currentAnim == self._animClose):
                if(self._animClose.isDone()):
                    self._currentAnim = self._animIdle
                    self._currentAnimState = STATE_NONE
        
        screen.blit(self._currentAnim.getCurrentFrame(self._dir), (self._x - Handler.gameCamera.getXOffset(), self._y - Handler.gameCamera.getYOffset()))

    def _movement(self):
        if(Arcade.PLATFORM == Arcade.PLATFORM_DESKTOP):
            keys = pygame.key.get_pressed()

            if(self._currentAnimState != STATE_EQUIP_JETPACK and self._currentAnimState != STATE_UNEQUIP_JETPACK):
                if(keys[pygame.K_LEFT]):
                    self._xVel = -self._movementSpeed
                if(keys[pygame.K_RIGHT]):
                    self._xVel = self._movementSpeed
            if(keys[pygame.K_UP]):
                if(self._currentAnimState == STATE_FLY_JETPACK):
                    self._yVel = -self._thrust
                    self._grounded = False
                    self._currentAnim = self._animJetpackFire
            else:
                if(self._currentAnimState == STATE_FLY_JETPACK or self._currentAnim == self._animJetpackFire):
                    self._currentAnim = self._animJetpack
            if(keys[pygame.K_SPACE]):
                if(self._spacePressed == False):
                    self._spacePressed = True
                    if(self._currentAnimState == STATE_NONE):
                        self._currentAnim = self._animOpen
                        self._currentAnim.start()
                        self._currentAnimState = STATE_EQUIP_JETPACK
                    elif(self._currentAnimState == STATE_FLY_JETPACK):
                        self._currentAnim = self._animJetpackClose
                        self._currentAnim.start()
                        self._currentAnimState = STATE_UNEQUIP_JETPACK
            else:
                self._spacePressed = False

    def show(self, tof):
        super().show(tof)