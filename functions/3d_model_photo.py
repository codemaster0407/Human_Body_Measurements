import bpy
import numpy as np

## Import the STL file and select the object
#filepath = "/Users/mac/Desktop/smoothened.stl"
#bpy.ops.import_mesh.stl(filepath=filepath)
object_name = "3d_model_photo"
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

# Bisect the mesh
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.bisect(plane_co=(19,19, 0.4), plane_no=(0, 0, 1), clear_inner=True, clear_outer=False)
bpy.ops.object.mode_set(mode='OBJECT')
mesh = obj.data

# Get the coordinates of vertices and edges
mesh = obj.data
vertices = np.zeros((len(mesh.vertices), 3))
for i, vertex in enumerate(mesh.vertices):
    vertices[i] = vertex.co[:]
edges = np.zeros((len(mesh.edges), 2), dtype=np.float64)
for i, edge in enumerate(mesh.edges):
    edges[i] = edge.vertices[:]

min_z = np.min(vertices[:, 2])
max_z = np.max(vertices[:, 2])

# Set the range encompassing the minimum z value
z_range = (min_z - range_size, min_z + range_size)

# Get the vertices within the z range
vertices_in_range = vertices[(vertices[:, 2] >= z_range[0]) & (vertices[:, 2] <= z_range[1])]

# Project the vertices onto a plane with z=min_z
vertices_projected = vertices_in_range.copy()
vertices_projected[:, 2] = min_z

# Calculate the circumference of the projected vertices
circumference = 0.0
for i in range(len(vertices_projected)):
    v1 = vertices_projected[i]
    v2 = vertices_projected[(i + 1) % len(vertices_projected)]
    circumference += np.linalg.norm(v2 - v1)

# Print the number of vertices and circumference
num_vertices = len(vertices_projected)
print("Number of vertices:", num_vertices)
print("Circumference:", circumference)

# Select the vertices within the z range
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='DESELECT')
for i in range(len(mesh.vertices)):
    v = mesh.vertices[i]
    if (v.co[2] >= z_range[0]) and (v.co[2] <= z_range[1]):
        v.select = True

bpy.ops.object.mode_set(mode='OBJECT')
bpy.context.view_layer.update()

