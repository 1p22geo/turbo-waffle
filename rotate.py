import math as m
import numpy as np
from ursina import *


def Rz(theta):
  return np.matrix([[ m.cos(theta), 0, m.sin(theta)],
                   [ 0           , 1, 0           ],
                   [-m.sin(theta), 0, m.cos(theta)]])

def rotate(vector, angle,scale=0.002):

    v = list(vector)
    v = np.array([[v[0]],[v[1]],[v[2]]])
    angle = angle*((2*m.pi)/360)

    f = Rz(angle)
    g = f*v
    g = list(g)
    g = Vec3(g[0],g[1],g[2])
    g=scale*g
    return g
