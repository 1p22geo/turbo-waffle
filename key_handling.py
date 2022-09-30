from ursina import *

class Key_Handling:
    def __init__(self):
        pass

    def Check_keys(self,shipOffset, held_keys, camera):
        if held_keys["s"]:
            shipOffset.speed = 0
        elif held_keys["w"]:
            shipOffset.speed = 1
        else:
            shipOffset.speed = 0.2
        if held_keys["6"]:
            if shipOffset.y <15:
                shipOffset.y+=1
        elif held_keys["4"]:
            if shipOffset.y >-15:
                shipOffset.y-=1
        else:
            if shipOffset.y <0:
                shipOffset.y+=1
            if shipOffset.y >0:
                shipOffset.y-=1

        
        if held_keys["2"]:
            if shipOffset.x <15:
                shipOffset.x+=1
        elif held_keys["8"]:
            if shipOffset.x >-35:
                shipOffset.x-=1
        else:
            if shipOffset.x <-5:
                shipOffset.x+=1
            if shipOffset.x >-5:
                shipOffset.x-=1
        if held_keys["a"]:
            camera.rotation_x += held_keys["2"] * 2
            camera.rotation_x += held_keys["8"] * -2
            camera.rotation_y += held_keys["6"] * 2
            camera.rotation_y += held_keys["4"] * -2
        elif held_keys["d"]:
            camera.rotation_x += held_keys["2"] * 0.1
            camera.rotation_x += held_keys["8"] * -0.1
            camera.rotation_y += held_keys["6"] * 0.1
            camera.rotation_y += held_keys["4"] * -0.1
        else:
            camera.rotation_x += held_keys["2"] * 0.5
            camera.rotation_x += held_keys["8"] * -0.5
            camera.rotation_y += held_keys["6"] * 0.5
            camera.rotation_y += held_keys["4"] * -0.5