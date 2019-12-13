import bpy 
import math

#variable declaration
number = 8
radius = 2
height = 10

#distance from center
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()
for j in range(height):
    for i in range (number*j):
        angle = i * math.pi *2/(number*j)
        print (angle)
        x = radius *math.cos(angle)
        y = radius *math.sin(angle)
        z = j*2
        bpy.ops.mesh.primitive_ico_sphere_add(location = [x,y,z], rotation = [0,0,angle])
    radius +=2