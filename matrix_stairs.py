import bpy
import math
from mathutils import Matrix


bpy.ops.object.select_all(action = 'SELECT')
bpy.ops.object.delete()

#setting starting points 
x,y,z = 0,0,0

for i in range(10):
    #add cube at location
    bpy.ops.mesh.primitive_cube_add(location = [x,y,z])
    #select active object
    obj = bpy.context.active_object
    #scale for x, y, & z
    scale_x_axis = (1,0,0)
    scale_y_axis = (0,1,0)
    scale_z_axis = (0,0,i)
    #factors to scale by
    scale_factorX = 20;
    scale_factorY = 2;
    scale_factorZ = 2*i;
    #actual math to modify cube
    scaleYmatrix = Matrix.Scale(scale_factorY, 4, scale_y_axis)
    scaleXmatrix = Matrix.Scale(scale_factorX, 4, scale_x_axis)
    scaleZmatrix = Matrix.Scale(scale_factorZ, 4, scale_z_axis)
    #translation vector & math to translate
    translateVector = (0, 2*i,2*i)
    translation_matrix = Matrix.Translation(translateVector)
    #modify cube using matrix multiplication
    obj.matrix_world = obj.matrix_world*translation_matrix*scaleXmatrix*scaleYmatrix*scaleZmatrix