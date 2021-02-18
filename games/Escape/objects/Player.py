import math, pygame

from libs.SimpleArcade import Arcade
from libs.SimpleArcade.gui import Button

from games.Escape.objects import Creature
from games.Escape.utils import Assets, Handler, Animation
from games.Escape.gui import OptionsMenu

STATE_NONE = 0
STATE_EQUIP_JETPACK = 1
STATE_FLY_JETPACK = 2
STATE_UNEQUIP_JETPACK = 3
STATE_EQUIP_DRILL = 4
STATE_USE_DRILL = 5
STATE_UNEQUIP_DRILL = 6

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

        self._animJetpackOpen = Animation.Animation(Assets.playerSheet.getImagesByRow(4, 4), 500, flip=True, continuous=False)
        self._animJetpackOpen.start()

        self._animJetpackFire = Animation.Animation(Assets.playerSheet.getImagesByRow(5, 3), 400, flip=True)
        self._animJetpackFire.start()

        self._animWalkJetpack = Animation.Animation(Assets.playerSheet.getImagesByRow(6, 2), 400, flip=True)
        self._animWalkJetpack.start()

        self._animJetpackClose = Animation.Animation(Assets.playerSheet.getImagesByRow(7, 4), 500, flip=True, continuous=False)
        self._animJetpackClose.start()


        self._animDrillOpen = Animation.Animation(Assets.playerSheet.getImagesByRow(8, 4), 500, flip=True, continuous=False)
        self._animDrillOpen.start()

        self._animDrillUse = Animation.Animation(Assets.playerSheet.getImagesByRow(9, 2), 400, flip=True)
        self._animDrillUse.start()

        self._animDrillClose = Animation.Animation(Assets.playerSheet.getImagesByRow(10, 4), 500, flip=True, continuous=False)
        self._animDrillClose.start()

        self._animDrillWalk = Animation.Animation(Assets.playerSheet.getImagesByRow(11, 2), 400, flip=True)
        self._animDrillWalk.start()

        self._currentAnim = self._animWalk
        self._currentAnimState = STATE_NONE

        self._optionsMenu = OptionsMenu.OptionsMenu(100, 20, show=False)
        self._optionsMenu.alignHorizontally(None, Arcade.ALIGN_CENTER, 0)
        self._optionsMenu.alignVertically(None, Arcade.ALIGN_CENTER, 0)

        self._optionsMenu.addButton(self._animJetpackOpen.getFramesRight()[3])
        self._optionsMenu.addButton(self._animDrillUse.getFramesRight()[0])  

    def updateGUI(self, screen):
        self._optionsMenu.update(screen)

        keys = pygame.key.get_pressed()
        if(keys[pygame.K_SPACE]):
            self._optionsMenu.show(True)

        if(self._optionsMenu.isShown()):
            #Jetpack
            if(self._optionsMenu.getButton(0).isClicked(stopClick=True)):
                self._optionsMenu.show(False)

                if(self._currentAnimState == STATE_NONE):
                    self._setCurrentAnim(self._animOpen, STATE_EQUIP_JETPACK)
                elif(self._currentAnimState == STATE_FLY_JETPACK):
                    self._setCurrentAnim(self._animJetpackClose, STATE_UNEQUIP_JETPACK)

            #Drill
            if(self._optionsMenu.getButton(1).isClicked(stopClick=True)):
                self._optionsMenu.show(False)

                if(self._currentAnimState == STATE_NONE):
                    self._setCurrentAnim(self._animOpen, STATE_EQUIP_DRILL)
                elif(self._currentAnimState == STATE_USE_DRILL):
                    self._setCurrentAnim(self._animDrillClose, STATE_UNEQUIP_DRILL)
        
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
            elif(self._currentAnimState == STATE_USE_DRILL):
                if(self._yVel < 0):
                    self._currentAnim = self._animDrillUse
                else:
                    self._currentAnim = self._animDrillWalk

        self._equipJetpackAnimation()
        self._equipDrillAnimation()
        
        screen.blit(self._currentAnim.getCurrentFrame(self._dir), (self._x - Handler.gameCamera.getXOffset(), self._y - Handler.gameCamera.getYOffset()))

    def _movement(self):
        if(Arcade.PLATFORM == Arcade.PLATFORM_DESKTOP):
            keys = pygame.key.get_pressed()

            if(self._currentAnimState != STATE_EQUIP_JETPACK and self._currentAnimState != STATE_UNEQUIP_JETPACK and self._currentAnimState != STATE_EQUIP_DRILL and self._currentAnimState != STATE_UNEQUIP_DRILL):
                if(keys[pygame.K_LEFT]):
                    self._xVel = -self._movementSpeed
                if(keys[pygame.K_RIGHT]):
                    self._xVel = self._movementSpeed
            if(keys[pygame.K_UP]):
                if(self._currentAnimState == STATE_FLY_JETPACK):
                    self._yVel = -self._thrust
                    self._grounded = False
                
                    self._setCurrentAnim(self._animJetpackFire, STATE_FLY_JETPACK)
            #else:
            #    if(self._currentAnimState == STATE_FLY_JETPACK or self._currentAnim == self._animJetpackFire):
            #        self._currentAnim = self._animJetpack

    def _setCurrentAnim(self, anim, state):
        self._currentAnim = anim
        self._currentAnim.start()
        self._currentAnimState = state

    def _equipJetpackAnimation(self):
        if(self._currentAnimState == STATE_EQUIP_JETPACK):
            if(self._currentAnim == self._animOpen):
                if(self._animOpen.isDone()):
                    self._setCurrentAnim(self._animJetpackOpen, STATE_EQUIP_JETPACK)

            if(self._currentAnim == self._animJetpackOpen):
                if(self._animJetpackOpen.isDone()):
                    self._currentAnimState = STATE_FLY_JETPACK
        
        if(self._currentAnimState == STATE_UNEQUIP_JETPACK):
            if(self._currentAnim == self._animJetpackClose):
                if(self._animJetpackClose.isDone()):
                    self._setCurrentAnim(self._animClose, STATE_UNEQUIP_JETPACK)
            if(self._currentAnim == self._animClose):
                if(self._animClose.isDone()):
                    self._setCurrentAnim(self._animIdle, STATE_NONE)

    def _equipDrillAnimation(self):
        if(self._currentAnimState == STATE_EQUIP_DRILL):
            if(self._currentAnim == self._animOpen):
                if(self._animOpen.isDone()):
                    self._setCurrentAnim(self._animDrillOpen, STATE_EQUIP_DRILL)

            if(self._currentAnim == self._animDrillOpen):
                if(self._animDrillOpen.isDone()):
                    self._currentAnimState = STATE_USE_DRILL

    def show(self, tof):
        super().show(tof)