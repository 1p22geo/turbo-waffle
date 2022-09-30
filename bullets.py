from ursina import *
from cruise import Enemy

class Bullet(Entity):
    def __init__(self, position, vector):
        super().__init__()
        self.position = position
        self.rotation = vector
        self.vector = vector
        self.model = "bullets.glb"
        self.scale = .01
        self.collider = "box"
        self.count = 0
        self.range = 100

    def update(self):
        self.count +=1

        self.position +=self.forward*50
        hit = self.intersects()
        if hit.hit:
            if issubclass(type(hit.entity),Enemy):
                hit.entity.disable()
                Explosion(self.position)
        if self.count >=500:

            destroy(self)

class Explosion(Entity):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.model = "sphere"
        self.color = color.red
        self.scale = .1
        self.count = 0
        self.range = 100

    def update(self):
        self.count+=1
        self.color=color.rgba(150,20,20,255-self.count*6)
        self.scale*=1.1
        if self.count>=255:
            destroy(self)