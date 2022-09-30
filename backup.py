from ursina import *
#from random import *


app = Ursina()
#background = Entity(model='quad', texture='pixelscape_combo', parent=camera.ui, scale=(camera.aspect_ratio,1), color=color.black)
cube = Entity(model = "cube", texture = "white_cube", parent=scene, color = color.blue, scale = 1.5, collider = "box",position = (0,0,0))
cube.double_sided = True
""" for n in range(50):
    cube = Entity(model = "cube", texture = "white_cube", parent=scene, color = choice([color.blue, color.red, color.yellow]), scale = 1, collider = "box",position = (randint(5,20),randint(5,20),randint(5,20)))
    cube.double_sided = True 
 """

spaceship = Entity(model = "untitled2.glb", scale = 0.05)
spaceship.rotation_y = 90
Sky(texture="skybox2.jpg")
def update():
    spaceship.position = camera.position+camera.forward*3
    if held_keys["w"]:
        camera.position += camera.forward *0.2
    if held_keys["s"]:
        camera.position += camera.back *0.2
    if held_keys["a"]:
        camera.position += camera.left *0.2
    if held_keys["d"]:
        camera.position += camera.right *0.2
    if held_keys["space"]:
        camera.position += camera.up *0.2
    if held_keys["c"]:
        camera.position += camera.down *0.2
    #spaceship.rotation_x = 0
    #spaceship.rotation_z = -10

    if held_keys["6"]:
        spaceship.rotation_x += 0
    if held_keys["4"]:
        spaceship.rotation_x += -0
    if held_keys["2"]:
        spaceship.rotation_z += 0
    if held_keys["8"]:
        spaceship.rotation_z += -0

    camera.rotation_x += held_keys["2"] * 0.5
    camera.rotation_x += held_keys["8"] * -0.5
    camera.rotation_y += held_keys["6"] * 0.5
    camera.rotation_y += held_keys["4"] * -0.5


    print(camera.forward)
    print(camera.position)

app.run()