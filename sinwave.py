import bpy 
from math import sin
bpy.ops.object.select_all(action ='SELECT')
bpy.ops.object.delete();
for i in range(50):
    x,y,z = i, sin(i), 0
    bpy.ops.mesh.primitive_cube_add(
    location = [x,y,z])
    bpy.ops.transform.resize (0.2,0.2,0.2)