import bpy
import numpy as np
import math 

# Import the STL file and select the object
filepath = "C:\\Users\\schai\\OneDrive\\Desktop\\Course Project\\result_pints-removebg-preview_256.obj"
bpy.ops.import_scene.obj(filepath=filepath)
object_name = "result_pints-removebg-preview_256"
obj = bpy.data.objects[object_name]
obj.select_set(True)
bpy.context.view_layer.objects.active = obj

# Subdivide the mesh
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.subdivide(number_cuts=1, smoothness=0, quadcorner='INNERVERT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.subdivide(number_cuts=1, smoothness=0, quadcorner='INNERVERT')
bpy.ops.object.mode_set(mode='OBJECT')

# Set the range size for selecting vertices
range_size = 0.0001


#Find the height of the model


mesh = obj.data
vertices = np.zeros((len(mesh.vertices), 3))
for i, vertex in enumerate(mesh.vertices):
    vertices[i] = vertex.co[:]
edges = np.zeros((len(mesh.edges), 2), dtype=np.float64)
for i, edge in enumerate(mesh.edges):
    edges[i] = edge.vertices[:]

min_z = np.min(vertices[:, 2])
max_z = np.max(vertices[:, 2])

print(min_z, max_z)

h = max_z - min_z
print(h)

shoulder_z = h * 0.670
print(shoulder_z + min_z) 

bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.bisect(plane_co=(19,19, shoulder_z+min_z), plane_no=(0, 0, 1), clear_inner=True, clear_outer=False)

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

# print("Vertices Array:\n", vertices)
# print("Edges Array:\n", edges)

# print(vertices.shape)
# print(edges.shape)

# print(vertices[])

unique_z = []
for i in range(len(vertices)):
    unique_z.append(vertices[i][2])

unique_z = list(sorted(set(unique_z)))

print(len(unique_z))

# unique_z = sorted(unique_z)

plane_points_dict = {}

for key in unique_z:
    plane_points_dict[key] = []
    
for i in range(len(vertices)):
    if vertices[i][2] in unique_z:
        plane_points_dict[vertices[i][2]].append(np.array(vertices[i]))
        
sorted_dict = dict(sorted(plane_points_dict.items()))


plane_points_keys = list(plane_points_dict.keys())



# create_aggregated_plots(plane_points_dict, plane_points_keys, "L")
    


# print(len(unique_z),end = "\n")
# print(len(vertices))
prime_key = 0

for key in plane_points_keys:
    if len(plane_points_dict[key]) >100:
        # print(plane_points_keys)
        prime_key = key
        
print(prime_key)

print(len(plane_points_dict[prime_key]))


#Assumption: 
#original - 35 in, 85 cm 
original_inches = 35
original_cm = 85
estimate_one_in = 35/ (float)(len(plane_points_dict[prime_key]))
estimate_one_cm = 85/ (float)(len(plane_points_dict[prime_key]))

print("estimation of one cm :" + str(estimate_one_cm))
print("estimation of one in :" + str(estimate_one_in))

print("Chest Length (in): ", estimate_one_in * len(plane_points_dict[prime_key]))
print("Chest Length (cm): ",estimate_one_cm * len(plane_points_dict[prime_key]))

#waist - 35
#chest - 34
#shoulder - 43
#biceps - 11
#wrist - 7
