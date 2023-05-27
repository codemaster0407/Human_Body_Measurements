import bpy
import numpy as np
#import matplotlib.pyplot as plt
# import mathutils
import math

# Select the object you want to subdivide
  # Replace with the name of your object
  
# def create_aggregated_plots(dictionary, keys, condition):
#     if condition == "L":
#         lengths = {key: len(arr) for key, arr in dictionary.items()}
#         keys = list(lengths.keys())
#         values = list(lengths.values())

#         # Equally space the points in the x-axis
#         x_pos = [i for i, _ in enumerate(keys)]

#         # Plot the line graph
#         plt.plot(x_pos, values, '-x')

#         # Set the labels for the x-axis and y-axis
#         plt.xlabel('Keys')
#         plt.ylabel('Values')

#         # Set the title for the plot
#         plt.title('Line Graph with Dictionary Key-Value Pairs')

#         # Set the x-tick labels to the keys
#         plt.xticks(x_pos, keys)

#         # Show the plot
#         plt.show()
#     elif condition == "dist":
#         keys = list(dictionary.keys())
#         values = list(dictionary.values())

#         # Equally space the points in the x-axis
#         x_pos = [i for i, _ in enumerate(keys)]

#         # Plot the line graph
#         plt.plot(x_pos, values, '-o')

#         # Set the labels for the x-axis and y-axis
#         plt.xlabel('Keys')
#         plt.ylabel('Values')

#         # Set the title for the plot
#         plt.title('Line Graph with Dictionary Key-Value Pairs')

#         # Set the x-tick labels to the keys
#         plt.xticks(x_pos, keys)

#         # Show the plot
#         plt.show()
        

  
filepath = "C:\\Users\\schai\\OneDrive\\Desktop\\Course Project\\smoothened.stl"  # Replace with the actual file path of your .stl model
bpy.ops.import_mesh.stl(filepath=filepath)
object_name = "smoothened"
    

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

# Bisect the mesh
bpy.ops.mesh.bisect(plane_co=(0.2, 0.2, 0.2), plane_no=(0, 0, 1), clear_inner=True, clear_outer=False)
bpy.ops.mesh.bisect(plane_co=(0.15, 0.0, 0.0), plane_no=(1.0, 0.0, 0.0))
bpy.ops.mesh.bisect(plane_co=(-0.15, 0.0, 0.0), plane_no=(1.0, 0.0, 0.0))
#bpy.ops.mesh.bisect(plane_co=(0.15, -0.04, 0.2), plane_no=(1, 0, 0), clear_inner=True, clear_outer=False)
#bpy.ops.mesh.bisect(plane_co=(-0.15, -0.04, -0.2), plane_no=(1, 0, 0), clear_inner=True, clear_outer=False)
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

print("Chest Length (in): ", estimate_one_in * len(plane_points_dict[prime_key]))
print("Chest Length (cm): ",estimate_one_cm * len(plane_points_dict[prime_key]))


#Time to estimate for waist 




# bpy.ops.object.mode_set(mode='OBJECT')

# bpy.ops.object.mode_set(mode = 'EDIT')
# bpy.ops.mesh.select_all(action = 'DESELECT')

# z_level = prime_key 

# bpy.ops.object.mode_set(mode = 'OBJECT')
# bpy.ops.object.select_all(action = 'DESELECT')
# obj.select_set(True)
# bpy.context.view_layer.objects.active = obj
# bpy.ops.object.mode_set(mode='EDIT')
# bpy.ops.mesh.select_all(action='SELECT')

# bpy.ops.object.mode_set(mode='OBJECT')
# selected_edges = []

