import bpy
import math
bpy.ops.object.select_all(action ='SELECT')
bpy.ops.object.delete()

H =12 #hours in the clock
S=60 #seconds in the clock
rad=1 #r is radius of circle



for i in range(S):
    angle = i * math.pi*2/S
    x = rad*math.cos(angle)
    y = rad*math.sin(angle)
    z = 0
    bpy.ops.mesh.primitive_cube_add(
    radius = 0.015,
    location = [x,y,z])

for i in range(H):
    angle = i * math.pi*2/H
    x = rad*math.cos(angle)
    y = rad*math.sin(angle)
    z = 0
    bpy.ops.mesh.primitive_cube_add(
    radius = 0.05,
    location = [x,y,z],
    rotation= [angle,0,angle])   