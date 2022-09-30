from time import sleep
from ursina import *
from random import *
import cruise
import rotate


class Generator():
    def __init__(self):
        self.tick=0

    def update(self, cubes, position):
        self.tick += 1
        if randint(0,2000) == 0:
            pos = position+Vec3(randint(-100,100),randint(-100,100),randint(-100,100))
            vector=Vec3(0,randint(0,360),0)
            distance=Vec3(4,0,0)
            distance=rotate.rotate(distance,vector.y,scale=1)
            cubes.append(cruise.Cruise_AI(pos,vector=vector))
            cubes.append(cruise.Cruise_AI(pos+distance,vector=vector))
            cubes.append(cruise.Cruise_AI(pos+distance*2,vector=vector))


if __name__=="__main__":
    e = Generator()
    cubes=[]
    position=Vec3(0,0,0)
    while True:
        e.update(cubes, position)
        print(cubes)
        sleep(0.1)
