import bpy
from mathutils import Matrix

bpy.ops.object.select_all(action = 'SELECT')
bpy.ops.object.delete();
bpy.ops.mesh.primitive_cube_add(location =[0,0,0])
obj = bpy.data.objects['Cube']

#original matrix is 3x3
jack = Matrix([(4.0000, 0.0000, 0.0000, 0.0000),
                (0.0000, 4.0000, 0.0000, 0.0000),
                (0.0000, 0.0000, 4.0000, 5.0000),
                (0.0000, 0.0000, 0.0000, 1.0000)])
                
#assign 4x4 to the object                
obj.matrix_world = jack