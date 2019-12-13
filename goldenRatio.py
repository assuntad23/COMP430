import bpy
import math

theta = 137.5 *(math.pi/180)
for n in range(0,200):
    radius = 4.0*math.sqrt(n)
    phi = n*theta;
    x = radius * math.cos(phi)
    y = radius * math.sin(phi)
    z = 0
    bpy.ops.mesh.primitive_ico_sphere_add(location = [x,y,z], size = 3)