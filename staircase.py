import bpy
from random import randint

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete();

height = 10;
width = 5;
depth = 10;


for z in range(height):
    for x in range(z, depth):
        for y in range(width):
            bpy.ops.mesh.primitive_cube_add(
            location= (z-x, y, z)) 