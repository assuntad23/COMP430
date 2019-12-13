import bpy
import math
bpy.ops.object.select_all(action = 'SELECT')
bpy.ops.object.delete();

n_verts = 6
radius = 1
interior_angle = 360/n_verts
z=0
verts = []
edges = []
faces = []


for i in range(n_verts):
    x = math.cos (math.radians(interior_angle*i))
    y = math.sin (math.radians(interior_angle*i))
    verts.append((x,y,z))
    
for i in range(n_verts):
    if i == n_verts-1:
        edges.append ([i,0])
    else:
        edges.append([i,i+1])

    

faces.append([0,1,2,3,4,5])
profile_mesh = bpy.data.meshes.new("its_a_polygon")
profile_mesh.from_pydata(verts,edges,faces)
profile_mesh.update()
profile_object = bpy.data.objects.new("its_a_polygon", profile_mesh)
scene = bpy.context.scene
scene.objects.link(profile_object)
profile_object.select = True

