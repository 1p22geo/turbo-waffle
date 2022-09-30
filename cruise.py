from ursina import *
from random import randint

class Enemy(Entity):
    def __init__(self, position, vector=Vec3(randint(0,360),randint(0,360),randint(0,360))):
        super().__init__()
        self.position = position
        self.rotation = vector
        self.vector = vector
        self.model = "cruise_shuttle.glb"
        self.scale = .05
        self.collider = "box"
    
    def update(self):
        pass


class Cruise_AI(Enemy):
    def __init__(self, position,speed=1, vector=Vec3(0,randint(0,360),0)):
        super().__init__(position, vector)
        self.speed = speed

    def update(self):
        self.position +=self.forward*self.speed