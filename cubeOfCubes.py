import bpy
from random import randint
bpy.ops.object.select_all(action ='SELECT')
bpy.ops.object.delete()

for k in range(5):
    for j in range(5):
        for i in range(5):
            bpy.ops.mesh.primitive_cube_add(
            radius = 0.25,
            location = [i,j,k])