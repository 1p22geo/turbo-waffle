from ursina import *
app = Ursina()
cube = Entity(model = "untitled2.glb", scale = 0.1, double_sided=True, position=(0,0,10))
#cube.double_sided = True
cube.rotation_y = 90
def update():
    cube.rotation_x+=held_keys["a"]
    cube.rotation_x-=held_keys["s"]
    cube.rotation_y+=held_keys["d"]
    cube.rotation_y-=held_keys["f"]
    cube.rotation_z+=held_keys["g"]
    cube.rotation_z-=held_keys["h"]
#EditorCamera()
app.run()