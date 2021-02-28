import time

from games.Bloons.utils import Handler

class Timer:

    def __init__(self, speed, applyGameSpeed=False):
        super().__init__()

        self.speed = speed
        self.applyGameSpeed = applyGameSpeed
        
        self.reset()

    def start(self):
        self.started = True
        self.lastTime = time.time()*1000
        self.time = 0
        self.done = False

    def isDone(self):
        return self.done
    
    def reset(self):
        self.done = False
        self.started = False
        self.time = 0
        self.lastTime = 0

    def update(self):
        if (self.started == True):
            self.time += time.time()*1000 - self.lastTime
            self.lastTime = time.time()*1000

            speed = self.speed
            if(self.applyGameSpeed == True):
                speed = speed / Handler.GAME_SPEED

            if(self.time > speed):
                self.started = False
                self.done = True