import pygame

from libs.SimpleArcade import Timer

class Animation():

    def __init__(self, frames, animDuration, continuous=True, flip=False, nextAnim=None):
        self._framesRight = frames
        self._index = 0
        self._animDuration = animDuration
        self._continious = continuous
        self._done = False
        self._nextAnim = nextAnim

        self._framesLeft = []
        if(flip == True):
            for frame in frames:
                self._framesLeft.append(pygame.transform.flip(frame, True, False))

        self._timerNextFrame = Timer.Timer(int(animDuration/len(self._framesRight)))

    def update(self):
        self._timerNextFrame.update()

        if(self._timerNextFrame.isDone()):
            if(self._index != len(self._framesRight)-1):
                self._index += 1
                self._timerNextFrame.start()
            else:
                if(self._continious == True):
                    self._index = 0
                    self._timerNextFrame.start()
                else:
                    self._done = True
    
    def start(self):
        self._timerNextFrame.start()
        self._index = 0
        self._done = False
    def reset(self):
        self._timerNextFrame.reset()
        self._index = 0
        self._done = False

    def isStarted(self):
        return self._timerNextFrame.isStarted()
    def isDone(self):
        return self._done
    def bindNextAnim(self, anim):
        self._nextAnim = anim
    def getNextAnim(self):
        return self._nextAnim

    def getCurrentFrame(self, direction=1):
        if(direction == -1):
            return self._framesLeft[self._index]
        else:
            return self._framesRight[self._index]