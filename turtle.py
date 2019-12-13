import bpy
from mathutils import Matrix, Vector
from math import cos, sin, radians

bpy.ops.object.select_all (action = 'SELECT')
bpy.ops.object.delete()

derivedString = "F+F-FF++F-F--FFF+F"
verts =[]
edges = []
angle_in_degrees = 90


def turtlePosition(derivedString):
    xStart, yStart, xEnd, yEnd = 0,0,0,0
    angle = 0
    for i in range(len(derivedString)):
        if (derivedString[i] == 'F'):
            verts.append((xStart, yStart,0))
            xEnd = xStart + cos(angle)
            yEnd = yStart + sin(angle)
            xStart = xEnd
            yStart = yEnd
        elif (derivedString[i]== '-'):
            angle = angle+radians(angle_in_degrees)
        elif (derivedString[i] == '+'):
            angle = angle-radians(angle_in_degrees)

    for i in range(len(verts) -1):
        edges.append((i,i+1))

def drawTurtle():
    profile_mesh = bpy.data.meshes.new("Base_Profile_Data")
    profile_mesh.from_pydata(verts, edges, [])
    profile_mesh.update()
    profile_object = bpy.data.objects.new ("Base_Profile", profile_mesh)
    scene = bpy.context.scene
    scene.objects.link(profile_object)
    profile_object.select = True
    
turtlePosition(derivedString)
drawTurtle()