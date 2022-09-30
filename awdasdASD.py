from ursina import *
from ursina.window import Window
from ursina.camera import Camera
import numpy as np
import math as m
app = Ursina()
cube = Entity(model="cube")

newCube = Entity(model="cube", parent=cube, position=(0,0,5))
cube3 = Entity(model="sphere", position=(0,11,7))
f = np.array([[5],[0],[0]])
r = 0

def Rz(theta):
  return np.matrix([[ m.cos(theta), 0, m.sin(theta)],
                   [ 0           , 1, 0           ],
                   [-m.sin(theta), 0, m.cos(theta)]])

def update():
    global r,f
    r+=0.01
    v = Rz(r)*f
    newCube.position = cube.position+list(v)

cube.rotation_y += 45
app.run()