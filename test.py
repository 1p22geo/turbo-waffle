from ursina import *
from random import *
import key_handling
import bullets
import cruise
import generator
from ursina.prefabs.trail_renderer import TrailRenderer

from rotate import rotate

app = Ursina()
from ursina.prefabs.ursfx import *
from ursina.shaders import unlit_shader
Shader = unlit_shader
class Offset:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.speed = 0.2
radar = Entity(model = "untitled2.glb", scale = 0.005)
shipOffset = Offset(0,0,0)
key_handler = key_handling.Key_Handling()
radar_rotation = 0
#background = Entity(model='quad', texture='pixelscape_combo', parent=camera.ui, scale=(camera.aspect_ratio,1), color=color.black)
crosshair = Entity(model = "quad", parent=camera.ui, color = color.white, scale_x = 0.005, scale_y = 0.02,position = (0,0.2))
crosshair = Entity(model = "quad", parent=camera.ui, color = color.white, scale_x = 0.02, scale_y = 0.005,position = (0,0.2))
cubes = []
ex = bullets.Explosion((0,0,0))
for n in range(5):
    """ cube = Entity(model = "cube", texture = "white_cube", color = color.red, scale = 1, collider = "box",position = (randint(-100,100),randint(-100,100),randint(-100,100)) )
    cube.double_sided = True  """
    cube = cruise.Cruise_AI(position = (randint(-100,100),randint(-100,100),randint(-100,100)), speed=1)
    cubes.append(cube)
detected = [Entity()]

spaceship = Entity(model = "untitled2.glb", scale = 0.02, collider="box", name="player")

spaceship.rotation_y = 90
Sky(texture="skybox2.jpg")

def input(key):
    if key=="space":
        ursfx([(0.0, 1.0), (0.01, 1.0), (0.36, 1.0), (0.41, 1.0), (0.73, 0.0)], volume=1.0, wave='sine', pitch=-4, pitch_change=-7, speed=3.0)
        bullet = bullets.Bullet(spaceship.position+spaceship.forward*10, spaceship.rotation)
        trail = TrailRenderer(parent=bullet, thickness=5, color=color.rgba(0,120,255,75), length=7)

gen = generator.Generator()

def update():

    global shipOffset, radar, detected, radar_rotation

    gen.update(cubes,camera.position)
    radar_rotation+=1.2
    """ shipOffset.y = 0
    shipOffset.x = 0
    shipOffset.z = 0 """
    spaceship.position = camera.position+camera.forward*3+camera.down*0.2
    camera.position += camera.forward *shipOffset.speed

    key_handler.Check_keys(shipOffset,held_keys,camera)

    destroy(radar)
    
    radar = Entity(model = "untitled2.glb", scale = 0.002, rotation_y=radar_rotation)
    radar.position = camera.position+(camera.forward*3)+(camera.right*0.7)+(camera.up*0.3)

    for e in detected:
        destroy(e)
        del e
    #print("____________________")
    eh = (camera.forward*3)+(camera.right*0.7)+(camera.up*0.3)
    


    for entity in cubes:
        if not entity.enabled:
            cubes.remove(entity)
            continue
        g = rotate(entity.position-camera.position, radar_rotation-camera.rotation_y)
        if distance(spaceship,entity) <= 200:
            #print(entity)
            if str(entity) != "sky" and str(entity) != "camera":
                temp = Entity(model="cube", scale= 0.005,position=(camera.position+eh+g))
                detected.append(temp)

    spaceship.rotation_x = camera.rotation_x+shipOffset.x
    spaceship.rotation_y = camera.rotation_y+shipOffset.y
    spaceship.rotation_z = camera.rotation_z+shipOffset.z

app.run()