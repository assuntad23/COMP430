import bpy
import math
import mathutils
bpy.ops.object.select_all(action ='SELECT')
bpy.ops.object.delete()

H =24 #hours in the clock (we'll subtract the unused ones later, but we need all 24 to form the circle)
rad=1 #r is radius of circle

#This loop lays out the hour markers. 
#Because 6 is represented twice, there are 13 markers
for i in range(H-11):
    angle = i * math.pi*2/H
    x = rad*math.cos(angle)
    y = rad*math.sin(angle)
    z = 0
    bpy.ops.mesh.primitive_cube_add(
    radius = 0.05,
    location = [x,y,z])

#add the cone, in the right location, set the bottom radius smaller    
bpy.ops.mesh.primitive_cone_add(location = (0,-1,0.95), radius1 = 0.4)

#add a plane to see the shadows better
bpy.ops.mesh.primitive_plane_add(location = (0,0,-0.05))

#scale it to encompass all the markers
bpy.ops.transform.resize(value = (1.5,1.5,1.5))

#add a spot lamp, set it to a good location, and rotate it to about a 45 degree angle
bpy.ops.object.lamp_add(type='SPOT',radius=1.0,location=(0,-2,3),rotation = (0.7,0,0))

#add camera again, so we can render
bpy.ops.object.camera_add(location = (0,0,8))