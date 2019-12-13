import bpy
from mathutils import Vector,Matrix
import math
bpy.ops.object.select_all(action = 'SELECT')
bpy.ops.object.delete();
x,y,z = 0, 0, 0
for i in range(10):
    bpy.ops.mesh.primitive_cube_add(location = [x,y,z] )
    obj = bpy.context.active_object
    translation = (0, 0, 2*i)
    translation_matrix = Matrix.Translation(translation)
    print("Translation matrix ", translation_matrix)
    obj.matrix_world *= translation_matrix