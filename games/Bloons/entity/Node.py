from games.Bloons.entity import Entity

class Node(Entity.Entity):
    
    def __init__(self, x, y):
        super().__init__(x, y, 10, True, color=(100,80,120))
    
    def update(self, screen):
        super().update(screen)