import bpy
#the vertex array contains 4 items with xyz definitions
verts = [(0,0,0),(6,0,0),(3,6,0),(3,3,6)]

# the order will determine how the face is constructed
#to construct a plane, only one face is needed
faces =[(0,1,2),(0,1,3),(1,2,3),(0,2,3)]

#defineMesh and object variables
assuntaMesh = bpy.data.meshes.new("Tetrahedron")

#this mesh variable is reference by object variable
assuntaObject = bpy.data.objects.new ("Tetrahedron", assuntaMesh)

#where it will be created - cursor location
assuntaObject.location = bpy.context.scene.cursor_location
#linking object to current scene
bpy.context.scene.objects.link(assuntaObject)

assuntaMesh.from_pydata(verts,[],faces)
assuntaMesh.update(calc_edges = True)

