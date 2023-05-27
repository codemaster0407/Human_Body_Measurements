import bpy
import numpy as np

import math


filepath = "C:\\Users\\schai\\OneDrive\\Desktop\\Course Project\\result_pints-removebg-preview_256.obj"
bpy.ops.import_scene.obj(filepath=filepath)
object_name = "result_pints-removebg-preview_256"
    

obj = bpy.data.objects[object_name]
obj.select_set(True)
bpy.context.view_layer.objects.active = obj

# Switch to object mode
bpy.ops.object.mode_set(mode='OBJECT')

# Subdivide the mesh
subdivision_type = 'SIMPLE'  # You can choose 'SIMPLE', 'CATMULL_CLARK', or 'LOOP' for the subdivision type
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.subdivide(number_cuts=1, smoothness=0, quadcorner='INNERVERT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.subdivide(number_cuts=1, smoothness=0, quadcorner='INNERVERT')

# bpy.ops.object.mode_set(mode='OBJECT')
#Bisecting the object 
bpy.ops.object.mode_set(mode='EDIT')

mesh = obj.data

# Print the number of edges and vertices
num_edges = len(mesh.edges)
num_vertices = len(mesh.vertices)

print("Number of Edges:", num_edges)
print("Number of Vertices:", num_vertices)

# Store the coordinates of vertices in a NumPy array
vertices = np.zeros((len(mesh.vertices), 3))
for i, vertex in enumerate(mesh.vertices):
    vertices[i] = vertex.co[:]

# Store the coordinates of edges in a NumPy array
edges = np.zeros((len(mesh.edges), 2), dtype=np.float64)
for i, edge in enumerate(mesh.edges):
    edges[i] = edge.vertices[:]



min_z = np.min(vertices[:, 2])
max_z = np.max(vertices[:, 2])

height = max_z - min_z

chest_z = height*0.9 +min_z
shoulder_z = height*0.99 + min_z
waist_z = height*0.67 + min_z

print("Waist is at the value : " + str(waist_z))
# print(" Number of vertices at the waist level is "+str(waist_vertices))


# #Bisect the object at the given point


bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.bisect(plane_co=(19,19, waist_z), plane_no=(0, 0, 1), clear_inner=True, clear_outer=False)

bpy.ops.object.mode_set(mode='OBJECT')


mesh = obj.data

# Print the number of edges and vertices
num_edges = len(mesh.edges)
num_vertices = len(mesh.vertices)

print("Number of Edges:", num_edges)
print("Number of Vertices:", num_vertices)

# Store the coordinates of vertices in a NumPy array
vertices = np.zeros((len(mesh.vertices), 3))
for i, vertex in enumerate(mesh.vertices):
    vertices[i] = vertex.co[:]

# Store the coordinates of edges in a NumPy array
edges = np.zeros((len(mesh.edges), 2), dtype=np.float64)
for i, edge in enumerate(mesh.edges):
    edges[i] = edge.vertices[:]



waist_vertices = []

for i in range(len(vertices)):
    if vertices[i][2] - waist_z < 1e-8:
        waist_vertices.append(vertices[i][2])

print(len(waist_vertices))


#Assumption: 
#original waist size - 35 in, 85 cm 
original_inches = 35
original_cm = 85
estimate_one_in = original_inches/ len(waist_vertices)


print("estimation of one in :" + str(estimate_one_in))





