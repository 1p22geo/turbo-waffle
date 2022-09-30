from ursina import *
from random import *
from ursina.shaders import unlit_shader
Shader = unlit_shader

app = Ursina()
offset_y = 0
offset_x = 0
offset_z = 0
speed = 0.2

#background = Entity(model='quad', texture='pixelscape_combo', parent=camera.ui, scale=(camera.aspect_ratio,1), color=color.black)
cube = Entity(model = "cube", texture = "white_cube", parent=scene, color = color.blue, scale = 1.5, collider = "box",position = (0,0,0))
cube.double_sided = True
for n in range(500):
    cube = Entity(model = "cube", texture = "white_cube", color = color.red, scale = 1, collider = "box",position = (randint(-100,100),randint(-100,100),randint(-100,100)))
    cube.double_sided = True 
EditorCamera()
app.run()